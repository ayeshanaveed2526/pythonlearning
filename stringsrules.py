#STRINGS RULES
#three ways to write strings
a= "ayesha"
b='rafia'
c='''habib'''
print(a,b,c)
#String slicing
# A string is immutable, if a string is created, it cannot be changed.
name ="ayeshanaveed"
nameshort=name[0:6] #start from 0 and include all values from 1to 3 and excluded values of 4 to onwards
print(nameshort)
namelength=len(name) #get the length of the string
print(namelength)
#we can print a letter seperately
char=name[3]
print(char)