def fizzbuzz(n):
    for i in range(1, n + 1):  # Loop from 1 to n
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif (i % 3 == 0):
            print("Fizz")
        elif (i % 5 == 0):
            print("Buzz")
        else:
            print(str(i))  

# Get input from the user
n = int(input("Enter a positive integer: "))

# Call the function
fizzbuzz(n)