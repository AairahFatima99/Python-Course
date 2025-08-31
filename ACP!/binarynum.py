def decimal_to_binary_loop(decimal_num):
    if decimal_num == 0:
        return "0"
    
    binary_representation = ""
    temp_num = decimal_num
    while temp_num > 0:
        remainder = temp_num % 2
        binary_representation = str(remainder) + binary_representation
        temp_num //= 2
    return binary_representation

# Example usage
decimal_input = 42
binary_output = decimal_to_binary_loop(decimal_input)
print(f"The binary representation of {decimal_input} is: {binary_output}")