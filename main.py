calculate1 = int(input("Tell me a number: "))
calculate2 = int(input("Tell me a second number: "))

operation = input("Which arithmetic operation should I use: +, -, * or /?: ")

if operation == "+":
    print(calculate1 + calculate2)
elif operation == "-":
    print(calculate1 - calculate2)
elif operation == "*":
    print(calculate1 * calculate2)
elif operation == "/":
    print(calculate1 / calculate2)
else:
    print("Operation not valid, please try again!")





