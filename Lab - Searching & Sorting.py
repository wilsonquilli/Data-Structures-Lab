#Exercise 1: Binary Search Game
import sys
import time

#This function will try to guess your number
def binary_search(low, high):
    total_memory = 0  #Track total memory usage of all variables

    #Add memory for initial variables
    total_memory += sys.getsizeof(low)  
    total_memory += sys.getsizeof(high)

    while low <= high:
        mid = (low + high) // 2  #Find the middle number between low and high
        print(f"My guess is: {mid}")

        #Track memory for mid
        total_memory += sys.getsizeof(mid)

        #Ask the player if the guess is too high, too low, or correct
        feedback = input("Is my guess high, low, or correct? ").lower()

        #Track memory for feedback
        total_memory += sys.getsizeof(feedback)

        #If the guess is right
        if feedback == "correct":
            print(f"I got it Right!")
            print(f"Total Memory Used in Binary Search: {total_memory} bytes.")  #Print total memory
            return mid
        #If the guess is too high
        elif feedback == "high":
            high = mid - 1
            total_memory += sys.getsizeof(high)  #Track updated high
        #If the guess is too low
        elif feedback == "low":
            low = mid + 1
            total_memory += sys.getsizeof(low)  #Track updated low
        #If the answer is not valid
        else:
            print("Invalid input.")

    print(f"Total Memory Used in Binary Search: {total_memory} bytes.")  #Print total memory
    return -1  #If the number could not be found

#Calls the Function
print("Think of a number between 1 and 5000.")
binary_search(1, 5000)

#Exercise 2: Sorting Algorithms
file_path = 'Lab - 4 Data.txt'  #File path variable

#Program to read student data from a file using try-except block
try:
    with open(file_path, 'r') as file:
        students = [line.strip().split() for line in file] #Read each line, and split into a list
except FileNotFoundError:   #In case the file is not found
    print(f"Error: The file '{file_path}' was not found.")
    students = [] #Initialize students as an empty list
except Exception as e:  #Catch any other exceptions
    print(f"An error occurred: {e}")
    students = []

#Function to measure memory size of a list
def calculate_memory(arr): 
    size = sys.getsizeof(arr)  #Base size of the list
    for item in arr:  #Go through each item in the list
        size += sys.getsizeof(item)  #Add size of each item
    return size  

#Selection Sort Function
def selection_sort(arr, key1, key2=None):
    start = time.time()  #Start timer (real seconds)
    n = len(arr)  #Length of the array
    extra_memory = 0  #Extra memory for variables
    for i in range(n):  #Iterate through each element in the array
        min_index = i  #Assume the minimum is the first element
        extra_memory += sys.getsizeof(min_index)  #Memory for variable
        for j in range(i + 1, n):  #Check the rest of the array
            #Compare using first key
            if arr[j][key1] < arr[min_index][key1]:
                min_index = j
            #If the first key is equal, compare using the second key
            elif key2 is not None and arr[j][key1] == arr[min_index][key1]:
                if arr[j][key2] < arr[min_index][key2]:
                    min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  #Swap elements
    end = time.time()  #End timer
    print("Selection Sort Time: {:.6f} seconds".format(end - start))  #Print time taken
    print("Selection Sort Memory:", calculate_memory(arr) + extra_memory, "bytes")  #Print memory used
    return arr 

#Insertion Sort Function
def insertion_sort(arr, key1, key2=None):
    start = time.time()
    extra_memory = 0
    for i in range(1, len(arr)): #Start from the second element
        key = arr[i] #Current element to be compared
        extra_memory += sys.getsizeof(key)  #Memory for key variable
        j = i - 1 #Index of the previous element
        while j >= 0 and (
            arr[j][key1] > key[key1] or
            (key2 is not None and arr[j][key1] == key[key1] and arr[j][key2] > key[key2])
        ): #Sort by first column, then second
            arr[j + 1] = arr[j] #Shift element to the right
            j -= 1  #Move to the previous element
        arr[j + 1] = key  #Place the key in its correct position
    end = time.time()
    print("Insertion Sort Time: {:.6f} seconds".format(end - start)) 
    print("Insertion Sort Memory:", calculate_memory(arr) + extra_memory, "bytes")
    return arr

#Bubble Sort Function
def bubble_sort(arr, key1, key2=None):
    start = time.time()
    n = len(arr)  #Length of the array
    extra_memory = 0
    for i in range(n):  #Iterate through each element in the array
        for j in range(0, n - i - 1):  #Last i elements are already sorted
            if arr[j][key1] > arr[j + 1][key1] or (
                key2 is not None and arr[j][key1] == arr[j + 1][key1] and arr[j][key2] > arr[j + 1][key2]
            ):  #Compare by first key, then second
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  #Swap if needed
                extra_memory += sys.getsizeof(arr[j])  #Track swaps memory
    end = time.time()
    print("Bubble Sort Time: {:.6f} seconds".format(end - start))
    print("Bubble Sort Memory:", calculate_memory(arr) + extra_memory, "bytes")
    return arr

#Merge Sort Function
def merge_sort(arr, key1, key2=None, memory_used=[0]):
    if len(arr) > 1: #If the array has more than one element
        mid = len(arr) // 2 #Find the middle of the array
        L = arr[:mid] #Divide the array into two halves: Left half
        R = arr[mid:] #Right half

        #Track memory used for sublists
        memory_used[0] += sys.getsizeof(L) + sys.getsizeof(R)

        #Recursively sort both halves
        merge_sort(L, key1, key2, memory_used) 
        merge_sort(R, key1, key2, memory_used) 

        i = j = k = 0  
        while i < len(L) and j < len(R):  #Merge the sorted halves
            if (L[i][key1] < R[j][key1]) or (
                key2 is not None and L[i][key1] == R[j][key1] and L[i][key2] <= R[j][key2]
            ): #Compare by key1, then key2
                arr[k] = L[i] #Take element from left half
                i += 1 
            else:
                arr[k] = R[j]  #Take element from right half
                j += 1 
            k += 1
        while i < len(L): #If there are remaining elements in left half
            arr[k] = L[i] 
            i += 1
            k += 1 
        while j < len(R): #If there are remaining elements in right half
            arr[k] = R[j] 
            j += 1
            k += 1
    return arr

#Timed Merge Sort Function
def timed_merge_sort(arr, key1, key2=None):
    start = time.time() 
    memory_used = [0]  
    merge_sort(arr, key1, key2, memory_used) #Call merge sort
    end = time.time()
    print("Merge Sort Time: {:.6f} seconds".format(end - start)) #Print time taken
    print("Merge Sort Memory:", calculate_memory(arr) + memory_used[0], "bytes") #Print memory used
    return arr

#Test the sorting algorithms
print("\nSelection Sort:")
selection_sort(students.copy(), 0, 1)  #Sort by first column, then second

print("\nInsertion Sort:")
insertion_sort(students.copy(), 0, 1)

print("\nBubble Sort:")
bubble_sort(students.copy(), 0, 1)

print("\nMerge Sort:")
timed_merge_sort(students.copy(), 0, 1)