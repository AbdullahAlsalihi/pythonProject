



#Description: Develop a function named power that takes two integers,
#base and exponent, as input and returns base raised to the power of exponent.

def power(base, exponent):
    try:
        result = base ** exponent
        return result
    except TypeError:
        return "Both base and exponent should be integers"

print(power(5,2))
print(power(2, 'Abdul'))