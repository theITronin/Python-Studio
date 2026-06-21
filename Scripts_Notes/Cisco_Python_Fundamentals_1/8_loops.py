# --- Basic While Loop ---
counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1  # Loops while the condition is True, decrementing step by step.
print("Outside the loop.", counter)

# --- For Loop with range(stop) ---
for i in range(10):  # Loops from index 0 up to 9 (10 values).
    print("The value of i is", i)

# --- For Loop with range(start, stop) ---
for i in range(2, 8):  # Loops from index 2 up to 7 (excludes 8).
    print("The value of i is", i)

# --- For Loop with range(start, stop, step) ---
for i in range(2, 8, 3):  # Applies an increment step of 3 (outputs 2, then 5).
    print("The value of i is", i)

# --- Powers of 2 Generator ---
power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2

# --- Loop with time delays (time.sleep) ---
import time
for number in range(1, 6):
    print(number, "Mississippi")
    time.sleep(1)  # Delays code flow for exactly 1 second per iteration.
print("Ready or not, here I come!")

# --- Control flow: break and continue ---
# break: terminates the running loop environment immediately.
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)

# continue: skips current iteration tasks and goes straight to the next loop step.
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)

# --- While loop with an else clause ---
i = 5
while i > 5:
    print(i)
    i += 1
else:
    print("else:", i)  # Executes smoothly when the while state changes to False.

# --- For loop with an else clause ---
for i in range(5):
    print(i) 
else:
    print("else:", i)  # Executes right after the loop finishes all standard loops.

# --- Complete Algorithm: Pyramid Block Calculator ---
def calculate_pyramid_height(blocks):
    height = 0
    blocks_needed = 1
    while blocks >= blocks_needed:
        blocks -= blocks_needed
        height += 1
        blocks_needed += 1
    return height

available_blocks = int(input("Enter the number of available blocks: "))
pyramid_height = calculate_pyramid_height(available_blocks)
print(f"The maximum height of the pyramid you can build is: {pyramid_height}")