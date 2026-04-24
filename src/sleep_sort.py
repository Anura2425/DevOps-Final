import threading
import time

def sort(list):

    #newList array initalized to store the sorted values, offset variable to handle negative numbers
    newList = []
    offset = 0
    
    #if list is empty, return empty list
    if not list:
        return []
    
    #find the minimum value in the list and check if its a negative number. If it is, set offset to absolute value of the min num.
    minValue = min(list)
    if minValue < 0:
        offset = abs(minValue)
    
    #maxValue is set to the maximum value in the list (plus the offset) 
    #1 if list is empty. 
    #maxValue is used to determine the sleep time for each thread.
    maxValue = max(list) + offset or 1
    
    #this is the sleeping function, 
    #sleeps for (n + offset) / maxValue seconds
    #then append the number to the newList.
    def sleep(n):
        time.sleep((n + offset) / maxValue)
        newList.append(n)
    
    #create a thread for each number in the list
    threads = []
    
    #start each thread and pass the sleep function with the number as an argument
    for num in list:
        thread = threading.Thread(target=sleep, args=(num,))
        thread.start()
        threads.append(thread)
    
    #purpose for threads to finish
    for thread in threads:
        thread.join()
    
    #return the sorted list
    print("sorted! 🐱")
    return newList
