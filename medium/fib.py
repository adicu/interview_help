# Write a function that finds the nth Fibonacci number.  The Fibonacci numbers 
# are a sequence of numbers where each number is the sum of the previous two 
# numbers: 1,1,2,3,5,8,13..

def fib(n):
  current =1
  previous = 1
  for i in range(n-2):
    updated_previous = current
    current = previous + current
    previous = updated_previous
  return current
