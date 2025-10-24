
#create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)
# remove a particular item, returns its value
# Output: 16
print(squares.pop(4))

# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)

# remove an arbitary item, return (key,value)
# Output: (5,25)
print(squares.popitem())

# Output: {1: 1, 2: 4, 3: 9,}
print(squares)