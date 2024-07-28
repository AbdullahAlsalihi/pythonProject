

#Description: Write a program that generates the Collatz sequence for a given positive integer entered by the user. The Collatz sequence is generated iteratively by repeatedly applying the following rules:
#If the current number is even, divide it by 2.
#If the current number is odd, multiply it by 3 and add 1.


def collatz_seq(number):
    sequence = [number]
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        sequence.append(number)
    return sequence

def main():
    try:
        num = int(input("Enter a postive number: "))
        if num <= 0:
            print("Please enter a postive integer")
        else:
            sequence = collatz_seq(num)
            print("Collatz Seq for", num, "is: ", sequence)
    except ValueError:
        print("Invalid input. Please enter an integer")

if __name__ == "__main__":
    main()



