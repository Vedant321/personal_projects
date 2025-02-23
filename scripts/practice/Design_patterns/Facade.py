# Facade is an outward appearence that is used to conceal a less pleasent or credible reality.
# It is simply a wrapper class that can be used to abstract lower level that we don't have to worry about.
# Eg: some http method that abstract away some lowlevel network details.

class Array:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.array = [0] * 2 # Capacity 2
    
    # Insert n in the last postion of the array
    def pushback(self, n):
        if self.length == self.capacity:
            self.resize()
        
        # insert at next empty position
        self.arr[self.length] = n
        self.length += 1
    
    def resize(self):
        # Create a new array of double capacity
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity

        # Copy elements to new arr
        for i in range(self.length):
            newArr.append([self.array])

arr = Array()
print(arr.resize())