import random
import string

# b=1
# while b<2:
x=random.randint(1, 10)
print(x)
   #b+=1
    
letters = string.ascii_lowercase#("abcdefghijklmnopqestuvwxyz")
print(letters)

rand_let=random.choices(letters,k=x)
print(rand_let)
#random.choice()
        