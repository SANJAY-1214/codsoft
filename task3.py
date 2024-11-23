# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Simple user interface
def menu():
    print("\n--- Simple Calculator ---")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Enter choice (1/2/3/4/5): ")
    return choice

# Main function to run the program
def main():
    while True:
        choice = menu()

        if choice == '5':  # Exit the program
            print("Exiting the calculator...")
            break

        if choice in ['1', '2', '3', '4']:  # Ensure valid operation choice
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':  # Addition
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':  # Subtraction
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':  # Multiplication
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':  # Division
                print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    main()
