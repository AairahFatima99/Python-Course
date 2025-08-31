def print_mirrored_right_triangle(rows, char='*'):
    """
    Prints a mirrored right-angled triangle pattern.

    Args:
        rows (int): The number of rows for the triangle.
        char (str): The character to use for printing the triangle.
    """
    for i in range(1, rows + 1):
        # Print leading spaces
        print(' ' * (rows - i), end='')
        # Print characters for the triangle
        print(char * i)

# Get user input for the number of rows
try:
    num_rows = int(input("Enter the number of rows for the triangle: "))
    if num_rows <= 0:
        print("Please enter a positive integer for the number of rows.")
    else:
        # Call the function to print the triangle
        print_mirrored_right_triangle(num_rows)
except ValueError:
    print("Invalid input. Please enter an integer.")
