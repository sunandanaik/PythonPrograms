# for count in range(0,26):
#     print(count, "Python")
# 
#     
# text="Kaushik"
# for i in text:
#     print(i)
#     
# #list using for loop
# languages=["Eng","French","Hindi","German"]
# for l in languages:
#     print(l)
#     
# for num in range(1,101):
#     print(num)
#     
# 
# # Program to find the sum of all numbers stored in a list
# 
# # List of numbers
# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# 
# # variable to store the sum
# sum = 0
# 
# # iterate over the list
# for val in numbers:
#     sum = sum+val
# 
# print("The sum is", sum)
# 
# 
# add=0
# for i in range(1,11):
#     add=add+i
# print("Sum of first 10 numbers is =", add)
# 
# print(range(10))  # prints no from 0 to 9
# print(list(range(10)))
# 
# print(list(range(2, 8)))
# 
# print(list(range(2, 20, 2)))
# 
# # Program to iterate through a list using indexing
# 
# genre = ['pop', 'rock', 'jazz']  #len(genre)=3
# 
# # iterate over the list using index
# for j in range(len(genre)):     #for j in range(3):
#     print("I like", genre[j])  #genre[0]="pop" genre[1]="rock" genre[2]="jazz"
# 
#break and continue statements
digits = [0, 1, 5, 8]

for d in digits:
    
    if (d==5):
       continue #skips the program
    print(d)
else:
    print("No items left.")
    
# program to display student's marks from record
student_name = 'Jules'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}
# for key in marks:
#     print(key)
#     print(marks[key])
for key in marks:
    if key == student_name:
        #print(key)
        print(key, "-", marks[key])  #to retrieve dictionary key and value
        
            
        break
else:
    print('No entry with that name found.')
# 
# 
# # Program to add natural
# # numbers up to 
# # sum = 1+2+3+...+n
# 
# # To take input from the user,
# #n = int(input("Enter n: "))
# 
# n = 10
# 
# # initialize sum and counter
# sum=0
# i = 1
# 
# while i <= n:
#     sum = sum + i
#     i = i+1    # update counter i++
# 
# # print the sum
# print("The sum is", sum)
# 
# '''Example to illustrate
# the use of else statement
# with the while loop'''
# 
# counter = 0
# 
# while counter < 3:
#     print("Inside loop")
#     counter = counter + 1
# else:
#     print("Inside else")

# Use of break statement inside the loop

# for val in "python":
#     if val == "o":
#         break
#     print(val)
# 
# print("The end")
# 
# #continue
# for val in "string":
#     if val == "i":
#         continue
#     print(val)
# 
# print("The end")
# 
# for item in range(1,6):
#     if item==3:
#         break
#     print(item)
    
# while True:
#     number=float(input("Enter a number:"))
#     if number<0:
#         break
#     print("You entered:", number)
    
# while True:
#     number=float(input("Enter a number:"))
#     if number<0:
#         continue
#     print("You entered:", number)
    
# for i in range(5):
#     numb=int(input("Enter a no:"))
#     if numb<0:
#         continue
#     print(numb)
    
#Ex-1-Break Statement
n=int(input("Enter value:"))
m=int(input("Enter no to skip:"))
for i in range(1,n+1):
    if(i==m):
      break
    print(i)

#Ex-2-Continue Statement
n=int(input("Enter value:"))
m=int(input("Enter no to skip:"))
for i in range(1,n+1):
    if(i==m):
      continue
    print(i)






    
