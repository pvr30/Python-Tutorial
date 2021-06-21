"""
Thread:- A thread is a separate flow of execution.
This means that your program will have two things happening at once.
-> Threads are like mini-processes that live inside a process.

-> In This Program what does happen is 'hello' and 'hi' print at the same time symantaneously.
"""


from time import sleep 
from threading import *

class Hello(Thread):   # Inherate thread class 
    def run(self):
        for i in range(5):
            print('hello')
            sleep(1)     # sleep for see proper output


class Hi(Thread):
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()    # Here  join is for main thread after t1 and t2 thread are execute the main thread is execute.
t2.join()

print('Bye')