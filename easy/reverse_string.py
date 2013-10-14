# Write a function to reverse a string

# Tags: [string]

def reverse(str):
  reversed_string = ""
  for i in range(len(str), 0, -1):
    reversed_string += str[i]
  return reversed_string
