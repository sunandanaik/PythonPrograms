# #1.  Write a program to print all natural numbers from 1 to n(user input). Print the same in reverse order.
# """n=int(input("Input a number:"))
# for i in range(n,0,-1):
#     print(i)
#     
# for i in range(1,7,2):
#     print(i)"""
# 
# #to find even no
# for i in range(2,20,2):
#     print(i)
#     
# #to find odd no
# for i in range(1,11,2):
#     print(i)
#     
# for sun in range(2000,3201):
#     if sun%7==0 and sun%5!=0:
#         print(sun)

# add_sq=0
# sq_add=0
# 
# for i in range(1,101):
#     add_sq+=i
#     sq_add+=i**2
# result=sq_add-(add_sq**2)
# print(result)
#Question :4
# list1=[]
# for l in range(11):
#     list1.append(l)
# print(list1)

li=[]
for i in range(1,21):
    if i%2==0:
        li.append(i)
print(li)

#or
li2=[]
for j in range(2,21,2):
    li2.append(j)
print(li2)