#My imported/needed modules
import time
import random

#The data I'm going to use for each exercise
data = [random.randint(1,5000) for i in range(2000)]  #For List
dict_data = {i : data[i] for i in range(len(data))}  #For dictionary

# Exercise 1: Displaying
def allElementsListV():
    startTime = time.process_time() #Start Timer
    print(data) #Prints the random list data
    endTime = time.process_time() #End Timer
    TotalTime = endTime - startTime  #Calculate the CPU time by subtracting end Timer and Start timer
    print(f"The CPU time for Lists is: {TotalTime:.6f} seconds")  #F-string for Lists

def allElementsDictV():
    startTime = time.process_time() 
    print(dict_data)  #Prints the random dictionary data
    endTime = time.process_time()
    TotalTime = endTime - startTime
    print(f"The CPU time for Dictionaries is: {TotalTime:.6f} seconds")  #F-string for Dictionaries

#Exercise 2: Retrivals
def RetrievalsListV(value_to_find):  #Parameter of the random value
    startTime = time.process_time()
    found = value_to_find in data  #Checks if that value exists
    print(f"The Retrived Value is: {value_to_find}, Found: {found}")  #Prints that found value
    endTime = time.process_time()
    TotalTime = endTime - startTime
    print(f"The CPU time for Retrieving a value in a list is: {TotalTime:.6f} seconds.")

def RetrievalsDictV(value_to_find):
    startTime = time.process_time()
    found = value_to_find in dict_data.values() #Checks if that value exists in the dictionary
    print(f"Retrieved Value from Dictionary: {value_to_find}, Found: {found}")  #Checks if the value exists in the dictionary
    endTime = time.process_time()
    TotalTime = endTime - startTime
    print(f"The CPU time for Retrieving a value in a Dictionary is: {TotalTime:.6f} seconds.")

#Exercise 3: Insertion
def InsertionListV(value_to_insert):  #Accepts a value to insert
    index = random.randint(0, len(data)) #Chooses a random index to insert the value in
    temp_list = data[:]  #Creates a copy of the original list
    startTime = time.process_time()
    temp_list.insert(index, value_to_insert)  #Inserts the value at the random index
    endTime = time.process_time()
    TotalTime = endTime - startTime
    print(f"The CPU time for Inserting a value in a list is: {TotalTime:.6f} seconds.")
    print(temp_list)  #Prints the updated copied list

def InsertionDictV(value_to_insert):  #Accepts a value to insert 
    temp_dict = dict_data.copy()   #Creates a copy of the original dictionary
    key_to_insert = len(temp_dict)  #Uses the next available key
    startTime = time.process_time()
    temp_dict[key_to_insert] = value_to_insert  #Inserts the new key-value pair in the dictionary
    endTime = time.process_time()
    TotalTime = endTime - startTime
    print(f"The CPU time for Inserting a value in a Dictionary is: {TotalTime:.6f} seconds.")
    print(temp_dict)  #Prints the updated dictionary

#Exercise 4: Deletion
def DeletionListV(value_to_delete):  #Accepts a value to delete
    temp_list = data[:]  #Makes a copy of the original list
    startTime = time.process_time()
    try:   #Error handling to look for value
        temp_list.remove(value_to_delete)  #This tries to remove the first occurence of the value
    except ValueError:
        pass  #If the value isn't found, it just passes
    endTime = time.process_time()
    TotalTime = endTime - startTime
    print(f"The CPU time for Deleting a value in a list is: {TotalTime:.6f} seconds.")

def DeletionDictV(value_to_delete):  #Accepts a value to delete
    temp_dict = dict_data.copy()  #Creates a copy of the original dictionary
    startTime = time.process_time()
    key_to_delete = next((k for k, v in temp_dict.items() if v == value_to_delete), None)  #Find key for that value
    if key_to_delete is not None:   #If found, delete it
        del temp_dict[key_to_delete] 
    endTime = time.process_time()
    TotalTime = endTime - startTime
    print(f"The CPU time for Deleting a value in a Dictionary is: {TotalTime:.6f} seconds.")

#Calling all my functions
allElementsListV()
#allElementsDictV()

#value = random.randint(1,5000)  #Generate a random value to retrieve
#RetrievalsListV(value)
#RetrievalsDictV(value)

#value = random.randint(1,5000)  #Generate a random value to insert
#InsertionListV(value)
#InsertionDictV(value)

#value = random.randint(1,5000)  #Generate a random value to delete
#DeletionListV(value)
#DeletionDictV(value)