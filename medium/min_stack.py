# Implement a data structure that supports the native operations of stack, 
# push and pop, but also allow you to find the minimum in O(1) time.

# Solution is to under the hood maintain 2 stacks, one is the actual stack, and
# the other keeps the current minimum, and when the current minimum is popped
# off the stack, pop it off the stack
