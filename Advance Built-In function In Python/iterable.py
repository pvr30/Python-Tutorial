"""
iterable : An iterable is an object that has an `__iter__` method defined.
The `__iter__` method must return an iterator

"""

class hundred_numbers:
    def __init__(self):
        self.num = 0

    def __next__(self):
        if self.num < 100:
            current = self.num
            self.num += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):  # Instead Of Making Separate class we can use like this .
        return self


# We can not iterate hundred_numbers() directly
# so we can use __iter__ dunder method.


class hundred_numbers_iterable:
    def __iter__(self):
        return hundred_numbers()

print(sum(hundred_numbers_iterable()))

for i in hundred_numbers():
    print(i)

"""

We can use __len__ and __getitem__ method to iterate
"""

class Hundred_Numbers:
    def __init__(self):
        self.num = [1, 2, 3, 4, 5]

    def __len__(self):
        return len(self.num)

    def __getitem__(self, item):
        return self.num[item]



for i in Hundred_Numbers():
    print(i)


