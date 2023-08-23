from Deque import Deque
from Linked_List import Linked_List

class Linked_List_Deque(Deque):

  def __init__(self):
    self.__list = Linked_List()

  def __str__(self):
    return str(self.__list)

  def __len__(self):
    return len(self.__list)
  
  # DO NOT CHANGE ANYTHING ABOVE THIS LINE
  
  def push_front(self, val):
    # TODO replace pass with your implementation.
    # Use the head position for the front.
    # I used a combination of the linked list insert and append methods. 
    # If the list is empty, append the value. This is because insert_element_at
    # will throw an error if the list is empty. Appending is a constant time operation and the trailer is known. 
    # If the list is not empty, insert the value at the head position using insert_element_at.
    # This method appears to be O(n) because it has to traverse the list to find the head position, but in reality
    # it is O(1) because the head position is a constant distance from the header. So it only has to initialize the loop 
    # once no matter how long the list is.
    if len(self) == 0:
        self.__list.append_element(val)
    else:
        self.__list.insert_element_at(val, 0)

  
  def pop_front(self):
    # TODO replace pass with your implementation.
    # Use the head position for the front.
    # This method uses remove_element_at, which is already very similar to a pop method. 
    # If the list is empty I return none. Otherwise I remove the element at the head position.
    # This method is O(1), as we known the header position and only have to walk back once no matter how long the list is.
    if len(self) == 0:
        return None
    return self.__list.remove_element_at(0)


  def peek_front(self):
    # TODO replace pass with your implementation.
    # Use the head position for the front.
    # This method uses get_element_at, at a fixed index of zero like the other methods. 
    # If the list is empty I return none. Otherwise I return the element at the head position
    # This method is O(1), as we known the header position and only have to walk back once no matter how long the list is.

    if len(self) == 0:
        return None
    return self.__list.get_element_at(0)

  def push_back(self, val):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.
    # This element uses append_element, which is a constant time operation as we know the trailer position.
    # Nothing else needs to be done as this is a direct implementation of the append method.
    self.__list.append_element(val)
    
  
  def pop_back(self):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.
    # This method uses remove_element_at, but at the end of the list.
    # If the list is empty I return none. Otherwise I remove the element at the tail position.
    # This method is complicated because it has to pass a check of dividing n by 2 to decide which way to walk the list.
    # But once that happens (a constant time operation), it only has to walk back one point from the trailer.
    if len(self) == 0:
        return None
    return self.__list.remove_element_at(len(self) - 1) # Decrement by one because the list is zero indexed.

  def peek_back(self):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.
    # All methods that wallk the list use the same private __get_node_at method, which divide by 2 to decide which way to walk the list.
    # But once that happens (a constant time operation), it only has to walk back one point from the trailer in this case. 
    # So this method is O(1) as well.
    if len(self) == 0:
        return None
    return self.__list.get_element_at(len(self) - 1)

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
