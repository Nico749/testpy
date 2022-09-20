# lambda functions are normal functions but shorter to write:
# gives back the product of each element multply by 2, and only the even numbers
a=[1,2,3,4,5]
b= map(lambda x:x*2,a)
c= filter(lambda x:x%2==0,a)
print(list(b), list(c))

# lambda function to add 10 to a number 
add10 = lambda x:x+10
# print(add10(55))