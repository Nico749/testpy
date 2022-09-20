# collections:Counter, namedtuple, OrderedDic, defaultdict, deque
# counter gives back a dict of the characters of the string and their count 
from collections import Counter
a= "aaaannnnnbbbddddgeee"
my_counter = Counter(a)
# print(my_counter)
print(my_counter.most_common(2))
# gives back only the key, not the count 
print(my_counter.most_common(2)[0][0])

# namedtuple WE CAN CREATE 2D POINTS
from collections import namedtuple
Point  = namedtuple("Point",'x,y')
pt = Point(-2,5)
print(pt)