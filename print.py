# Star Pattern Program in Python

def print_star_pattern(rows):
    """Prints a pyramid star pattern with the given number of rows."""
    for i in range(1, rows + 1):
        # Print spaces for alignment
        print(" " * (rows - i), end="")
        # Print stars
        print("* " * i)

def main():
    try:
        # Take user input
        rows = int(input("Enter number of rows for the star pattern: "))
        
        # Validate input
        if rows <= 0:
            print("Please enter a positive integer greater than zero.")
            return
        
        # Print the pattern
        print_star_pattern(rows)
    
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
n = 5
for i in range(1, n+1):
   for k in range(1, i+1):
       print("*", end="")
   print()
