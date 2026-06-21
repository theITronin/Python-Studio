# --- Bubble Sort Algorithm Implementation ---
my_list = [8, 10, 6, 2, 4]
swapped = True

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)  # Output: [2, 4, 6, 8, 10]

# --- Interactive Bubble Sort Version ---
my_list = []
swapped = True
num = int(input("How many elements do you want to sort?: "))

for i in range(num):
    val = float(input("Enter an element for the list: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)

# --- Built-in Sorting Methods ---
# Ascending Order
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)  # Output: [2, 4, 6, 8, 10]

# Descending Order
my_list = [8, 10, 6, 2, 4]
my_list.sort(reverse=True)
print(my_list)  # Output: [10, 8, 6, 4, 2]