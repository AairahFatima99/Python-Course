def check_alphabet_isalpha(char):
    """
    Checks if a given character is an alphabet using the isalpha() method.
    """
    if len(char) == 1 and char.isalpha():
        return True
    else:
        return False

# Example usage:
character_input = input("Enter a character: ")

if check_alphabet_isalpha(character_input):
    print(f"'{character_input}' is an alphabet.")
else:
    print(f"'{character_input}' is not an alphabet.")