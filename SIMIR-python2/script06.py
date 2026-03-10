import random 
import string

def password_generator():
    # We created a dictionary made up of letters, digits and punctuation marks.
    dictionary = string.ascii_letters + string.digits + string.punctuation 
    c = random.choice(dictionary)
    return(c) 

c1 = password_generator()
c2 = password_generator() 
c3 = password_generator()
c4 = password_generator()
c5 = password_generator()
c6 = password_generator()
c7 = password_generator()
c8 = password_generator()

passwd = c1 + c2 + c3 + c4 + c5 + c6 + c7 +c8 # We add up all the values.

print("The passwd:", passwd)
