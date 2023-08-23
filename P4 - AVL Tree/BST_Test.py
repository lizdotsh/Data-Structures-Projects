import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BST_Test(unittest.TestCase):
  
  def setUp(self):
    self.__bst = Binary_Search_Tree()
  
  def test_bst_value_error(self):
    # ValueError When Already Inserted 
    self.__bst.insert_element(4)
    self.assertRaises(ValueError, self.__bst.insert_element, 4)
    self.__bst.insert_element(3)
    self.assertRaises(ValueError, self.__bst.insert_element, 3)
  def test_bst_check_heights(self):
    # Check Heights
    # Insert and remove
    self.__bst.insert_element(4)
    self.assertEqual(self.__bst.get_height(), 1)
    self.__bst.insert_element(3)
    self.assertEqual(self.__bst.get_height(), 2)
    self.__bst.remove_element(3)
    self.assertEqual(self.__bst.get_height(), 1)
    self.__bst.insert_element(8)
    self.assertEqual(self.__bst.get_height(), 2)
    self.__bst.insert_element(2)
    self.assertEqual(self.__bst.get_height(), 2)
    self.__bst.insert_element(5)
    self.assertEqual(self.__bst.get_height(), 3)
    self.__bst.remove_element(8)
    self.assertEqual(self.__bst.get_height(), 2)

  def test_bst_no_insert(self):
    # Single Insert
    # Check every method before 
    self.assertEqual(self.__bst.get_height(), 0)
    self.assertEqual(str(self.__bst), "[ ]")
    # Traversals
    self.assertEqual(self.__bst.pre_order(), "[ ]")
    self.assertEqual(self.__bst.in_order(), "[ ]")
    self.assertEqual(self.__bst.post_order(), "[ ]")
    self.assertEqual(self.__bst.to_list(), [])

  def test_bst_single_insert(self):
    # Insert
    self.__bst.insert_element(4)
    self.assertEqual(self.__bst.get_height(), 1)
    self.assertEqual(str(self.__bst), "[ 4 ]")
    # Traversals
    self.assertEqual(self.__bst.pre_order(), "[ 4 ]")
    self.assertEqual(self.__bst.in_order(), "[ 4 ]")
    self.assertEqual(self.__bst.post_order(), "[ 4 ]")
    self.assertEqual(self.__bst.to_list(), [4])

  def test_bst_single_insert_remove(self):
    # Insert and remove
    self.__bst.insert_element(4)
    self.__bst.remove_element(4)
    self.assertEqual(self.__bst.get_height(), 0)
    self.assertEqual(str(self.__bst), "[ ]")
    # Traversals
    self.assertEqual(self.__bst.pre_order(), "[ ]")
    self.assertEqual(self.__bst.in_order(), "[ ]")
    self.assertEqual(self.__bst.post_order(), "[ ]")
    self.assertEqual(self.__bst.to_list(), [])

  def test_bst_double_insert(self):
    # Insert
    self.__bst.insert_element(4)
    self.__bst.insert_element(3)
    self.assertEqual(self.__bst.get_height(), 2)
    self.assertEqual(str(self.__bst), "[ 3, 4 ]")
    # Traversals
    self.assertEqual(self.__bst.pre_order(), "[ 4, 3 ]")
    self.assertEqual(self.__bst.in_order(), "[ 3, 4 ]")
    self.assertEqual(self.__bst.post_order(), "[ 3, 4 ]")
    self.assertEqual(self.__bst.to_list(), [3, 4])
 
  def test_bst_double_insert_remove_second(self):
    # Insert and remove
    self.__bst.insert_element(4)
    self.__bst.insert_element(3)
    self.__bst.remove_element(3)
    self.assertEqual(self.__bst.get_height(), 1)
    self.assertEqual(str(self.__bst), "[ 4 ]")
    # Traversals
    self.assertEqual(self.__bst.pre_order(), "[ 4 ]")
    self.assertEqual(self.__bst.in_order(), "[ 4 ]")
    self.assertEqual(self.__bst.post_order(), "[ 4 ]")
    self.assertEqual(self.__bst.to_list(), [4])
  def test_bst_double_insert_remove_first(self):
    # Insert and remove
    self.__bst.insert_element(4)
    self.__bst.insert_element(3)
    self.__bst.remove_element(4)
    self.assertEqual(self.__bst.get_height(), 1)
    self.assertEqual(str(self.__bst), "[ 3 ]")
    # Traversals
    self.assertEqual(self.__bst.pre_order(), "[ 3 ]")
    self.assertEqual(self.__bst.in_order(), "[ 3 ]")
    self.assertEqual(self.__bst.post_order(), "[ 3 ]")
    self.assertEqual(self.__bst.to_list(), [3])

  def test_bst_triple_insert(self):
    # Insert
    self.__bst.insert_element(4)
    self.__bst.insert_element(3)
    self.__bst.insert_element(8)
    self.assertEqual(self.__bst.get_height(), 2)
    self.assertEqual(str(self.__bst), "[ 3, 4, 8 ]")
    # Traversals
    self.assertEqual(self.__bst.pre_order(), "[ 4, 3, 8 ]")
    self.assertEqual(self.__bst.in_order(), "[ 3, 4, 8 ]")
    self.assertEqual(self.__bst.post_order(), "[ 3, 8, 4 ]")
    self.assertEqual(self.__bst.to_list(), [3, 4, 8])
  def test_bst_triple_insert_inc_order(self):
    # Insert
    self.__bst.insert_element(4)
    self.__bst.insert_element(5)
    self.__bst.insert_element(6)
    self.assertEqual(self.__bst.get_height(), 2)  
    self.assertEqual(str(self.__bst), "[ 4, 5, 6 ]")
    # Traversals
    self.assertEqual(self.__bst.pre_order(), "[ 5, 4, 6 ]")
    self.assertEqual(self.__bst.in_order(), "[ 4, 5, 6 ]")
    self.assertEqual(self.__bst.post_order(), "[ 4, 6, 5 ]")
    self.assertEqual(self.__bst.to_list(), [4, 5, 6])
  def test_bst_triple_insert_dec_order(self):
    # Insert
    self.__bst.insert_element(6)
    self.__bst.insert_element(5)
    self.__bst.insert_element(4)
    self.assertEqual(self.__bst.get_height(), 2)  
    self.assertEqual(str(self.__bst), "[ 4, 5, 6 ]")
    # Traversals
    self.assertEqual(self.__bst.pre_order(), "[ 5, 4, 6 ]")
    self.assertEqual(self.__bst.in_order(), "[ 4, 5, 6 ]")
    self.assertEqual(self.__bst.post_order(), "[ 4, 6, 5 ]")
    self.assertEqual(self.__bst.to_list(), [4, 5, 6])

  def test_bst_five_variation_one(self):
    # Test representations and traversals of [50, 30, 70, 20, 10]
    for i in [50, 30, 70, 20, 10]:
        self.__bst.insert_element(i)
    self.assertEqual(self.__bst.get_height(), 3)
    self.assertEqual(str(self.__bst), "[ 10, 20, 30, 50, 70 ]")
    # Traversals
    self.assertEqual(self.__bst.pre_order(), "[ 50, 20, 10, 30, 70 ]")
    self.assertEqual(self.__bst.in_order(), "[ 10, 20, 30, 50, 70 ]")
    self.assertEqual(self.__bst.post_order(), "[ 10, 30, 20, 70, 50 ]")
    self.assertEqual(self.__bst.to_list(), [10, 20, 30, 50, 70])
  def test_bst_five_variation_two(self):
    # Test representations and traversals of [50, 30, 70, 90, 80]
    for i in [50, 30, 70, 90, 80]:
        self.__bst.insert_element(i)
    self.assertEqual(self.__bst.get_height(), 3)
    self.assertEqual(str(self.__bst), "[ 30, 50, 70, 80, 90 ]")
    # Traversals
    self.assertEqual(self.__bst.pre_order(), "[ 50, 30, 80, 70, 90 ]")
    self.assertEqual(self.__bst.in_order(), "[ 30, 50, 70, 80, 90 ]")
    self.assertEqual(self.__bst.post_order(), "[ 30, 70, 90, 80, 50 ]")
    self.assertEqual(self.__bst.to_list(), [30, 50, 70, 80, 90])

  def test_bst_six_variation_one(self):
    # Test representations and traversals of [50, 30, 70, 60, 80, 90]
    for i in [50, 30, 70, 60, 80, 90]:
        self.__bst.insert_element(i)
    self.assertEqual(self.__bst.get_height(), 3)
    self.assertEqual(str(self.__bst), "[ 30, 50, 60, 70, 80, 90 ]")
    # Traversals
    self.assertEqual(self.__bst.pre_order(), "[ 70, 50, 30, 60, 80, 90 ]")
    self.assertEqual(self.__bst.in_order(), "[ 30, 50, 60, 70, 80, 90 ]")
    self.assertEqual(self.__bst.post_order(), "[ 30, 60, 50, 90, 80, 70 ]")
    self.assertEqual(self.__bst.to_list(), [30, 50, 60, 70, 80, 90])
  def test_bst_six_var_2_insert(self):
    # Test representations and traversals of [60, 50, 70, 30, 65, 80]
    for i in [60, 50, 70, 30, 65, 80]:
        self.__bst.insert_element(i)
    self.assertEqual(self.__bst.get_height(), 3)
    self.assertEqual(str(self.__bst), "[ 30, 50, 60, 65, 70, 80 ]")
    # Traversals
    self.assertEqual(self.__bst.pre_order(), "[ 60, 50, 30, 70, 65, 80 ]")
    self.assertEqual(self.__bst.in_order(), "[ 30, 50, 60, 65, 70, 80 ]")
    self.assertEqual(self.__bst.post_order(), "[ 30, 50, 65, 80, 70, 60 ]")
    self.assertEqual(self.__bst.to_list(), [30, 50, 60, 65, 70, 80])
  def test_bst_six_var_2_remove_one(self):
    # Test representations and traversals of [60, 50, 70, 30, 65, 80]
    for i in [60, 50, 70, 30, 65, 80]:
        self.__bst.insert_element(i)
    self.__bst.remove_element(80)
    self.assertEqual(self.__bst.get_height(), 3)
    self.assertEqual(str(self.__bst), "[ 30, 50, 60, 65, 70 ]")
    # Traversals
    self.assertEqual(self.__bst.pre_order(), "[ 60, 50, 30, 70, 65 ]")
    self.assertEqual(self.__bst.in_order(), "[ 30, 50, 60, 65, 70 ]")
    self.assertEqual(self.__bst.post_order(), "[ 30, 50, 65, 70, 60 ]")
    self.assertEqual(self.__bst.to_list(), [30, 50, 60, 65, 70])
  def test_bst_six_var_2_remove_3_dec(self):
    # remove 80,50,30
    for i in [60, 50, 70, 30, 65, 80]:
        self.__bst.insert_element(i)
    self.__bst.remove_element(80)
    self.__bst.remove_element(50)
    self.__bst.remove_element(30)
    self.assertEqual(self.__bst.get_height(), 2)
    self.assertEqual(str(self.__bst), "[ 60, 65, 70 ]")
    # Traversals
    self.assertEqual(self.__bst.pre_order(), "[ 65, 60, 70 ]")
    self.assertEqual(self.__bst.in_order(), "[ 60, 65, 70 ]")
    self.assertEqual(self.__bst.post_order(), "[ 60, 70, 65 ]")
    self.assertEqual(self.__bst.to_list(), [60, 65, 70])
  def test_bst_six_var_2_point_5_remove_3_inc(self):
    # remove 30, 70, 80
    for i in [60, 50, 70, 30, 55, 80]:
        self.__bst.insert_element(i)
    self.__bst.remove_element(30)
    self.__bst.remove_element(70)
    self.__bst.remove_element(80)
    self.assertEqual(self.__bst.get_height(), 2)
    self.assertEqual(str(self.__bst), "[ 50, 55, 60 ]")
    # Traversals
    self.assertEqual(self.__bst.pre_order(), "[ 55, 50, 60 ]")
    self.assertEqual(self.__bst.in_order(), "[ 50, 55, 60 ]")
    self.assertEqual(self.__bst.post_order(), "[ 50, 60, 55 ]")
    self.assertEqual(self.__bst.to_list(), [50, 55, 60])
  def test_bst_six_var_2_remove_3_mix(self):
    # remove 65, 50, 30
    for i in [60, 50, 70, 30, 65, 80]:
        self.__bst.insert_element(i)
    self.__bst.remove_element(65)
    self.__bst.remove_element(50)
    self.__bst.remove_element(30)
    self.assertEqual(self.__bst.get_height(), 2)
    self.assertEqual(str(self.__bst), "[ 60, 70, 80 ]")
    # Traversals
    self.assertEqual(self.__bst.pre_order(), "[ 70, 60, 80 ]")
    self.assertEqual(self.__bst.in_order(), "[ 60, 70, 80 ]")
    self.assertEqual(self.__bst.post_order(), "[ 60, 80, 70 ]")
    self.assertEqual(self.__bst.to_list(), [60, 70, 80])

  def test_bst_remove_element(self):
    # Remove Element
    self.__bst.insert_element(4)
    self.__bst.insert_element(3)
    self.__bst.insert_element(8)
    self.__bst.insert_element(2)
    self.__bst.insert_element(5)
    self.__bst.insert_element(7)
    self.__bst.remove_element(8)
    self.assertEqual(self.__bst.get_height(), 3)
    self.__bst.remove_element(3)
    self.assertEqual(self.__bst.get_height(), 3)
    self.__bst.remove_element(4)
    self.assertEqual(self.__bst.get_height(), 2)
    self.__bst.remove_element(2)
    self.assertEqual(self.__bst.get_height(), 2)
    self.__bst.remove_element(5)
    self.assertEqual(self.__bst.get_height(), 1)
    self.__bst.remove_element(7)
    self.assertEqual(self.__bst.get_height(), 0)
  def test_empty_tree_height_zero(self):
    self.assertEqual(self.__bst.get_height(), 0)

  def test_bst_string_rep(self):
    # String Representation
    self.assertEqual(str(self.__bst), "[ ]")
    self.__bst.insert_element(4)
    self.assertEqual(str(self.__bst), "[ 4 ]")
    self.__bst.insert_element(3)
    self.assertEqual(str(self.__bst), "[ 3, 4 ]")
    self.__bst.insert_element(8)
    self.assertEqual(str(self.__bst), "[ 3, 4, 8 ]")
    self.__bst.insert_element(2)
    self.assertEqual(str(self.__bst), "[ 2, 3, 4, 8 ]")
    self.__bst.insert_element(5)
    self.assertEqual(str(self.__bst), "[ 2, 3, 4, 5, 8 ]")
    self.__bst.insert_element(7)
    self.assertEqual(str(self.__bst), "[ 2, 3, 4, 5, 7, 8 ]") 


  def test_bst_pre_order_long(self):
    # Pre Order
    # final: [ 25, 15, 10, 22, 50, 35, 70, 90 ]
    self.assertEqual(self.__bst.pre_order(), "[ ]")
    for i in [25, 15, 10, 22, 50, 35, 70, 90]:
      self.__bst.insert_element(i)
    self.assertEqual(self.__bst.pre_order(), "[ 25, 15, 10, 22, 50, 35, 70, 90 ]")

  def test_bst_in_order_long(self):
    # In Order
    # final: [ 10, 15, 22, 25, 35, 50, 70, 90 ]
    self.assertEqual(self.__bst.in_order(), "[ ]")
    for i in [25, 15, 10, 22, 50, 35, 70, 90]:
        self.__bst.insert_element(i)
    self.assertEqual(self.__bst.in_order(), "[ 10, 15, 22, 25, 35, 50, 70, 90 ]")
    
  def test_bst_post_order_long(self):
    # Post Order
    # final: [ 10, 22, 15, 35, 90, 70, 50, 25 ]
    self.assertEqual(self.__bst.post_order(), "[ ]")
    for i in [25, 15, 10, 22, 50, 35, 70, 90]:
        self.__bst.insert_element(i)
    self.assertEqual(self.__bst.post_order(), "[ 10, 22, 15, 35, 90, 70, 50, 25 ]")

  def test_bst_to_list(self):
    # final: [2, 3, 4, 5, 7, 8 ]
    self.assertEqual(self.__bst.to_list(), [])
    self.__bst.insert_element(4)
    self.assertEqual(self.__bst.to_list(), [4])
    self.__bst.insert_element(3)
    self.assertEqual(self.__bst.to_list(), [3, 4])
    self.__bst.insert_element(8)
    self.assertEqual(self.__bst.to_list(), [3, 4, 8])
    self.__bst.insert_element(2)
    self.assertEqual(self.__bst.to_list(), [2, 3, 4, 8])
    self.__bst.insert_element(5)
    self.assertEqual(self.__bst.to_list(), [2, 3, 4, 5, 8])
    self.__bst.insert_element(7)
    self.assertEqual(self.__bst.to_list(), [2, 3, 4, 5, 7, 8])

  def test_bst_to_list_long(self):
    # final: [10, 15, 22, 25, 35, 50, 70, 90 ]
    self.assertEqual(self.__bst.to_list(), [])
    for i in [25, 15, 10, 22, 50, 35, 70, 90]:
        self.__bst.insert_element(i)
    self.assertEqual(self.__bst.to_list(), [10, 15, 22, 25, 35, 50, 70, 90])

    

if __name__ == '__main__':
  unittest.main()

