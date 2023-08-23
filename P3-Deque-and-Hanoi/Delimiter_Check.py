import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
  # TODO replace pass with an implementation that returns True
  # if the delimiters (), [], and {} are balanced and False otherwise.
  # This function is a little more complicated than it probably needs to be, but I think it is pretty clear. 
  # First off, I create a dictionary that maps the opening delimiters to their closing counterparts. This just makes things a lot easier later. 
  # Then I create a stack and open the file. I concatenate the entire file into a single string, and then iterate through it character by character.
  # If the character is an opening delimiter, I push it onto the stack. If it is a closing delimiter, 
  # I pop the top of the stack and check if it is the correct delimiter. I use the dictionary from earlier to map opening delimiters to closing delimiters.
  # This makes sure that there are not only the correct number of delimiters, but that they are in the correct order, without any other 
  # incomplete delimiters in between. If the top of the stack is not the correct delimiter, I return False.
  # If the stack is empty at the end, I return True. 
  # The performance of this algorithm is O(n), where n is the number of characters in the file.
  # The push and pop operations are O(1), so each loop iteration is O(1).
  # This O(1) is looped over n times, so the total is O(n).
  conversion = {'(':')', '[':']', '{':'}'}
  stack = Stack()
  with open(filename) as f:
    full_string = "".join(f) # Concatenate the entire file into a single string.
  for char in full_string:
    if char in ['(', '[', '{']:
      stack.push(char)
    elif char in [')', ']', '}']:
      top_token = conversion[stack.pop()] # Get the top of the stack and map it to its closing delimiter.
      if top_token != char:
          return False
  if len(stack) == 0:
    return True
if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']

  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


