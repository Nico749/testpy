import random
# generates a random float 
a=random.random()
# print(a)

# pick a random value in the list 
mylist = list ("ABCDEFGH")
b= random.sample(mylist,2)
print(b)

# if we need a value for security reasons, we use the secrets module
import secrets
# generates a number below a threshold
x= secrets.randbelow(10)