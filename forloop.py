#for loop with break and continue statements
# Example 1: Using break statement
# for i in range(20):
#     print(i)
#     if i==13:
#         print("Breaking the loop at ", i)
#         break
# Example 2: Using continue statement
for i in range(20):
    if i%2==0:
        continue  # Skip even numbers
    print("Odd number: ", i)


# Write a program that takes an integer and prints whether it’s odd.
# a= int(input("Enter your number"))
# if a%2!=0:
#     print(a, "your number is odd")
# else:
#     print (a, "your number is even")
