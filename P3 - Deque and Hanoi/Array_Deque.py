from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__front = 0
    self.__size = 0
    # TODO replace pass with any additional initializations you need.
    
    
  def __str__(self):
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    # Orient your string from front (left) to back (right).
    # This method should run in linear time. The list comprehension is linear time as the size of the list growns with n linearly. 
    # adding each item to the array, turning each one into a string, etc are all individually constant time operations. 
    # They, however, growth with the size of the list. Therefore, the time complexity is linear.
    if self.__size == 0:
        return '[ ]'
    printstr = ', '.join(
       [
       str(self.__contents[(self.__front + i) % self.__capacity]) 
       for i in range(self.__size)
       ]
    )
    return f"[ {printstr} ]"   

  def __len__(self):
    # TODO replace pass with an implementation that returns the number of
    # items in the deque. This method must run in constant time.
    # This method should return in constant time. The size of the array is stored in the constructor
    # and is updated when the array is grown or shrunk. Therefore, the size of the array can be returned
    # in constant time.
    return self.__size
  def __grow(self):
    # TODO replace pass with an implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (why is
    # necessary?)
    # This method should run in linear time. The size of the new array should be a constant 2 times
    # as large as the original. Copying it over is proportional to how large existing array is. 
    # Therefore, the time complexity is linear. 
    # The new array starts at zero because the array is circular. It needs to wrap around 
    # at the end of the array, so when copying it over it can't already wrap around halfway through. 
    new_capacity = self.__capacity * 2
    new_contents = [None] * new_capacity
    for i in range(self.__size):
            new_contents[i] = self.__contents[(self.__front + i) % self.__capacity]
    self.__contents = new_contents
    self.__front = 0
    self.__capacity = new_capacity
    

    
  def push_front(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    # This operation runs in constant time, unless the array needs to be grown. Array lookups are a constant time operation as they are stored 
    # in sequence in memory. The only time this operation would run in linear time is if the array needs to be grown, where the copying
    # over of the old array and creation of new ones run in linear time. 

    if self.__size == self.__capacity:
        self.__grow()
    self.__front = (self.__front - 1) % self.__capacity # Decrement the front of the array by 1, wrapping around if necessary
    self.__contents[self.__front] = val
    self.__size += 1
    
  def pop_front(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    # This operation runs in constant time. We know the location of the front of the array as well as the size of the array. 
    # Modular arithmetic is a constant time operation as well as array lookups. The rest of the function is updating constants, which is also
    # a constant time operation.
    if self.__size == 0:
        return None 
    val = self.__contents[self.__front] 
    self.__front = (self.__front + 1) % self.__capacity # Increment the front of the array by 1, wrapping around if necessary
    self.__size -= 1
    return val
    
  def peek_front(self):
    # TODO replace pass with your implementation.
    # This operation runs in constant time for the same reason as pop_front does. It is essentially the same as pop_front
    # except it doesn't delete the value in question, only returning it. Array lookups are a constant time operation, and we know the index. 
    if self.__size == 0:
        return None
    return self.__contents[self.__front]
    
  def push_back(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    # This operation runs in constant time, unless the array needs to be grown. 
    # Array lookups are a constant time operation as they are stored in sequence in memory, and 
    # the only time this operation would run in linear time is if the array needs to be grown, where the copying
    # over of the old array and creation of new ones run in linear time.

    if self.__size == self.__capacity:
        self.__grow()
    self.__contents[(self.__front + self.__size) % self.__capacity] = val # Uses front and size to find the index of the back of the array
    self.__size += 1
    
   
  
  def pop_back(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    # This operation runs in constant time. We know the location of the front of the array as well as the size of the array.
    # We can easily find the index of the array with front + size - 1, array lookups are O(1), and the rest of the function is updating
    # constants, which is also a constant time operation. 
    if self.__size == 0:
        return None
    val = self.__contents[(self.__front + self.__size - 1) % self.__capacity]  # Decrement the size of the array by 1, wrapping around if necessary
    self.__size -= 1
    return val

  def peek_back(self):
    # TODO replace pass with your implementation.
    # This operation runs in constant time for the same reason as pop_back is. 
    # It is essentially the same as pop_back except it doesn't delete the value in question, only returning it.
    # Array lookups are a constant time operation. 
    if self.__size == 0:
        return None
    return self.__contents[(self.__front + self.__size - 1) % self.__capacity] 

  

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':

