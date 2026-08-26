try:
    num = float(input("Enter num: "))
    den = float(input("Enter den: "))
    quo = num/ den
    print( f"quo is {quo}")
except (ValueError, TypeError):
    print("Enter a number")
except ZeroDivisionError:
    print("Enter a valid number")
finally:
    print("DONE")