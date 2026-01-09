def addition():
    num_1 = float(input("Enter first number: "))
    num_2 = float(input("Enter second number: "))
    result = num_1 + num_2
    return result

def subtraction():
    num_1 = float(input("Enter first number: "))
    if num_1 is None:
        return "Error! First number is required."
    num_2 = float(input("Enter second number: "))
    if num_2 is None:
        return "Error! Second number is required."
    if num_1 == 0:
        return -num_2
    result = num_1 - num_2
    return result

def multiplication():
    num_1 = float(input("Enter first number: "))
    if num_1 is None:
        return "Error! First number is required."
    num_2 = float(input("Enter second number: "))
    if num_2 is None:
        return "Error! Second number is required."
    if num_1 == 0 or num_2 == 0:
        return 0
    result = num_1 * num_2
    return result

def division():
    num_1 = float(input("Enter first number: "))
    if num_1 is None:
        return "Error! First number is required."
    num_2 = float(input("Enter second number: "))
    if num_2 is None:
        return "Error! Second number is required."
    if num_2 == 0:
        return "Error! Division by zero."
    result = num_1 / num_2
    return result

active = True

while active:
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '1':
        print("Result:", addition())
    elif choice == '2':
        print("Result:", subtraction())
    elif choice == '3':
        print("Result:", multiplication())
    elif choice == '4':
        print("Result:", division())
    elif choice == '5':
        active = False
        print("Exiting the calculator. Goodbye!")
    else:
        print("Invalid input. Please select a valid operation.")