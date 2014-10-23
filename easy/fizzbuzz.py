# Write FizzBuzz.  This is a function that prints out the numbers 1 to 100, and 
# whenever a multiple of 3 is reached, print ‘fizz’, when a multiple of 5 is 
# reached, print ‘buzz’, and whenever a number that is a multiple of both is 
# reached print ‘fizzbuzz’.

# Tags: [basic]

def fizzbuzz():
  for i in range(100):
    if i % 15 == 0:
      print "fizzbuzz" 
    elif  i % 5 == 0:
      print "buzz"
    elif i % 3 == 0:
      print "fizz"
    else:
      print i
