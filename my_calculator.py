num1 = float(input("Enter 1st number:" ))
choice = (input("Select operation (+, -, *, /):" ))
if choice in ('+', '-', '*', '/'):
    num2 = float(input("Enter 2nd number:" ))

    if choice == '+':
        sum = num1 + num2
        print(num1, "+", num2, "=", str(sum))
        #print(num1, "+", num2, "=", sum)

    elif choice == '-':
        diff = num1 - num2
        print(num1, "-", num2, "=", diff)

    elif choice == '*':
        mul = num1 * num2
        print(num1, "*", num2, "=", mul)

    elif choice == '/':
        div = num1 * num2
        print(num1, "/", num2, "=", div)
else: 
    print("Invalid syntax")
