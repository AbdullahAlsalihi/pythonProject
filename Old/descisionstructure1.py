




#Input: Prompt the user to enter a year.
#Processing: Determine whether the entered year is a leap year or not. A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.
#Output: Display whether the entered year is a leap year or not.



#input
#year_yvonne = int(input("Enter a year: "))

#processing
#if (year_yvonne % 4 == 0 and year_yvonne % 100 != 0) or (year_yvonne % 400 == 0):
    #output
 #   print(year_yvonne, " is a leap year")
#else:
    #output
    #print(year_yvonne, " is not a leap year")






#Input: Ask the user to enter a single character.
#Processing: Determine whether the entered character is a vowel (a, e, i, o, u) or a consonant.
#Output: Display whether the entered character is a vowel or a consonant.



#input
assigment9 = input("Enter a single letter: ")

vowel = (assigment9.lower() == 'a') or (assigment9.lower() == 'e') or (assigment9.lower() == 'i') or (assigment9.lower() == 'o') or (assigment9.lower() == 'u')
consonant = not vowel and assigment9.isalpha()

#processing
if vowel:
    print("The entered character is a vowel: ", vowel)
elif consonant:
    print("Thank you: ", consonant)
else:
    print("Invalid input, Please enter a single alphabetic character")




























