# Given a list of strings, print out every string and its reverse if the reverse 
# of the string is also in the list.  

def print_reverse(string_list):
  dict = {}
  for str in string_list:
    if dict[str]:
      print str
      print ''.join(reversed(str))
      dict[''.join(reversed(str))] = 1

