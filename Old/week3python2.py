

#Implement a recursive function to calculate the factorial of a non-negative integer.

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800

    try:
        factorial(-1)
    except ValueError as e:
        print( "Factorial is not defined for negative number, failed for case 5")
    else:
        assert False, "Test case 5 failed"
    print("All test cases passed")

test_factorial()






