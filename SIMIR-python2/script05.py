import random # We import 'random' module.

def roll_dice(): # We define a function that will be used for the dice.
    n = random.randrange(1,6) # We call the function "randrange" belonging to the "random" module.
    return(n) # We return the value of n to the global scope in the invocation.


n1 = roll_dice() # We invoke the "roll dice" function and save the returned value.
n2 = roll_dice() 
n3 = roll_dice()

print("Roll 1:", n1)
print("Roll 2:", n2) 
print("Roll 3:", n3) 

sum = n1 + n2 + n3 # We add up all the values.
print("Total sum:", sum)
