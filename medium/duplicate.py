# In an array containing integers, one element is duplicated.  Find this element.  
# What is the performance of your algorithm? How much memory does it use?

def find_duplicate(list):
  element_dict = {}
  for element in list:
    if element in element_dict:
      return element
    else: 
      element_dict[element] = 1
