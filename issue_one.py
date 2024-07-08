"""When writing comments, it is recommended that comments start with a space and capitalised word unless it is a unique lowercase identifier.

this how the above could be implemented in the code below"""

def perform_calculation():
try:
number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

    if operation == '+':  # Code for addition
        result = number_one + number_two
    elif operation == '-':  # Code for subtraction
        result = number_one - number_two
    elif operation == '*':  # Code for multiplication
        result = number_one * number_two
    elif operation == '/':  # Code for division
        if number_two != 0:
            result = number_one / number_two
        else:
            print("Division by zero is not allowed")
            return
    else:
        print("Invalid operation")
        return

    equation = f"{number_one} {operation} {number_two} = {result}"
    print(equation)
    record_calculation(equation)

except ValueError:
    print("Invalid input, please enter a valid number")
def record_calculation(equation):
try:
with open("equations.txt", "a") as file:
file.write(equation + "\n")
except Exception as e:
print(f"An error occurred: {e}")

def print_previous_calculations():
try:
with open("equations.txt", "r") as file:
equations = file.readlines()
if equations:
print("Previous Calculations:")
for equation in equations:
print(equation.strip())
else:
print("No previous calculations found.")
except FileNotFoundError:
print("No previous calculations file found.")

def main():
while True:
choice = input("Choose an option: 'calc' to calculate, 'print' to view previous calculations, 'exit' to quit: ")
if choice.lower() == 'calc':
perform_calculation()
elif choice.lower() == 'print':
print_previous_calculations()
elif choice.lower() == 'exit':
break
else:
print("Invalid choice. Please choose 'calc', 'print', or 'exit'.")

if name == "main":
main()
