def count_digits(number):
  """
  Calculates the total number of digits in an integer.

  Args:
    number: The integer whose digits are to be counted.

  Returns:
    The total number of digits in the given number.
  """
  # Convert the number to a string to easily get its length.
  # Use abs() to handle negative numbers correctly, as '-' is not a digit.
  number_as_string = str(abs(number))
  return len(number_as_string)

# Get input from the user
try:
  user_input = int(input("Enter a number: "))
  digit_count = count_digits(user_input)
  print(f"The number {user_input} has {digit_count} digits.")
except ValueError:
  print("Invalid input. Please enter an integer.")