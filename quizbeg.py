# Write a program that takes an integer and prints whether it’s even or odd.
# a= int(input("Enter your number"))
# if a%2==0:
#     print(a, "your number is even")

# else:
#     print (a, "your number is odd")






# Given a list of numbers, calculate their total using a for loop and also using Python’s built-in sum().
# a =[1,4,5,6,4,0,5,3,2,5,7,8]
# i=0
# for num in a:
#     i+=num
#     print("Total using for loop is ", i)
#     #and after using su function
#     print("Total using sum function is ", sum(a))





#reverse a string
# a ="hello"
# reversed_string = ""
# for char in a:
#     reversed_string = char + reversed_string
# print("Reversed string is ", reversed_string)

# Count how many vowels appear in a user-input string.
a = str(input("Enter a string: "))
vowels = "aeiouAEIOU"
count = 0   
for char in a:
    if char in vowels:
        count +=1
print("Number of vowels in the string is ", count)
