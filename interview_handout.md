## ADI Interview Workshop Questions

### Couple high-level questions

1.) Describe in as much detail as possible what happens when a person requests
a web page.

2.) Describe how you would design Google Docs from scratch

### Easy

 1.) Add up the elements in an array:

 2.) Given the radius of a circle, calculate the area.

 3.) Find the Euclidean distance between two coordinate points.

 4.) Find the Euclidean distance between 2 points in n dimensions.

 5.) Add up the elements in an array:

 6.) Write FizzBuzz.  This is a function that prints out the numbers 1 to 100, 
 and whenever a multiple of 3 is reached, print "fizz", when a multiple of 5 is 
 reached, print "buzz", and whenever a number that is a multiple of both is
 reached print "fizzbuzz".

 7.) Given two strings, check whether the first string is a substring of the
 second string.  What is the runtime of your algorithm?

 8.)  Write a function to reverse a string

### Medium

 1.) Given a two-dimensional array in which each row and each column is sorted,
 detect if a given element is in the array*

 2.) Write a method that sorts a list of strings such that all anagrams are
 adjacent in the list

 3.) Given an integer, return as a string the binary representation of the integer.

 4.) Given a binary search tree, print out the elements in level order.
 for example, for the tree
       8
      /\
     6  9
    /\   \
    5 7  11

  It will print 8 6 9 5 7 11


 5.) Given a binary search tree, print out the elements in sorted order.


 6.) Determine if two strings are a cipher match.  Two strings are a cipher match
 if they have the same ordering of characters, even if the characters themselves
 are not the same.  For example, "aabb" and "ccdd" are a cipher match, as are
 "abccd" and "efggh"

 7.) In an array containing integers, one element is duplicated.  Find this element.

 8.) Write a function that finds the nth Fibonacci number.  The Fibonacci numbers
 are a sequence of numbers where each number is the sum of the previous two
 numbers: 1,1,2,3,5,8,13..

 9.) Write a function that gives the number of possible ways one can combine
 quarters, dimes, and nickels to form n cents (0 is a possibility).

 10.) Write a function that given a string detects whether all parentheses are
 matched

 11.) Implement a data structure that supports the native operations of stack,
 push and pop, but also allow you to find the minimum in O(1) time.

 12.) Given a list, return all permutations of the list*

 13.) Given a list of numbers, return the powerset of this list. The powerset
 is the set of all subsets of the list.
 For example, the power set of [1,2,3] is
 [[],[1],[2],[3], [1,2], [2,3], [1,3], [1,2,3]]

 14.) Given a list of strings, print out every string and its reverse if the reverse
 of the string is also in the list.

 15.) What is the second largest element in a binary search tree?

 16.) Write a function to sort a list of numbers.  What is the runtime of the
 algorithm that you have written? Can it be improved?

 17.) Given a list of numbers and a target number, find the number of ways the
 numbers in the list can add to the target number. Each number in the list can
 be reused. For example, if the list is [4,8,2,6] and the target number is 12,
 it can be formed with
 [2,6,4],[8,4],[6,6], [2,2,2,2,2,2], [8,2,2], [6,2,2,2], [4,4,4], [4,2,2,2,2]
  and the program should return 8.

  18.) Find the maximum continuous subsequence of a list, and return its sum.
  This is the continous subsequence (adjacent elements) that has the largest sum.
  For example, for [7,-8,4,-1,5,-3,-2,6,1], the maximum continuous subsequence is
[4,-1,5,-3,-2,6,1], which adds to 10.

### Hard

 1.) Write a Brainf*ck interpreter.  An interpreter is a program that accepts
 another program as input and executes it.  Brainf*ck is a language consisting 
 of characters "><+-[ ].,", where the program itself represents a large array 
 of data.  The command
 ">" moves a data pointer, which points at a given element, to the element on
 the right, the command "<" moves the data pointer to the element on the left,
 "+" increments the value of the element that the data pointer is pointed it,
 and "-" decrements it.  "," takes raw input and puts it in the element that the
 data pointer is it, and "." outputs the value of the current element. The "]"
 cell that the data pointer is pointed is 0, then move the corresponding "[" character.

 2.) Find the longest common substring between two strings.  ie. for "abcde" and
 "acccde" the longest common substring is "acde".

 3.) Write a maze-solver: Given a matrix of 1’s and 0’s, where a 1 indicates a
 position that you can move to and a 0 one that you cannot move to, a start
 coordinate, and an end coordinate, find the shortest path from the start
 coordinate to the end coordinate.

 4.) Sort a linked list.

 5.) Given a sudoku board, determine whether what has been placed on the board is
 a valid solution. Remember that each column must contain numbers 1-9, as must
 each row 
# ADI Interview Workshop Solutions

### Easy

1.) 

    def array_sum(array):
      sum = 0
      for element in array:
        sum += element
      return sum
2.) 

    def area(radius):
      math.pi * pow(r, 2)


3.) 

    def distance(x1, x2, y1, y2):
      sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
4.) 

    def distance(x,y):
      square_sum = 0
      for i in range(len(x)):
         square_sum += pow(x[i] - y[i], 2)
      return sqrt(square_sum)

5.) 

    def array_sum(array):
      sum = 0
      for element in array:
        sum += element
      return sum

6.)

    def fizzbuzz():
      for i in range(100):
        if i % 15 == 0:
          print "hello" 
        elif  i % 5 == 0:
          print "buzz"
        elif i % 3 == 0:
          print "fizz"
        else:
          print i
7.)

    def substring(str1, str2):
      is_substring = False  
      for i in range(len(str2)):
        is_match = True 
        for j in range(len(str1)):
           if str2[i + j] != str1[j]:
             is_match = False
        if is_match:
          return True
      return False

8.)

    def reverse(str):
      reversed_string = ""
      for i in range(len(str), 0, -1):
        reversed_string += str[i]
      return reversed_string

### Medium

1.)

Hint: How would you do it if it were one dimensional?
     
Naive Solution: Do a binary search on each row. This has an O(nlog(m)) runtime.

Proper Solution: Use binary search across rows as well, giving a runtime of 
O(log(m) * log(n)), where m and n are the numbers of rows and columns

2.)  Hint: Do we need to do a sorting algorithm at all? How do you tell if two
strings are anagrams? 

A Solution: sort each individual string by its letters, and then store the
sorted string in a dictionary that maps the sorted string to a list of indices.
These indices represent the position of elements in the array that when sorted
are the sorted string inserted in the dictionary. 

Once you have gone through the whole array, iterate over the dictionary and
for each item, make swaps in the array such that elements in the each of the
indices in the list are adjacent.

3.) Hint: What happens when you try to do this by hand?
    Hint: What if you try it with a power of 2?

    Solution: Greedily pick the biggest power of 2 that works, set that bit to 1,
    subtract that power of 2 from the decimal number, and then pick the biggest
    power of 2 that fits into that.  Keep going until finished.

4.) Hint: Think about what data structures might make sense here.

    Solution: Recursively add elements of the BST to a queue, and then dequeue
    the elements

5.)  Solution: Recurse through the tree, printing out the element on the left,
then the parent element, then the element on the right.

6.) Hint: What exactly about the strings are you comparing?

    def cipher_match(str1, str2):
      return string_to_cipher(str1) == string_to_cipher(str2)

    def string_to_cipher(str):
      used_chars = {}
      cipher = ""
      character_count = 0
      for c in str:
        dict_entry = used_chars.get(c)
        if dict_entry:
          cipher += dict_entry
        else:
          used_chars[c] = character_count
          character_count += 1
      return cipher

7.)
    def find_duplicate(list):
      element_dict = {}
      for element in list:
        if element in element_dict:
          return element
        else: 
          element_dict[element] = 1

8.)
    def fib(n):
      current =1
      previous = 1
      for i in range(n-2):
        updated_previous = current
        current = previous + current
        previous = updated_previous
      return current

9.) Hint: How would you try all possibilities?

    @memoize
    def count_change(n):
      if n == 0:
        return 1
         
      if n < 5:
        return 0 
      elif n < 10: 
        return count_change(n - 5) 
      elif n < 25:
        return count_change(n-5) + count_change(n - 10)
      else:
        return count_change(n - 25) + count_change(n - 10) + count_change(n - 5)

10.) Hint: What data structures might be helpful?

 Solution: Use a stack, and make sure the stack is empty when the program
 is complete.

11.) Solution: Use two stacks, one to keep track of the current minimum, and
one to keep track of the order that the elements came in.  The second stack
is used when push and pop operations happen, and when an element is pushed
that is lower than the current min, add it to the current min stack, and when
that element is popped, if it is the current min, pop it from the stack.

12.) Solution: recursively iterate through the string, keeping track of a list
of characters that you have already use.

13.) 

Hint: How many elements are in the power set of a list?


    def power_set(list):
      power_set_helper(list, [], [])

    # This can be done is a pure fashion I think...exercise to the reader 
    # if you care.
    
    def power_set_helper(remaining_list, current_list, power_set):
      if not remaining_list:
        power_set.append(current_list)
      else
        power_set_helper(remaining_list[1:], current_list, power_set)
        power_set_helper(remaining_list[1:], current_list.append(remaining_list[0]), power_set)
      return power_set


14.) Hint: What kind of data structure might you need to keep in place to
store information that you need?

    def print_reverse(string_list):
      dict = {}
      for str in string_list:
        if dict[str]:
          print str
          print ''.join(reversed(str))
        else:
          dict[''.join(reversed(str))] = 1

15.) 
Hint: Try drawing out a tree.

If the largest element of the tree has a lesser child, then that is the
second largest element, otherwise, it is the parent of the largest element.

16.) 

    def sort(ls):
      for i in range(len(ls)):
        for j in range(i-1,0, -1):
          if list[j] > list[j-1]:
            tmp = list[j]
            list[j] = list[j-1]
            list[j-1] = tml

17.) Hint: Could building a set of numbers be structured conceptually as a tree?

Solution:

     def meet_target(list, target):
       meet_target_helper(list, target, 0)

     def meet_target_helper(remaining_list, target, current_sum):
       if current_sum == target:
         return 1
       elif current_sum > target:
         return 0
       elif len(remaining_list) == 0:
         return 0 
       else:
         return meet_target_helper(remaining_list, target, current_sum + remaining_list[0]) +
                  meet_target_helper(remaining_list[1:], target, current_sum)

18.) Hint: Why don't you start by trying to enumerate all the continuous
subsequences? What extra work are you doing?  Try solving it by hand for
a given sequence

Naive: Try enumerating all subsequences and check the longest one. How many
are there?

Better Solution:

    def longest_continuous_subsequence(list):
      current_sum = 0
      larget_sum = 0

      for i in list:
        current_sum += i
        if current_sum > largest_sum:
          largest_sum = current_sum
        elif current_sum < 0:
          current_sum = 0

### Hard

1.) Use an array to keep track of your data, store a "program counter" as an
integer to keep track of where you are in the program, and a "data counter" to
keep track of what array element you are currently operating on. Then, use a case/switch
statement to parse out commands.  For ">" and "<" operations, move the data
counter accordingly, for "+" and "-" operations, change the data accordingly,
and for "[" and "]" change the program counter accordingly.

2 and 3.) Both require dynamic programming solutions

4.) Tedious programming--mergesort is probably the best solution here although
I think insertion sort is good enough. 

5.) This is just tedious programming, the brute force solution is good enough. 
