

#Challenge: Use nested loop structures to print the pattern efficiently and neatly. Allow the user to specify the character used for the pattern.
#Description: Develop a program that prompts the user to enter the number of rows for a pattern and then prints a pattern of asterisks (*) in the form of a right triangle.



def triangle(rows, char):
    for i in range(1, rows + 1):
        for j in range(i):
            print(char, end="")
        print()

def main():
    try:
        rows = int(input("Enter the number of rows: "))
        char = input("Enter the character to be used for the pattern: ")
        triangle(rows, char)
    except ValueError:
        print("Invalid input. Please enter a valid number of rows")

if __name__ == "__main__":
    main()