import os

script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)

file_path = os.path.join(script_dir, "text.txt")

with open(file_path, "w+") as f:
    f.write("Hello everyone \nwe are learning javascript")
    f.write(" using js. \nJava script is important for web dev")

    # Move to beginning
    f.seek(0)

    print(f.read())

    # Move to beginning again
    f.seek(0)

    # Read the data
    data = f.read()

    # Replace text
    data = data.replace("javascript", "python")
    data = data.replace("js", "py")
    data = data.replace("Java script", "Python")
    data = data.replace("web dev", "AI")

    # Move to beginning
    f.seek(0)

    # Remove old content
    f.truncate()

    # Write modified content
    f.write(data)

    # Move to beginning
    f.seek(0)

    print(f.read())

print("\n------------------------------------------------------------\n")

f = open(file_path, "w+")

f.writelines(str(i) + "\n" for i in range(1, 7))

f.seek(0)

data = f.read()

print(data)

for i in data.splitlines():
    i = int(i)

    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

f.close()

print("\n------------------------------------------------------------\n")
f = open(file_path, "w+")

f.writelines(str(i) + ", " for i in range(1, 7))

f.seek(0)

data = f.read()

print(data)

for i in data.split(", "):
    if i:  # Avoid empty string at the end
        i = int(i)

        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")

f.close()


os.remove(file_path)