li=[[1,2,3],[4,2,6],[5,6,7],[67,89]]

#print(li)
# for i in li:
#     print(i)

#Question-1
#Now use Nested loop
add=0
for i in li:
    for j in i:
        #print(j)
        add+=j
print("Sum is:",add)

#Question-2
prod=1
sum=0
for i in li:
    for j in i:
        #print(j)
        prod*=j
        sum+=j
print("Product is:",prod)
result=prod-sum
print("Result:",result)

#Question-3
li=[]
for i in range(1,7):
    li1=[]
    for j in range(1,i+1):
        li1.append(j)
    li.append(li1)
print(li)

