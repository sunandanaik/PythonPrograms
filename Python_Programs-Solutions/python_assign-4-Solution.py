#1.  Write a program to find the length of a given input string using a for loop. Ex: “Iant Python”: length = 11
# name=input("Enter Your Name :")
# length=0
# for i in name:
#     length+=1
# print(length)
#Or using len() function
leng=len("Iant Python Goa")
print(leng)

#2.  Write a program to print following pattern. 
##### 
##### 
##### 
##### 
##### 
# n=int(input("Enter n number:"))
# for p in range(n):
#     print(" # " * n)
    
#Or
n=int(input("Enter n number:"))
for p in range(1,n):
    print(" # " * p)
    
#3.  Write a program to print following pattern.  
# 1 
# 2   2 
# 3   3 3 
# 4   4 4 4 
# 5   5 5 5 5

n=int(input("Enter n number:"))
for p1 in range(1,n+1):
    print(str(p1) * p1)
    
#4 Question
number=int(input("Enter a number:"))

count=1
while count<=10:
    product=count*number
    print(number, "*", count,"=", product)
    count=count+1
    
#4th question reverse done
number=int(input("Enter a number:"))

count=10
while count>=1:
    product=count*number
    print(number, "*", count,"=", product)
    count=count-1
