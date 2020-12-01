s="hello Iantians"
print(type(s))
print(isinstance(s,str)) #used to check if 's' is a string
print(s)
print(s.capitalize())

s1="sunanda naik"
print(s1.capitalize())

print(s1.title()) #it capitalizes first letter of every word.

print(s1.upper())
print(s1) #here value is not getting updated

s1=s1.upper() #so now if u store updated value and then display..it updates
print(s1)

print(s1.lower())

print(len(s1)) #calculates length of the string including the space

#or
length=0
for i in s1:
    length+=1
print(length)

#split function
s1=s1.split()
print(s1)

i=2345
print(len(str(i)))

#join function
print(":".join(s1))

#or concatenate
first="Sunanda"
last="Naik"
print(first+last)
print(".".join(first))

new=""
for i in first:
    if i=="S":
        new+="s"
    else:
        new+=i
print(new)

#or using replace function
newstr=first.replace("S","s")
print(newstr)

#count function
count=0
for i in first:
    if i=="a":
       count+=1
print(count)

#or now using count function
c=first.count("a")
print(c)

#formatting of string
# intro="My name is Sunanda"
# print(intro)
# 
# name=input("Please tell me your name:")
# print("My name is:",name)
# 
# #or
# intro="Hey, my name is %s"
# print(intro%(name))
# 
# #or
# name=input("Name:")
# age=int(input("Age:"))
# intro="Hey, my name is %s and my age is %i"%(name,age)
# print(intro)
# 
# #or now using format method
# name=input("Name:")
# age=input("Age:")
# intro="Hey, my name is {} and my age is {}".format(name,age)  #{} indicates any type of value can be inserted
# print(intro)
# 
# #or
# name=input("Name:")
# age=input("Age:")
# intro=f"Hey, my name is {name} and my age is {age}"
# print(intro)

num=int(input())
square=f"hey the square of your {num} is {num * num}"
print(square)

##I will be given a input and I have to check the number of times vowels came in my sentence or string.
s=input("Enter a sentence:")
vowels = ["a","e","i","o","u"] #stored all vowels in list
count=0

for character in s:
    #print(character)
    if character in vowels:
          print(character)
          count+=1

    else:
        continue
print("Total no of vowels:",count)

##I will be given a input and I have to check the number of times consonants came in my sentence or string.
s=input("Enter a sentence:")
vowels = ["a","e","i","o","u"] #stored all vowels in list
count=0

for character in s:
    #print(character)
    if character not in vowels:
          print(character)
          count+=1

    else:
        continue
print("Total no of consonants:",count)

#split() function
s="hey there"
print(s.split())

a=5
b=5
print(a==b)
print(a is b)
print(id(a),id(b))

c=1324
d=1324
print(c==d) #== it will check for equal value
print(c is d) #'is' this checks for whether in same memory location
print(id(c),id(d))

#join() function
s="hey there"
print("-".join(s))




