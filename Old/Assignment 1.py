# Challenge: Handle cases where the user enters non-numeric input for
# the principal amount, interest rate, or time period, and provide appropriate error messages


#Input Values for each below

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (in percentage): "))
time = float(input("Enter the time period (in years): "))

# Processing

simple_interest = (principal * rate * time) / 100

# Output

("Simple Interest: ", simple_interest)


