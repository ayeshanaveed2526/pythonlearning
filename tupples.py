#tupples are immutable, like strings. we use lists if we want mutable sequences.
# What is a Tuple in Python?
# A tuple is an ordered collection of items, just like a list.
# Immutable → once created, you cannot change, add, or remove elements.
# Written using parentheses ( ) instead of [ ].
numbers=(1,5,4,3,2,5,5,4,3,6,3,6,3,0)
print(type(numbers))
print(numbers)
#for empty tuple
a=(1,)
print(type(a))
print(a)
#we cant change tuple because they are immutable and they cannot be modified after creation.
