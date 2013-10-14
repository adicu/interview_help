#Given two strings, check whether the first string is a substring of the 
# second string.  What is the runtime of your algorithm? 


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

