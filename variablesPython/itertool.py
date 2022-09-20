# itertools: products, permutations, combinations, accumulate, groupby, infinite iterators
# make the product of 2 matrices
from itertools import product
a= [1,2]
b = [3,4]
prod = product(a,b)
print(list(prod)) 
# WE NEED TO PUT IT AS LIST TO READ THE RESULT
# gives back all the possible combinations of the values in the list 
from itertools import permutations
c=[1,2,3]
perm = permutations(c)
print(list(perm))

# groupby allows us to group a list in sublits based on a condition we provide 
from itertools import groupby
# we define a custom function 
def smaller_than_4(x):
    return x<4

numbers = [1,2,3,4,5,56,2,22]
group_obj = groupby(numbers, key=smaller_than_4)
for key,value in group_obj:
    print(key, list(value))