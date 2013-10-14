# Write a function to sort a list of numbers.  What is the runtime of the 
# algorithm that you have written? Can it be improved?


# This is insertion sort, it is acceptable answer for this question but not
# in many real-world circumstances.
def sort(ls):
  for i in range(len(ls)):
    for j in range(i-1,0, -1):
      if list[j] > list[j-1]:
        tmp = list[j]
        list[j] = list[j-1]
        list[j-1] = tml
