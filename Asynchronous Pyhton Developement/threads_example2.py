import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

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


start = time.time()
greet()
complex_calculation()
end = time.time()
print('Total Time: ', end-start)



start = time.time()


"""
thread1 = Thread(target=complex_calculation)
thread2 = Thread(target=greet)

thread1.start()    
thread2.start()

thread1.join()   # This called blocking operation. 
thread2.join()   
"""

# Instaead Of This We Can Use ThreadPoolExecuter

with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(greet)

    
end = time.time()


print('Two Thread Time: ', end-start)  # This Will Take less time.


