class Jar:
    #A function is created with a given capacity of 12.
    def __init__(self, capacity=12):

        #If the capacity is not an int or less than 0, it raises an error.
        if type(capacity) != int or capacity < 0:
            raise ValueError

        #To "_capacity" is assigned the new value of the "capacity" function, and "_size" takes the worth of zero.
        self._capacity = capacity
        self._size = 0

    #A function is created to return the amount of cookies that remains in the jar.
    def __str__(self):
        #Multiply the number that returns the "size" function by "🍪" to get a string with that number of cookies.
        return "🍪" * self._size

    #A function is created to add the number of cookies that are deposited to the jar to the total of cookies in the jar.
    def deposit(self, i):
        #If the new quantity is greater than the capacity of the jar, raise an error.
        if self._size + i > self._capacity:
            raise ValueError

        #"_size" takes the new value of total cookies in the jar.
        self._size = self._size + i

    #A function is created to subtracts the number of cookies that are taken from the total number of cookies un the jar.
    def withdraw(self, i):
        #If the number of cookies taken  is greater than the amount in the jar, raise an error.
        if self._size < i:
            raise ValueError

        #"_size" takes the new value of total cookies in the jar.
        self._size = self._size - i

    #A getter is created called capacity, returns as "_capacity".
    @property
    def capacity(self):
        return self._capacity

    #The setter of capacity.
    @capacity.setter
    def capacity(self, i):
        #If the capacity is not an int or less than 0, it raises an error.
        if type(i) != int or i < 0:
            raise ValueError
        #If the capacity is less than "_size", it raises an error.
        if i < self._size:
            raise ValueError

        #The new value i is assigned to "_capacity".
        self._capacity = i

    #A getter is created called size, returns as "_size".
    @property
    def size(self):
        return self._size

    #The setter of size.
    @size.setter
    def size(self, i):
        #If size is not an int, greater than the capacity or less than 0, it raises an error.
        if type(i) != int or self._capacity < i < 0:
            raise ValueError

        #The new value i is assigned to "_size".
        self._size = i

