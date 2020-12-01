# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))

#print(sol1,"and",sol2)

print(3/6) #0.5
print(0.5 * 2)
s="Welcome"
print(s[0]) #W
print(s.lower()) #welcome
# s[1]='r' #wrong
# print(s)

print(s.strip())

a=[1,2]
b=[2,3]
c=[3,4]
d=[a,b,c]
print(d)

print(type(4/2))

print(3**2)

x=int(1)
y=4
x=str(x)
print(x + str(y))
