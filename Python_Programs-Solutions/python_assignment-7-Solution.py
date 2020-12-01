#Q-1
def power_fun(x,y):
    return x**y

print("Power is:",power_fun(3,2))

#Q-2
s="Hi i am cool mentor"
li=s.split()
print(len(li))
def count_words(s):
    li=s.split()
    return len(li)

#Q-3
def calculator(a,b):
    
    choice=input("Enter your choice:")
    if choice=="Sum":
        return a+b
    elif choice=="prod":
        return a*b
    elif choice=="Sub":
        return a-b
    elif choice=="Div":
        return a/b
    elif choice=="Power":
        return a**b
    elif choice=="Rem":
        return a%b
    else:
        return "Valid choice you must input"
    
print("Result:",sum_prod(2,3))
    