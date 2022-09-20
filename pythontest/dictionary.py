mydict ={"name":"Jack","age":73,"mail":"jackmail.com"}
name = mydict["name"]
# print(name)
# add items
mydict["gender"] = "male"
# print(mydict)
# delete items
del mydict["name"]
# iterate over the dictionary
for key,value in mydict.items():
    print(key,value)
mydict2 = {"car":"audi","citizenship":"austrian"}
mydict.update(mydict2)
print(mydict)
    