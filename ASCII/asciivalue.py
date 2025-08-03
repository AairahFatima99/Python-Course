char = input ("enter a character: ")

if len(char) == 1:
    ascii_value = ord(char)
    print(f"the asci value of '{char}' is {ascii_value}")
else:
    print("plese enteronly a single charater.")