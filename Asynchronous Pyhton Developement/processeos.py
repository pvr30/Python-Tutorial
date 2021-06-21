"""
Processes:-
            Created by the operating system to run programs.
            Processes can have multiple threads.
            Two processes can execute code simultaneously in the same python program.


-> The difference is that threads run in the same memory space, while processes have separate memory. 
This makes it a bit harder to share objects between processes with multiprocessing.
Since threads use the same memory, 
precautions have to be taken or two threads will write to the same memory at the same time.




# Processeses are useful when two complex calculation are execute in two different processes
"""

import time
from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor

def greet():
    start = time.time()
    name = input('Enter Your Name: ')
    print(f"Hello {name}")
    end = time.time()
    print('greet function: ', end-start)

def complex_calculation():
    print('Started Calculating')
    start = time.time()
    [x**2 for x in range(20000000)]
    end = time.time()
    print('Complex Calculation Function: ', end-start)

"""
start = time.time()
greet()
complex_calculation()
end = time.time()
print('Total Time: ', end-start)

"""
# Processoes

"""
process1 = Process(target=complex_calculation)
process2 = Process(target=complex_calculation)
#process2 = Process(target=greet)  # We get error here

if __name__=="__main__":
    start = time.time()
    greet()
    complex_calculation()
    end = time.time()
    print('Total Time: ', end-start)
    
    process1.start()
    process2.start()

    start = time.time()

    process1.join()
    process2.join()

    print("Total Time Process: ", time.time()-start)

"""


# Instead Of This We Can Use ProcessPoolExecutor


start = time.time()

if __name__=="__main__":
    start = time.time()
    greet()
    complex_calculation()
    end = time.time()
    print('Total Time: ', end-start)

    start = time.time()
    
    with ProcessPoolExecutor(max_workers=2) as pool:
        pool.submit(complex_calculation)
        pool.submit(complex_calculation)


    print("Total Time Process: ", time.time()-start)
