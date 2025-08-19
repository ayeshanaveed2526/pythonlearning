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
#Tuple methods
#TUPPLE PRACTICE
#write a program to store 7 fruits in a list entered by the user
# fruits=[]
# fruit1=input("Enter fruit 1: ")
# fruit2=input("Enter fruit 2: ")
# fruit3=input("Enter fruit 3: ")
# fruit4=input("Enter fruit 4: ")
# fruit5=input("Enter fruit 5: ")
# fruit6=input("Enter fruit 6: ")
# fruit7=input("Enter fruit 7: ")
# fruits.append(fruit1)
# fruits.append(fruit2)
# fruits.append(fruit3)
# fruits.append(fruit4)
# fruits.append(fruit5)
# fruits.append(fruit6)
# fruits.append(fruit7)
# print(fruits)
#problem no 2
#write a program to accept marks of 5 students and show them in sorted manner
# marks=[]
# student1=input("Enter marks of student 1: ")
# student2=input("Enter marks of student 2: ")
# student3=input("Enter marks of student 3: ")
# student4=input("Enter marks of student 4: ")
# student5=input("Enter marks of student 5: ")
# marks.append(student1)
# marks.append(student2)
# marks.append(student3)
# marks.append(student4)
# marks.append(student5)
# marks.sort()
# print(marks)
#problem no 3
# check that tuple type that cannot be changed in python
# a=(8,4,3,"ayesha")
# a[3]="rafia"