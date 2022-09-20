# we can raise custom exceptions
# we can also use assert that will throw an exception in case what we are asserting is not true 
x= -5
if x<0:
    raise Exception("X should be positive")

# we can also use try-except block 
# try:
#     a=5%0
# except:
#     print("an error happened")
# finally:
#     print("Some random message ")