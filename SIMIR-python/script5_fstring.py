#    ███████╗███████╗████████╗██████╗ ██╗███╗   ██╗ ██████╗ 
#    ██╔════╝██╔════╝╚══██╔══╝██╔══██╗██║████╗  ██║██╔════╝ 
#    █████╗  ███████╗   ██║   ██████╔╝██║██╔██╗ ██║██║  ███╗
#    ██╔══╝  ╚════██║   ██║   ██╔══██╗██║██║╚██╗██║██║   ██║
#    ██║     ███████║   ██║   ██║  ██║██║██║ ╚████║╚██████╔╝
#    ╚═╝     ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 

# f-strings

# A f-string (since Python 3.6) is a string that begins con f o F
# and allows embedding Python expressions within keys {}.
# These expressions are evaluated and their result is converted into text.

name = "Pablo"
print(f"Hello {name}")
age = 24
print(f"{name} is {age} years old") # "Pablo's years"