f=open("new.txt","wt")
f.write("Data")
f.close()

r=open("new.txt","rt")
d=r.read()
print(d)

#or
with open("new1.txt","wt") as f:
    f.write("With Open")
    
with open("new1.txt","rt") as f:
    print(f.read())