#import this
#Q-1
s=input("Enter a string to capitalize:")
print(s.upper())

#Q-2 using loop
s1=input("Enter string to capitalize:")
s2=""
for i in s1:
    s2+=i.upper()
print(s2)
    
#Q-3
test="Hey there i am sunanda"
check=input("What You would like to check?:")

if check in test:
    print("Yes,This substring is present in test")
else:
    print("Not present")