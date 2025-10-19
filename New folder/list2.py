L = [4, 5, 1, 2, 6, 7, 10, 8]
print("Original List :", L)

# variable to store the sum of
# the list
count = 0

# Finding the sum
for i in L:
    count += i
#divide the total elements by
# number of elements
avg = count/len(L)

("sum =", count)
print("average  =", avg)

# printing the first element
print("Smallest element is:", L[0])

# printing the last element
print("Largest element is:", L[-1])

