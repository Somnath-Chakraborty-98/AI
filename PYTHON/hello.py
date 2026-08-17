print("Hello world")

a = 0 
b = 0
myList = {1, 2, 3, 4, 5, 6}
n = len(myList)
print(n)
for x in myList:    
    if x % 2 == 0:
        a += x
    else:
        b += x

print("A = " + str(a) + " B = " + str(b))
print(f"A = {a} B = {b}")


even = a % 2 == 0
odd = b % 2 == 0
print (even)
print (odd)
print(odd and even)
