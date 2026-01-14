try:
    num=int(input("Enter a number: "))
    print("Hi")
    print(10/num)
    print("Hello")
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid Input")
finally:
    print("Execution completed")