# Write a Brainf*ck interpreter.  Brainf*ck is a language consisting of characters
# “><+-[ ].,”, where the program itself represents a large array.  The command
# “>” moves a data pointer, which points at a given element, to the element on
# the right, the command “<” moves the data pointer to the element on the left,
# “+” increments the value of the element that the data pointer is pointed it,
# and “-” decrements it.  “,” takes raw input and puts it in the element that the
# data pointer is it, and “.” outputs the value of the current element. The “]”
# and “[“ characters handle looping--when a “]” is reached, if the value of the
# cell that the data pointer is pointed is 0, then move the corresponding “[“ character.

