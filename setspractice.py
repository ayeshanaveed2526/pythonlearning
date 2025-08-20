#SETS and dictionary Practice Exercise
#Write a program to create a dictonary of urdu  words with values as their english word and provide user with an option to look it up
# names={
#    "madad": "help",
#    "darwaza": "door",
#    "kursi": "chair",
#    "mez": "table",
#    "qalam": "pen",
#    "kitab": "book"
# }
# word=input("Enter the urdu word you want to look up: ")
# print(names[word])
#write a program to input 8 numbers from the users and display all the unique number once
# s=set()

# numbers= input("Enter no 1:")
# s.add(int(numbers))
# numbers= input("Enter no 2:")
# s.add(int(numbers))
# numbers= input("Enter no 3:")
# s.add(int(numbers))
# numbers= input("Enter no 4:")
# s.add(int(numbers))
# numbers= input("Enter no 5:")
# s.add(int(numbers))
# numbers= input("Enter no 6:")
# s.add(int(numbers))
# numbers= input("Enter no 7:")
# s.add(int(numbers))
# numbers= input("Enter no 8:")
# s.add(int(numbers))
# numbers= input("Enter no 9:")
# s.add(int(numbers))
# numbers= input("Enter no 10:")
# s.add(int(numbers))
# numbers= input("Enter no 11:")
# s.add(int(numbers))
# numbers= input("Enter no 12:")
# s.add(int(numbers))
# numbers= input("Enter no 1:")
# s.add(int(numbers))

# print("Unique numbers are:", s)  # Using set to get unique numbers
# create an empty dictionary and allow 4 friends to enter their favorite movies and use keys as their names.

d={}
name=input("Enter your name: ")
movie=input("Enter your favorite movie: ")
# d[name]=movie
d.update({name:movie})
name=input("Enter your name: ")
movie=input("Enter your favorite movie: ")
# d[name]=movie
d.update({name:movie})
name=input("Enter your name: ")
movie=input("Enter your favorite movie: ")
# d[name]=movie
d.update({name:movie})
name=input("Enter your name: ")
movie=input("Enter your favorite movie: ")
# `d[name]=movie`
d.update({name:movie})
# name=input("Enter your name: ")
# movie=input("Enter your favorite movie: ")
# # d[name]=movie
# d.update({name:movie})
print(d)
