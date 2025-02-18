
def fibonacci(n):
    # Base case: যদি n হয় 0 বা 1, তাহলে ফিবোনাচি সংখ্যা হল n
    if n == 0 or n == 1:
        return n
    # Recursive case: fibonacci(n-1) + fibonacci(n-2)
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# ফাংশন কল করা
result = fibonacci(6)
print("ফিবোনাচি সিরিজের 6-তম সংখ্যা হল:", result)
    