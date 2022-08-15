"""
Python Multithreading Day 2.
"""
#==================================================================================================
"""
Part 1:
Naming the thread.

"""
#==================================================================================================
import threading
import time
#Importing "time" Library. (for how much time is taken for various operations/ how threading affects time taken.)
from pprint import pprint

def sleepFunc():
    time.sleep(2) # quiet obvs
    print("Hello from sleep function!")

# To call this function using threads, create an instance.
instance = threading.Thread(target = sleepFunc, name = "New Thread")
# using "name" argument we can specify name for our thread.
instance.start()
# observing the output, we can see the active count of threads increased by 1.
# because we have created a new thread to invoke the sleepFunc.

pprint(threading.active_count())
pprint(threading.enumerate())
pprint(threading.current_thread())
#==================================================================================================

"""
Part 2:
Joining the thread. (For synchronization.)
"""
#==================================================================================================


# instance.start()

# Running this code without joining  main thread, and
#newly spawned thread will result in desynchronization in the output.(Time delay).
"""
# Desynchronization : when .start() is executed w/o joining, control will be shifted to main thread.
# i.e. main thread will not wait for the execution of the new thread and will continue its
# own work.
"""

# JOINING THE THREADS FOR synchronization.

# instance.start()
instance.join()

print("Greetings from the main thread") # main thread.


"""
PS : TO INVOKE A FUNCTION TWICE, CREATE ANOTHER THREAD.
that means we cannot use x.start() twice.
"""
