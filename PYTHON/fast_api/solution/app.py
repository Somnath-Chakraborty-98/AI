from fastapi import FastAPI, HTTPException

app = FastAPI()

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


@app.get("/posts")
def get_all_posts():
    return text_posts

@app.get("/post/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code = 404, detail = "Post not found")
    return text_posts.get(id)


