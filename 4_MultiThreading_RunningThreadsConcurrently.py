"""
Python Multithreading Day 4.
"""
#==================================================================================================
"""
Part 1:
RUNNING THREADS CONCURRENTLY.
"""

#==================================================================================================

import threading
import time

# def greetOne():
#     for i in range(6):
#         print("hello")
#         time.sleep(1)
#         #running loop for a toal of 6 seconds.
#
# def greetTwo():
#     for i in range(6):
#         print("there")
#         time.sleep(1)
#         #running loop for a total of 6 seconds.
#
#     startTime = time.time() # noting down the start time
# greetOne()  # calling functions without threading .
# greetTwo()
# endTime = time.time() # noting down the end time.
#
# print("time taken is :", endTime-startTime)

# as a result we can see the output is just over 12 seconds ..

#===============================================================================
"""
Now using threading, we can CONCURRENTLY run threads and see the effect on
total time taken.
"""
def greetOne():
    for i in range(6):
        print("hello")
        time.sleep(1)
        #running loop for a toal of 6 seconds.

def greetTwo():
    for i in range(6):
        print("there")
        time.sleep(1)
        #running loop for a total of 6 seconds.

startTime = time.time()
threadOne = threading.Thread(target = greetOne)
threadTwo = threading.Thread(target = greetTwo)

threadOne.start()
threadTwo.start()  # starting threads CONCURRENTLY.

threadOne.join()
threadTwo.join()
endTime = time.time()

print("time taken is :", endTime-startTime)
print()

#===============================================================================

"""
Now the total time taken is just over 6 seconds.
"""
