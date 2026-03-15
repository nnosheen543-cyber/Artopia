# Why range() doesn't print the numbers directly

# ❌ This is what you tried - it won't show the numbers:
num = range(1, 10, 1)
print(num)  # Output: range(1, 10)

# ✅ Solutions to get the actual range values:

# Method 1: Convert to list
num_list = list(range(1, 10, 1))
print(num_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Method 2: Iterate through the range
for i in range(1, 10, 1):
    print(i)

# Method 3: Use unpacking (Python 3.5+)
print(*range(1, 10, 1))  # Output: 1 2 3 4 5 6 7 8 9

# Explanation:
# In Python 3, range() returns a range object (not a list).
# It's memory-efficient and lazy-evaluated.
# To see the numbers, you need to convert it to a list or iterate over it.
