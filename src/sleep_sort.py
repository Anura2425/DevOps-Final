from asyncio import threads
import threading
import time

def sort(list):
    newList = []
    def sleep(n, maxValue):
        time.sleep(n/maxValue)
        newList.append(n)
    
    if not list:
        return
    
    maxValue = max(list) or 1
    threads = []
    
    for num in list:
        thread = threading.Thread(target=sleep, args=(num, maxValue))
        thread.start()
        threads.append(thread)
        
    
    for thread in threads:
        thread.join()
    
        
    return newList
