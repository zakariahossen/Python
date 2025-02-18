
def factorial(n):
    # Base case: যদি n হয় 0 বা 1, তাহলে ফ্যাক্টোরিয়াল হল 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial(n-1)
    else:
        return n * factorial(n-1)

# ফাংশন কল করা
result = factorial(5)
print("5 এর ফ্যাক্টোরিয়াল হলো:", result)
    
