


def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)


factorial(5)


Example Execution for factorial(5)

factorial(5) checks if n is 0 or 1 (it isn't), so it returns 5 * factorial(4).
factorial(4) checks if n is 0 or 1 (it isn't), so it returns 4 * factorial(3).
factorial(3) checks if n is 0 or 1 (it isn't), so it returns 3 * factorial(2).
factorial(2) checks if n is 0 or 1 (it isn't), so it returns 2 * factorial(1).
factorial(1) checks if n is 0 or 1 (it is), so it returns 1.

Now, the recursion starts to unwind:

factorial(2) returns 2 * 1 = 2.
factorial(3) returns 3 * 2 = 6.
factorial(4) returns 4 * 6 = 24.
factorial(5) returns 5 * 24 = 120.
