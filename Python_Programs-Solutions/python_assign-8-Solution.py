#Q-1
def high(a,b,c):
    if a>b and a>c:
        highest=a
    elif b>a and b>c:
        highest=b
    else:
        highest=c
    return highest

print(high(2,3,4))

#Q-2
def digit_reverse(a):
    a=str(a)
    b=a[::-1]  #[start:end:-1]
    return int(b)

print(digit_reverse(1234))

#Q-3
def replace_zero(a):
    a=str(a)  #typcaste to string
    b=""
    for i in a:
        if i=="0":
            b+="5"
        else:
            b+=i
    return int(b)

print(replace_zero(1006))