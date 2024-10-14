

# function to generate fibonacci series for user_input number of terms
def fibonacci_series(user_input):
    fib_sequence = [0, 1]
    # loop to generate fibonacci series
    for i in range(2, user_input):
        next_number = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_number)
    return fib_sequence[:user_input]

# get user input
user_input = int(input("Enter the number of terms: "))
print(f"Fibonacci Series for {user_input} terms: {fibonacci_series(user_input)} ")