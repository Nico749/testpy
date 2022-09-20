# by declaring our decorator, we can modify the behavior of a function, in this case first we print start, then we execute the 
# function and then we print end   

def start_end_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@start_end_decorator
def print_name():
    print("Nico")

print_name()