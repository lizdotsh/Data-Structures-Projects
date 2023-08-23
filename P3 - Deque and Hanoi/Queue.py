from Deque_Generator import get_deque

class Queue:

  def __init__(self):
    self.__dq = get_deque()

  def __str__(self):
    # TODO replace pass with your implementation.
    # Orient your string from front (left) to back (right).
    # Both of the deque implementations you will use will have a __str__ method, this just needs to export that method.
    return str(self.__dq)

  def __len__(self):
    # TODO replace pass with your implementation.
    # Both of the deque implementations you will use will have a __len__ method, this just needs to export that method.
    return len(self.__dq)

  def enqueue(self, val):
    # TODO replace pass with your implementation.
    # Enqueue is effectively the same operation as putting an element at the end of the list. In linked list terms, 
    # this means appending to the end of the list. In array terms, this means putting the element at the end of the
    # array. In both cases, the element is added to the back of the queue. I could use the beginning of the deque, 
    # but that is minorly more complicated (requiring a length check and an insert element that initializes a loop that runs once etc), so 
    # I just use the end of the deque.
    self.__dq.push_back(val)

  def dequeue(self):
    # TODO replace pass with your implementation.
    # Dequeue is effectively the same operation as popping an element from the beginning of the deque. 
    # For arrays, this is only a bit more math as I don't store the back portion, only the beginning and the size. Still O(1) either way though. 
    # For linked lists, this doesn't really make a huge difference but it is easier to append to the end of the list and pop from the beginning.
    return self.__dq.pop_front()

  def peek(self):
    # TODO replace pass with your implementation.
    # I was already using the end of the deque for enqueue, so I just use the front of the deque for peek.
    # Either way it is the same time complexity.
    return self.__dq.peek_front()

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
  
