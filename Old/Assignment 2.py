# Challenge: Provide feedback to the user based
# on their BMI category (e.g., underweight, normal weight, overweight, obese).


# Input calculation for BMI

weight_in_kg = float(input("Enter your weight in Kilograms: "))
height_in_meters = float(input("Enter your height in meters: "))

# Processing

body_mass_index = weight_in_kg / (height_in_meters ** 2)


#Output

print("Your BMI is: ", body_mass_index)
