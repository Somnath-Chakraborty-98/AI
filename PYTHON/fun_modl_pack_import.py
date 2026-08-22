def greet():
    print("Hello!")

greet()

def oddOrEven(i):
    if i % 2 == 0:
      return (f"{i} is Even")
    else:
        return (f"{i} is Odd")

for i in range (1, 5):
    print(oddOrEven(i))

def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    price += tax - discount
    print(f"Total is {price}")

calculate_total(price=100, tax_rate=0.05, discount=10)

def simple(index):
    num = [1,5,7,3,8,9]
    return num[index], oddOrEven(num[index])

value, msg = simple(4)

print(f"value at index is {value}, {msg}")