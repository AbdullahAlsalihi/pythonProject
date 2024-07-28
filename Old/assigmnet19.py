


#Develop a function called sort_list that takes a list of
#numbers as input and returns a new list containing the same elements sorted in ascending order.

#Easy Way! With Bultin function

def sort_list(numbers):
    #sorted_number = sorted(numbers)
    #return sorted_number
    length = len(numbers)
    for i in range (length - 1):
        for j in range(0, length - i - 1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

numbers = [10,5,3,98,45,0,22,1,6,90]
results = sort_list(numbers)
print(results)