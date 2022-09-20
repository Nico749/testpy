a=("banana","eddie",1)
# print(type(a))
for i in a:
    print(i)

# we can covert a tuple into a list and viceversa
mylist = list(a)
print(mylist)

# tuple destructuring 
mytuple = "mark",25,"fake address"
name,age,address = mytuple
print(name)

# tuple is lighter and faster than a list 