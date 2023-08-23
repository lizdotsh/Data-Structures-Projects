from Deque_Generator import get_deque

class Stack:

  def __init__(self):
    self.__dq = get_deque()

  def __str__(self):
    # TODO replace pass with your implementation.
    # Orient your string from top (left) to bottom (right).
    # Both of the deque implementations you will use will have a __str__ method, this just needs to export that method.
    return str(self.__dq)

  def __len__(self):
    # TODO replace pass with your implementation.
    # Both of the deque implementations you will use will have a __len__ method, this just needs to export that method.
    return len(self.__dq)

  def push(self, val):
    # TODO replace pass with your implementation.
    # Stacks are basically one sided deques, so I just use the front of the deque.
    # requiring an extra length check as it has to go from the footer instead of the header.
    # Also string methods will already be in order, so I don't need to reverse them.
    self.__dq.push_front(val)

  def pop(self):
    # TODO replace pass with your implementation.
    # Similar reasoning as before, I just use the front of the deque.
    # Removing at element 0 is very simple. So I don't need to reverse the string.
    return self.__dq.pop_front()

  def peek(self):
    # TODO replace pass with your implementation.
    # Same reasoning as before. All of these methods are O(1) either way.
    return self.__dq.peek_front()
  

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
