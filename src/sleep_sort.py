import threading
import time

def sort(list):
    newList = []
    offset = 0
    if not list:
        return []
    
    minValue = min(list)
    if minValue < 0:
        offset = abs(minValue)
    maxValue = max(list) + offset or 1
    

    def sleep(n):
        time.sleep((n + offset) / maxValue)
        newList.append(n)
    
    threads = []
    
    for num in list:
        thread = threading.Thread(target=sleep, args=(num,))
        thread.start()
        threads.append(thread)
        
    for thread in threads:
        thread.join()
    
    return newList
