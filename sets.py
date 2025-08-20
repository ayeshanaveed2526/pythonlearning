#Sets in Python: set is a collection of non repetive elements
e =set()  # empty set
#sets mai koi bhi element repeat nahi hota
s ={1,3,4,56,7,4,7,8,8,2,6}
print(s)
print(type(s))  # <class 'set'>
#set method
s.add(10)  # add element
print(s)
s.remove(7)  # remove element
print(s)
s.update([1,2,3])  # add multiple elements
print(s)
y={4,5,6}
print(s.union(y))  # union of two sets
print(s.intersection(y))  # intersection of two sets
print(s.difference(y))  # difference of two sets
