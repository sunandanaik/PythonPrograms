#tuples
t1=(1,2,3,4)
print(type(t1))
print(t1)

t2=("Sunanda","Hrutika","Iant","Goa")
print(type(t2))

print(t2)

##Are tuples iterable? yes
for i in t2:
    print(i)
    
# i=1234  #here int object is not iterable
# for x in i:
#     print(x)

length=0
for i in t2:
    length+=1
print(length)  #4

##Are tuples mutable?no
print(t2[0])

# t2[0]="Hrutu"
# print(t2)

#tuples are immutable
#now to change value in tuple
li1=list(t2) #typcaste tuple into list and then change value in tuple
print(type(li1))

li1[0]="Hrutu"
t2=tuple(li1)# then typcaste back list into tuple
print(t2)

# tup1=(1, 'a', True,"b",False)
# tup1[0]=2
# print(tup1)#error- as you cannot modify tuple