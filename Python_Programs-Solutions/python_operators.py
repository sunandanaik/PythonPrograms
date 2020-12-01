#ex-1
a=256
b=256
print(a==b) #true  it checks for values
print(a is b) #true
print((id(a)==id(b))) #true it checks for memory address

s1="hello there"
s2="hello there"
print(s1==s2)
s3=s1 is s2
print(s3)