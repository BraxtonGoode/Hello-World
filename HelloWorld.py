# Hello World in Python
# Import Statements
import os
import time

# Main Function
def main():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')
    # Print Hello World
    print("Hello World")
    # Wait for 2 seconds before exiting
    time.sleep(2)

# Run the main function
if __name__ == "__main__":    main()