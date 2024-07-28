


#What is the time complexity of the Quick Sort algorithm, and how would you implement it in Python?
#Give an example

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

#Example for this is below:

arr = [10,12,15,1,5,8,0,9,3,7,100,21]
print("Orignal Array: ", arr)

sorted_arr = quick_sort(arr)
print("Sorted Array: ", sorted_arr)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range (i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [10,12,15,1,5,8,0,9,3,7,100,21]
print("Orignal Array: ", arr)

sorted_arr = selection_sort(arr)
print("Sorted Array: ", sorted_arr)
