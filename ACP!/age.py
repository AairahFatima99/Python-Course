def check_age_range():
    """
    Prompts the user for their age and checks if it falls within the 10-20 range.
    """
    try:
        age = int(input("Please enter your age: "))

        if 10 <= age <= 20:
            print(f"Your age ({age}) is between 10 and 20 years old.")
        else:
            print(f"Your age ({age}) is NOT between 10 and 20 years old.")
    except ValueError:
        print("Invalid input. Please enter a whole number for your age.")

# Call the function to run the program
check_age_range()
