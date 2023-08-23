import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()
  

  def test_deque_push_front(self):
    self.__deque.push_front(1)
    self.assertEqual(str(self.__deque), '[ 1 ]')
    self.__deque.push_front(2)
    self.assertEqual(str(self.__deque), '[ 2, 1 ]')
    self.__deque.push_front(3)
    self.assertEqual(str(self.__deque), '[ 3, 2, 1 ]')

  def test_deque_push_back(self):
    self.__deque.push_back(1)
    self.assertEqual(str(self.__deque), '[ 1 ]')
    self.__deque.push_back(2)
    self.assertEqual(str(self.__deque), '[ 1, 2 ]')
    self.__deque.push_back(3)
    self.assertEqual(str(self.__deque), '[ 1, 2, 3 ]')

  def test_deque_pop_front(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    self.assertEqual(self.__deque.pop_front(), 3)
    self.assertEqual(str(self.__deque), '[ 2, 1 ]')
    self.assertEqual(self.__deque.pop_front(), 2)
    self.assertEqual(str(self.__deque), '[ 1 ]')
    self.assertEqual(self.__deque.pop_front(), 1)
    self.assertEqual(str(self.__deque), '[ ]')

  def test_deque_pop_back(self):
    self.__deque.push_back(1)
    self.__deque.push_back(2)
    self.__deque.push_back(3)
    self.assertEqual(self.__deque.pop_back(), 3)
    self.assertEqual(str(self.__deque), '[ 1, 2 ]')
    self.assertEqual(self.__deque.pop_back(), 2)
    self.assertEqual(str(self.__deque), '[ 1 ]')
    self.assertEqual(self.__deque.pop_back(), 1)
    self.assertEqual(str(self.__deque), '[ ]')

  def test_deque_peek_front(self):
    self.__deque.push_front(1)
    self.assertEqual(self.__deque.peek_front(), 1)
    self.__deque.push_front(2)
    self.assertEqual(self.__deque.peek_front(), 2)
    self.__deque.push_front(3)
    self.assertEqual(self.__deque.peek_front(), 3)

  def test_deque_peek_back(self):
    self.__deque.push_back(1)
    self.assertEqual(self.__deque.peek_back(), 1)
    self.__deque.push_back(2)
    self.assertEqual(self.__deque.peek_back(), 2)
    self.__deque.push_back(3)
    self.assertEqual(self.__deque.peek_back(), 3)

  def test_deque_len(self):
    self.assertEqual(len(self.__deque), 0)
    self.__deque.push_front(1)
    self.assertEqual(len(self.__deque), 1)
    self.__deque.push_back(2)
    self.assertEqual(len(self.__deque), 2)
    self.__deque.pop_front()
    self.assertEqual(len(self.__deque), 1)
    self.__deque.pop_back()
    self.assertEqual(len(self.__deque), 0)

  def test_deque_empty_pop_front_is_none(self):
    self.assertEqual(self.__deque.pop_front(), None)

  def test_deque_empty_pop_back_is_none(self):
    self.assertEqual(self.__deque.pop_back(), None)

  def test_deque_empty_peek_front_is_none(self):
    self.assertEqual(self.__deque.peek_front(), None)

  def test_deque_empty_peek_back_is_none(self):
    self.assertEqual(self.__deque.peek_back(), None)
  def test_deque_string_empty(self):
    self.assertEqual(str(self.__deque), '[ ]')

  # Testing String Representations of empty pops/peeks:
  def test_deque_string_empty_pop_front(self):
    self.__deque.pop_front()
    self.assertEqual(str(self.__deque), '[ ]')
  def test_deque_string_empty_pop_back(self):
    self.__deque.pop_back()
    self.assertEqual(str(self.__deque), '[ ]')
  def test_deque_string_empty_peek_front(self):
    self.__deque.peek_front()
    self.assertEqual(str(self.__deque), '[ ]')
  def test_deque_string_empty_peek_back(self):
    self.__deque.peek_back()
    self.assertEqual(str(self.__deque), '[ ]')
  
  # Testing Circular Behavior:
  def test_deque_circular_behavior_push_front(self):
    self.__deque.push_back(1)
    self.__deque.push_back(2)
    self.__deque.push_back(3)
    self.__deque.push_front(4)
    self.__deque.push_front(5)
    self.__deque.pop_back()
    self.__deque.pop_back()
    self.__deque.push_back(6)
    self.assertEqual(str(self.__deque), '[ 5, 4, 1, 6 ]')

  def test_deque_circular_behavior_push_back(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    self.__deque.push_back(4)
    self.__deque.push_back(5)
    self.__deque.pop_front()
    self.__deque.pop_front()
    self.__deque.push_front(6)
    self.assertEqual(str(self.__deque), '[ 6, 1, 4, 5 ]')

  def test_deque_expansion(self):
    for i in range(1, 9):
        self.__deque.push_back(i)
    self.assertEqual(str(self.__deque), '[ 1, 2, 3, 4, 5, 6, 7, 8 ]')

    self.__deque.push_back(9)
    self.assertEqual(str(self.__deque), '[ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]')

    for i in range(1, 6):
        self.__deque.pop_front()

    self.assertEqual(str(self.__deque), '[ 6, 7, 8, 9 ]')

    for i in range(10, 14):
        self.__deque.push_back(i)

    self.assertEqual(str(self.__deque), '[ 6, 7, 8, 9, 10, 11, 12, 13 ]')
  def test_deque_pop_empty_returns_none(self):
    self.assertEqual(self.__deque.pop_front(), None)
    self.assertEqual(self.__deque.pop_back(), None)
        
  def test_deque_alternate_push_pop_front_back(self):
    self.__deque.push_front(1)
    self.__deque.push_back(2)
    self.__deque.push_front(3)
    self.__deque.push_back(4)
    self.assertEqual(str(self.__deque), '[ 3, 1, 2, 4 ]')

    self.__deque.pop_front()
    self.assertEqual(str(self.__deque), '[ 1, 2, 4 ]')

    self.__deque.pop_back()
    self.assertEqual(str(self.__deque), '[ 1, 2 ]')

    self.__deque.push_front(5)
    self.assertEqual(str(self.__deque), '[ 5, 1, 2 ]')

    self.__deque.push_back(6)
    self.assertEqual(str(self.__deque), '[ 5, 1, 2, 6 ]')

    self.__deque.pop_front()
    self.assertEqual(str(self.__deque), '[ 1, 2, 6 ]')

    self.__deque.pop_back()
    self.assertEqual(str(self.__deque), '[ 1, 2 ]')

 
  def test_deque_single_element_operations(self):
    self.__deque.push_front(1)
    self.assertEqual(str(self.__deque), '[ 1 ]')

    self.assertEqual(self.__deque.peek_front(), 1)
    self.assertEqual(self.__deque.peek_back(), 1)

    self.__deque.pop_front()
    self.assertEqual(str(self.__deque), '[ ]')

    self.__deque.push_back(2)
    self.assertEqual(str(self.__deque), '[ 2 ]')

    self.assertEqual(self.__deque.peek_front(), 2)
    self.assertEqual(self.__deque.peek_back(), 2)

    self.__deque.pop_back()
    self.assertEqual(str(self.__deque), '[ ]')

  def test_deque_grow_shrink_cycle(self):
    for i in range(1, 17):
      self.__deque.push_back(i)
    self.assertEqual(len(self.__deque), 16)

    for i in range(1, 9):
      self.__deque.pop_front()
    self.assertEqual(len(self.__deque), 8)

    for i in range(9, 25):
      self.__deque.push_back(i)
    self.assertEqual(len(self.__deque), 24)

    for i in range(8):
      self.__deque.pop_front()
    self.assertEqual(len(self.__deque), 16)
  # TODO add your test methods here. Like Linked_List_Test.py,
  # each test should me in a method whose name begins with test_

  # Queue Tests:

  def test_queue_empty(self):
    self.assertEqual(len(self.__queue), 0)
    self.assertIsNone(self.__queue.peek())
    self.assertIsNone(self.__queue.dequeue())
    self.assertEqual(str(self.__queue), '[ ]')
    


  def test_queue_one(self):
    self.__queue.enqueue(1)
    self.assertEqual(len(self.__queue), 1)
    self.assertEqual(self.__queue.peek(), 1)
    self.assertEqual(str(self.__queue), '[ 1 ]')


  def test_queue_two(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.assertEqual(len(self.__queue), 2)
    self.assertEqual(self.__queue.peek(), 1)
    self.assertEqual(str(self.__queue), '[ 1, 2 ]')

  def test_queue_three(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.enqueue(3)
    self.assertEqual(len(self.__queue), 3)
    self.assertEqual(self.__queue.peek(), 1)
    self.assertEqual(str(self.__queue), '[ 1, 2, 3 ]')

  def test_queue_enqueue(self):
    self.__queue.enqueue(1)
    self.assertEqual(len(self.__queue), 1)
    self.assertEqual(self.__queue.peek(), 1)

    self.__queue.enqueue(2)
    self.assertEqual(len(self.__queue), 2)
    self.assertEqual(self.__queue.peek(), 1)

  def test_queue_dequeue(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.enqueue(3)

    val = self.__queue.dequeue()
    self.assertEqual(val, 1)
    self.assertEqual(len(self.__queue), 2)
    self.assertEqual(self.__queue.peek(), 2)

    val = self.__queue.dequeue()
    self.assertEqual(val, 2)
    self.assertEqual(len(self.__queue), 1)
    self.assertEqual(self.__queue.peek(), 3)

  def test_queue_length(self):
    self.assertEqual(len(self.__queue), 0)

    self.__queue.enqueue(1)
    self.assertEqual(len(self.__queue), 1)

    self.__queue.enqueue(2)
    self.assertEqual(len(self.__queue), 2)

    self.__queue.dequeue()
    self.assertEqual(len(self.__queue), 1)

    self.__queue.dequeue()
    self.assertEqual(len(self.__queue), 0)

  def test_queue_complex_scenario(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.enqueue(3)
    self.__queue.enqueue(4)
    self.__queue.dequeue()
    self.__queue.enqueue(5)
    self.__queue.dequeue()
    self.__queue.enqueue(6)
    self.__queue.enqueue(7)
    self.__queue.dequeue()

    self.assertEqual(len(self.__queue), 4)
    self.assertEqual(str(self.__queue), '[ 4, 5, 6, 7 ]')
  
  def test_queue_dequeue_returns_when_called(self):
    self.__queue.enqueue(1)
    self.assertEqual(self.__queue.dequeue(), 1)
    self.assertEqual(len(self.__queue), 0)

  # Stack Tests:
  
  def test_stack_empty(self):
    self.assertEqual(len(self.__stack), 0)
    self.assertIsNone(self.__stack.peek())
    self.assertIsNone(self.__stack.pop())
    self.assertEqual(str(self.__stack), '[ ]')

  
  def test_stack_one(self):
    self.__stack.push(1)
    self.assertEqual(len(self.__stack), 1)
    self.assertEqual(self.__stack.peek(), 1)
    self.assertEqual(self.__stack.pop(), 1)
    self.assertEqual(len(self.__stack), 0)
    self.assertEqual(str(self.__stack), '[ ]')
  
  def test_stack_two(self):
    self.__stack.push(1)
    self.__stack.push(2)
    self.assertEqual(len(self.__stack), 2)
    self.assertEqual(str(self.__stack), '[ 2, 1 ]')
    self.assertEqual(self.__stack.peek(), 2)
    self.assertEqual(self.__stack.pop(), 2)
    self.assertEqual(len(self.__stack), 1)
    self.assertEqual(str(self.__stack), '[ 1 ]')
    
  def test_stack_three(self):
    self.__stack.push(1)
    self.__stack.push(2)
    self.__stack.push(3)
    self.assertEqual(len(self.__stack), 3)
    self.assertEqual(str(self.__stack), '[ 3, 2, 1 ]')
    self.assertEqual(self.__stack.peek(), 3)
    self.assertEqual(self.__stack.pop(), 3)
    self.assertEqual(len(self.__stack), 2)
    self.assertEqual(str(self.__stack), '[ 2, 1 ]')






if __name__ == '__main__':
  unittest.main()

