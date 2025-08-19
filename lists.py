#if we want to store element in any programming language then we use array and lists but in python programming we use lists to store same types of elements
names=["ayesha", "hassan","habib", 8439, 8829.33, "rafia", "sohaib"]
print(names)
print(names[3])
names[4]="sidra"
print(names)
#lists are mutable they can be changed as we do above.
#list slicing
print(names[1:4])
#methods of lists
#to add something in list but at the end
names.append("izba")
print(names)
#to sort something we use sort method in numerical values
listno1=[7,9,4,3,2,1,7]
listno1.sort()
print(listno1)
#to sort in alphabetical order
alphabets=["h", "d", "s", "g", "y", "a", "b", "c"]
alphabets.sort()
print(alphabets)
# names.sort()
# print(names) #not supported between instances of 'int' and 'str' we have to change their datatypes to same values
#List reverse function: it is used to reverse the array in desending order
listno1.reverse()
print(listno1)
# to insert number in list "we dont change list element but index "
listno1.insert(3,6)
print(listno1)
# to remove element from list we use remove method
listno1.remove(7)
print(listno1)
# to remove last element from list we use pop method
listno1.pop()
print(listno1)
#functions like len,max,min,sum,minus
print(len(listno1))
print(max(listno1))
print(min(listno1))
print(sum(listno1))
