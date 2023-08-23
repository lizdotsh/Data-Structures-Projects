import timeit
from Stack import Stack

def Hanoi_rec(n, s, a, d):
  # This algorithm should be O(2^n). This is because 
  # For each time we call the function, we call it twice more (aside from the base case). 
  # And each time we call it, we decrement n by one. The end result of this is that 
  # as n gets larger, the number of times we call the function grows exponentially. 
  # This is frankly quite bad. It might be technically O(2^{n-1}), but that's not much better.
  print(n, s, a, d)
  if n == 0:
    d.push(s.pop())
  else: 
    Hanoi_rec(n-1, s, d, a)
    d.push(s.pop())
    Hanoi_rec(n-1, a, s, d)
  print(n, s, a, d)
  print()

def Hanoi(n):
  source = Stack()
  dest = Stack()
  aux = Stack()
  i = n-1
  while i >= 0:
    source.push(i)
    i = i - 1
  Hanoi_rec(n-1, source, aux, dest)

if __name__ == "__main__":
  n=3
  runtime = timeit.timeit("Hanoi(n)", setup="from __main__ import Hanoi,n", number=1)
  print("computed Hanoi(" + str(n) + ") in " + str(runtime) + " seconds.")

