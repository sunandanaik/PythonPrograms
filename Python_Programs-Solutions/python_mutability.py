a=5
print(id(a))

a=10
print(id(a))
#the objects are of immutable types
s="Sunanda"
print(id(s))

s="Sunanda Naik"
print(id(s))
#string is also of immutable data type

li=["Sunanda"]
print(id(li))

li.append("Pari")
print(li)

print(id(li))
#List is mutable data type

s2="Sunanda"
s1="Sunanda"
print(id(s2))
print(id(s1))