#Sum all elements in 2D Array
darray=[[1,2,3],[4,5,6],[7,8,9]]
sum=0
#print(darray)

for x in darray:
    print(x)
    for y in x:
        print(y, end=",")
        sum=sum+y
    print()
    print("Sum:", sum)
print("Sum is: ",sum)

#Or
darray=[[1,2,3],[4,5,6],[7,8,9]]
sum=0

for r in range(0,len(darray)):
    for c in range(0,len(darray[r])):
        sum=sum+darray[r][c]
print("Sum =", sum)

darray=[[1,2,3],[4,5,6],[7,8,9]]
sum=0
#printing individually
print(darray[0])
print(darray[2][2])