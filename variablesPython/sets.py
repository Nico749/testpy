# we can create unions, differences and intersections with sets
odds = {1,3,5,7,9}
even = {0,2,4,6,8}
primes = {1,3,5,7}

u = odds.union(even)
i = odds.intersection(primes)
diff = odds.difference(primes)
print(u,i,diff)

# literals with strings 
name = "Jerry"
mystring = f"the name is {name}"
print (mystring)
