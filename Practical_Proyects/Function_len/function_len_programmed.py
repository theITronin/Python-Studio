# Programming len without using len :)

def fun_len(var1): # We define a function.
    
    y = 0 # We initialize a variable to 0.
    for i in var1: # for loop to iterate in the string.
      y += 1  
    print(y) # we print the variable 'y' outside the loop.
    

var1 = input(str("What is the word? ")) # we request the string.
fun_len(var1) # We invoke the function.
