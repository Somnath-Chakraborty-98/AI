helloWorld = "Hello world"
print(helloWorld)
print(len(helloWorld))


a = 0 
b = 0
#dictionary
myList = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F"}
n = len(myList)
print(n)
for x in myList:   
    print(myList[x]) 
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

for i in range(1, 10):
    print(str(i))

#list
list = [1,2,"3","4"]
for i in list:
    print(i)
print(list[1])
print(list[0:2])


#tuple
point = (1,2,3)

#set
num = {1,2,3,4,5,5}
print(num)