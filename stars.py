# n=int(input("Enter number:"))
# i=0
# for i in range(i,n+1):
#     print(" " * (n-i),end="")
#     print("*" * (2*i-1), end="")
#
#     print(" ")
 
n=int(input("Enter number:"))
i=0
for i in range(i,n+1):
    if (i==0 or i==n):
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")
