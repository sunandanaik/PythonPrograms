#Dictionary Examples
d={"Sun":"Mentor"}
print(type(d))

print(d)
print(d["Sun"])
print(d.keys())
print(d.values())

d1={"pineapple":{"small":90,"large":120},"Mango":80,"bananas":60,"grapes":120}
print(d1)
print(d1.keys())
print(d1.values())
print(d1["pineapple"]["small"])
d1["lichi"]=100  #to add new value in dict
print(d1)

print(d1.clear())  #clears dict
print(d1)

#Set
s={1,2,3,4,4,12,34}
print(s) #prints only unique values in set
print(type(s))
s1={"Sun","Sun",1,1,1,1}
print(s1)

