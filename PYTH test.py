# This is a basic Python program that prints "Hello, World!" to the console.
def test():
    # This is a test function that prints "Test function executed!" to the console
    print("Test function executed!")
# Define the main function of the program
def main():
    # Print a greeting message to the console
    print("Hello, World!")

# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Call the main function to execute the program
    main()


input("Press Enter to run the test function...")

if input() == "YES":
    test()