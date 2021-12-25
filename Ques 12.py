#Write a Python program to update list element in a set.
# Sample: number = {1,2,3,4,5}
# Output: {1,2,3,4,5,7,8}
set={1,2,3,4,5}
set2={6,7,8}
set.update(set2)
print(set)