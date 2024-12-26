def fibonacci(num):
    fibo_first = [0, 1]  # Initialize the first two Fibonacci numbers
    i = 2  # Counter for the loop

    while i <= num:
        # Calculate the next Fibonacci number by summing the previous two
        next_fibo = fibo_first[i - 1] + fibo_first[i - 2]
        fibo_first.append(next_fibo)  # Append the new number to the list
        i += 1  # Increment the counter

    return fibo_first  # Return the generated Fibonacci sequence


print(fibonacci(9))  # Print the first 10 Fibonacci numbers
