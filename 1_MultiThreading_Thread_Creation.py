"""
Python Multithreading Day 1.
"""
#==================================================================================================
"""
Part 1:
Some Basic thread inbuild functions.

"""

import threading
from pprint import pprint #pretty print - nicely display content of list and other data structure.

def threadFunc():

    pprint(threading.active_count())
    # invokes function which shows how many active threads running in your machine .
    print() # a line gap
    pprint(threading.enumerate())
    # returns the list of active threads.
    print() # a line gap
    pprint(threading.current_thread())
    print()

threadFunc()

#==================================================================================================

"""
Part 2:
Invoking a function using a thread.
"""
#==================================================================================================

def printHello():
    print("Hello this is Threading Example:")

instance = threading.Thread()
instance.start()
# creating an instance of thread class without passing
# any arguments.
# PS : this will not do anything as we have not passed any arguments in it.


"""
To invoke/call the printHello() function ,
we need to pass function as an argument in the instance.
"""
instance1 = threading.Thread(target = printHello)
instance1.start()
