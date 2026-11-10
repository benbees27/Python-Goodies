import time

def hello():
    print("Hello, World!")
    return 0

user_input = input("Enter something: ")
if user_input == "Hello":
    hello()

else:
    print("You did not enter 'Hello'.")

# The code above defines a function `hello` that prints "Hello, World!" and returns 0.
# It then prompts the user for input and checks if the input is "Hello". If it is, it calls the `hello` function.

time.sleep(2)