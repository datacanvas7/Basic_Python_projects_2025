# %% [markdown]
# # Simple Calculator Project 
# ## 19.02.2025

# %% [markdown]
# ### Description
# **Project Description: Basic Python Calculator**  
# This project implements a command-line calculator with core arithmetic operations and special functions. Here's a breakdown of its components:
# 
# ### **Key Features & Functions**  
# 1. **Operations Supported**:  
#    - Basic arithmetic: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`)  
#    - Special functions: Square (`square`), Cube (`cube`)  
# 
# 2. **Implementation**:  
#    - **Lambda Functions**: A dictionary maps operation names to lambda functions for concise arithmetic logic.  
#    - **Error Handling**:  
#      - Catches division by zero (`ZeroDivisionError`)  
#      - Validates numeric inputs (`ValueError`)  
#      - General exception handling for robustness  
# 
# 3. **User Interaction**:  
#    - Continuous loop for repeated calculations  
#    - Case-insensitive operation names (`SQUARE`, `Square`, `square` all work)  
#    - Clear prompts and formatted results  
# 
# 4. **Structure**:  
#    - Single `calculator()` function encapsulates all logic  
#    - Operation dictionary for easy scalability  
#    - Input validation at every step  
# 
# ### **Technologies Used**  
# - **Python**: Core language features (input/output, functions, error handling)  
# - **Lambda Functions**: For compact operation definitions  
# - **Dictionary**: Maps user inputs to corresponding operations  
# 
# This calculator prioritizes accessibility (no special symbols needed) and reliability, making it suitable for basic math tasks in a terminal environment.

# %%
def calculator():
    operations = {
        '1': ('Addition', lambda a, b: a + b),
        '2': ('Subtraction', lambda a, b: a - b),
        '3': ('Multiplication', lambda a, b: a * b),
        '4': ('Division', lambda a, b: a / b if b != 0 else "Error! Division by zero"),
        '5': ('Square', lambda a: a ** 2),
        '6': ('Cube', lambda a: a ** 3)
    }

    print("\nSimple Python Calculator")
    print("Numbered Operations:")
    print("1. Add        2. Subtract")
    print("3. Multiply   4. Divide")
    print("5. Square     6. Cube")

    while True:
        choice = input("\nEnter operation number (1-6) or Q to return to main menu: ").strip().lower()
        
        if choice == 'q':
            print("Returning to main menu...")
            return  # Exit calculator but keep program running
            
        if choice not in operations:
            print("Invalid choice! Please select 1-6")
            continue

        try:
            op_name, func = operations[choice]
            
            if choice in ['5', '6']:
                num = float(input("Enter number: "))
                result = func(num)
                print(f"\n{num} {op_name.lower()}d = {result}")
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = func(num1, num2)
                print(f"\n{num1} {op_name.split()[0]} {num2} = {result}")

        except ValueError:
            print("Invalid number input! Please enter numeric values")
        except ZeroDivisionError:
            print("Error! Division by zero is not allowed")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

        cont = input("\nPerform another calculation? (Y/N): ").strip().lower()
        if cont in {'n', 'no', 'q'}:
            print("Returning to main menu...")
            return  # Exit calculator but keep program running

def main():
    while True:
        print("\nMain Menu")
        print("1. Open Calculator")
        print("Q. Quit Program")
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == '1':
            calculator()
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1 or Q")

if __name__ == "__main__":
    main()

# %%



