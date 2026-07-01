
# We declare the variable "amount" and assign it the value of the validated input as a float.
amount = float(input("What was the purchase amount (€):"))

# Conditionals:
if amount < 0: # We verify that the amount is not negative.
    print("Invalid amount.")
elif amount >= 50: # Amount greater than or equal to 50
    print("Free shipping.")
    print(f"Total: {amount}")
else:
    shipping_cost = 4.99 # another useful variable
    total = amount + shipping_cost
    print("The cost of shipping: 4,99€.") # Amount less than 50
    print(f"Shipping: {shipping_cost} €. Total {total} €") # We print the total (amount plus)
