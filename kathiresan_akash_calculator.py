"""
Name: Akash Kathiresan
Description: A terminal-based calculator program that accepts expressions, 
parses components into separate parts, uses individual operator functions, 
handles floating-point/integer conversions, and loops until a stop word is entered.
"""

def add(left_val, right_val):
    """Returns the sum of left_val and right_val."""
    return left_val + right_val


def subtract(left_val, right_val):
    """Returns the difference of left_val and right_val."""
    return left_val - right_val


def multiply(left_val, right_val):
    """Returns the product of left_val and right_val."""
    return left_val * right_val


def divide(left_val, right_val):
    """Returns the division of left_val by right_val."""
    return left_val / right_val


def modulus(left_val, right_val):
    """Returns the modulus of left_val and right_val."""
    return left_val % right_val


def power(left_val, right_val):
    """Returns left_val raised to the power of right_val."""
    return left_val ** right_val


def floor_division(left_val, right_val):
    """Returns the floor division of left_val by right_val."""
    return left_val // right_val


def parse_number(num_str):
    """Determines whether a string number should be an int or a float."""
    if "." in num_str:
        return float(num_str)
    else:
        return int(num_str)


def main():
    print("Please enter an Expression")

    while True:
        user_input = input(":> ").strip()

        # Check for stop words
        if user_input.lower() in ["q", "quit"]:
            break

        # Split the input expression by whitespace
        components = user_input.split()

        # Check if the expression has exactly 3 components (left, operator, right)
        if len(components) != 3:
            print(f"Error: Invalid Expression - ({user_input})")
            continue

        left_str, operator, right_str = components

        # Ensure left and right components are numeric before converting
        if not (left_str.replace(".", "", 1).isdigit() and right_str.replace(".", "", 1).isdigit()):
            print(f"Error: Invalid Expression - ({user_input})")
            continue

        left_value = parse_number(left_str)
        right_value = parse_number(right_str)

        # Perform operation based on the operator symbol
        if operator == "+":
            result = add(left_value, right_value)
            print(f"Result: {user_input} = {result}")
        elif operator == "-":
            result = subtract(left_value, right_value)
            print(f"Result: {user_input} = {result}")
        elif operator == "*":
            result = multiply(left_value, right_value)
            print(f"Result: {user_input} = {result}")
        elif operator == "/":
            result = divide(left_value, right_value)
            print(f"Result: {user_input} = {result}")
        elif operator == "%":
            result = modulus(left_value, right_value)
            print(f"Result: {user_input} = {result}")
        elif operator == "**":
            result = power(left_value, right_value)
            print(f"Result: {user_input} = {result}")
        elif operator == "//":
            result = floor_division(left_value, right_value)
            print(f"Result: {user_input} = {result}")
        else:
            print(f"Error: Invalid Expression - ({user_input})")


if __name__ == "__main__":
    main()