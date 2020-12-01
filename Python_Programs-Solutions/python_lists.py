#2d list-internal structure of list
l=[[4,8],[9,12]]
print(l[0])
print(l[1])
print(l[0][0])

l=[[4,8],[9,12,[6,7]]]
print(l[1][2][0])

#indexing in python
s="Sunanda Naik"
print(s[0])
print(s[-1])

#slicing in python
print(s[0:10])  #[start:end]->end point is excluded
print(s[:]) #this includes all
print(s[::])
print(s[::2]) #this jumps to 2 step ->[start:end:jump]
print(s[::-1]) # slices in reverse order
print(s[10:2:-1]) #moving backward in string

#Range funtions in python
#range(start,end,jump)
limit=range(1,6)
li=list(limit)
print(li)

l2=range(1,6,2)
li1=list(l2)
print(li1)

#now using range function in looping
for i in range(1,6):
    print(i)
    
for i in range(1,6,2):
    print(i)
    
#reverse ranging
for i in range(5,1,-1):
    print(i)
