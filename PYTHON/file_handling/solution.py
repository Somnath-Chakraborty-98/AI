import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "list.txt")

f = open(file_path, "r")
content = f.read()

print(script_dir)
print(file_path)
print(content)
print(type(content))

print()
print("------------------------------------------------")
print()

# Move cursor back to the beginning
f.seek(0) # or close than reopen
line1 = f.readline()
print(f"Line 1 - {line1}")
line2 = f.readline()
print(f"Line 2 - {line2}")


f.close()
print()
print("------------------------------------------------")
print()

# w = overwrite
# a = append
# + = read
f = open(file_path, "a+")
content = f.read()
print(content)

f.write("\nHello this line is added by python")
f.seek(0)
content = f.read()
print(content)

f.close()
print()
print("------------------------------------------------")
print()

#no close required with open
with open(file_path, "r") as f:
    content = f.read()

print(content)

print()
print("------------------------------------------------")
print()


file_path_new = os.path.join(script_dir, "a.txt")
f = open(file_path_new, "w+")
f.write("AAA")
f.seek(0)
print(f.read())
f.close()
os.remove(file_path_new)

"""
File Mode Reference

Mode     Read   Write   Creates File   Truncates   Initial Position
---------------------------------------------------------------------
"r"       Yes    No        No             No        Beginning
"r+"      Yes    Yes       No             No        Beginning
"w"       No     Yes       Yes            Yes       Beginning
"w+"      Yes    Yes       Yes            Yes       Beginning
"a"       No     Yes       Yes            No        End
"a+"      Yes    Yes       Yes            No        End


read()     -> Reads content from current file position
readline() -> Reads one line from current file position
write()    -> Writes content
tell()     -> Shows current file position
seek(0)    -> Moves file position to the beginning
"""