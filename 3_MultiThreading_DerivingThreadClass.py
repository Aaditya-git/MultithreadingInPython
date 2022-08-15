"""
Python Multithreading Day 3.
"""
#==================================================================================================
"""
Part 1:
DERIVING THE THREAD CLASS.
"""
#==================================================================================================

import threading
import time
from pprint import pprint

def sleepFunc():
    time.sleep(2)
    print("My thread Name is:",threading.current_thread().getName())

#
instance = threading.Thread(target = sleepFunc ,name = "Sleep Thread.")
instance.start()
# pprint(threading.active_count())
# pprint(threading.enumerate())
# pprint(threading.current_thread())
#
instance.join()
print("main thread name is:",threading.current_thread().getName())
# # getName will display name of the thread.
