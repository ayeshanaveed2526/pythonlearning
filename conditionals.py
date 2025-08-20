#conditional statements
# age =int(input("Enter your age:"))
# if (age>=18):
#     print("you are elgible for driving")
# else:
#     print("you are not eligible for driving")
#     print("Please try again when you are older.)
#practice q 1 :write a program to find greatest of 4 number enter by the user
# n1=int(input("Enter first number: "))
# n2=int(input("Enter second number: "))
# n3=int(input("Enter third number: "))
# n4=int(input("Enter forth number: "))
# if(n1>n2)and(n1>n3)and(n1>n4):
#     print("n1 is greatest")
# elif(n2>n3)and(n2>n4):
#     print("n2 is greatest")
# elif(n3>n4):
#     print("n3 is greatest")
# else:
#     print("n4 is greatest")
#write a program to show whether a student is passed or fail if marks is 40% and above is pass and if below 30% is fail
# marks=int(input("Enter your marks:"))
# if(marks>=40):
#     print("You are passed")
# elif(marks<=33):
#     print("You are failed")
# else:
#     print("You can try again")
# If marks are out of 100
marks1 =int(input("Enter your marks of English: "))
total=100
percentage=(marks1/total)*100
if(percentage>=40):
    print("You are passed")
elif(percentage<=33):
    print("You are failed")
else:
    print("You can try again")
marks1 =int(input("Enter your marks of Maths: "))
total=100
percentage=(marks1/total)*100
if(percentage>=40):
    print("You are passed")
elif(percentage<=33):
    print("You are failed")
else:
    print("You can try again")
marks1 =int(input("Enter your marks of Urdu: "))
total=100
percentage=(marks1/total)*100
if(percentage>=40):
    print("You are passed")
elif(percentage<=33):
    print("You are failed")
else:
    print("You can try again")
