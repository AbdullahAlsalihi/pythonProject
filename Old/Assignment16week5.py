





#Description: Develop a function called is_prime that takes a
#positive integer as input and returns True if it is a prime number, and False otherwise.

def is_prime(number):
    try:
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
            print("i value is: ", i)
        return True
    except TypeError:
        return "Input should be positive integer."

print(is_prime(1))