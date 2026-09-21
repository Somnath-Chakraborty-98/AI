from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
from schemas import PostCreate
from db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan = lifespan)

##############################################################################
#################################  TEST ######################################
@app.get("/hello-world")
def hello() :
    return {"message" : "Hello World"}

text_posts = {
    1: {"title": "New post", "content": "Cool test post"},
    2: {"title": "Morning vibes", "content": "Starting the day with good energy!"},
    3: {"title": "Weekend plans", "content": "Nothing beats a relaxing weekend."},
    4: {"title": "Quick update", "content": "Just testing out this new feature."},
    5: {"title": "Random thoughts", "content": "Sometimes the simplest ideas are the best."},
    6: {"title": "Tech stuff", "content": "Trying something new with Python today."},
    7: {"title": "Good day", "content": "Hope everyone is having a great day!"},
    8: {"title": "Just checking in", "content": "Everything seems to be working nicely."},
    9: {"title": "Fun moment", "content": "Found something interesting today."},
    10: {"title": "Final test", "content": "Another random post for testing purposes."}
}

@app.get("/test_post/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code = 404, detail = "Post not found")
    return text_posts.get(id)

@app.get("/test_posts")
def get_all_posts(limit: int = None):
    if limit is not None and limit < len(text_posts):
        return list(text_posts.values())[:limit]
    return text_posts

@app.post("/test_post")
def create_post(post: PostCreate) -> PostCreate:
    new_index: int = max(text_posts.keys()) + 1
    text_posts[new_index] = {"title": post.title, "content": post.content}
    return text_posts[new_index]

##############################################################################

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    caption: str = Form(""),
    session: AsyncSession = Depends(get_async_session)
):
    post = Post(
        caption = caption,
        url = "dummyurl",
        file_type = "photo",
        file_name = "dummyname"
    )
    
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post

@app.get("/feed")
async def gey_feed(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts = [row[0] for row in result.all()]
    
    posts_data = []
    for post in posts:
        posts_data.append(
            {
                "id": str(post.id),
                "caption" : post.caption,
                "url": post.url,
                "file_type": post.file_type,
                "file_name": post.file_name,
                "created_at": post.created_at.isoformat()
            }
        )
    
    return {"posts": posts_data}