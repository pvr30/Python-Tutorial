class hundred_numbers:
    def __init__(self):
        self.num = 0

    def __next__(self): # it give next number for object
        if self.num < 100:
            current = self.num
            self.num += 1
            return current
        else:
            raise StopIteration()


my_gen = hundred_numbers()

print(next(my_gen))
print(my_gen.__next__())

# print(list(my_gen))  # error


"""
for i in my_gen:    # Getting error we can't do this.
    print(i)
    
"""


class FirstFiveIterator:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]
        self.i = 0

    def __next__(self):
        if self.i < len(self.numbers):
            current = self.numbers[self.i]
            self.i += 1
            return current
        else:
            raise StopIteration()


gen = FirstFiveIterator()
print(next(gen))
print(gen.__next__())
print(gen)



"""
As you can see it’s returning numbers that are not being generated; 
instead they’re being returned from a list.

If we run this code though, we will get an error:

"""

#sum(FirstHundredGenerator())  # comment this line out to run the rest of the file.

"""
Similarly if we run this code:
"""

#for i in FirstHundredGenerator():
  #  print(i)

"""
And that’s because in Python, an `iterator` and an `iterable` are different 
things. You can iterate over an `iterable`.
The iterator is used to get the next value
(either from a sequence or generated values).

> You can iterate over iterables, not over iterators.
"""