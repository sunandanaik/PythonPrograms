"""col
1111->row
2222
3333
4444
"""
n=4
row=1
while row <=n:
    print(str(row)*n)
    row+=1
    
"""
*
 *
   *
     *
"""
n=4
row=1
while row<=n:
    print(" " *row, "*")
    row+=1
    
"""
*
* *
* * *
* * * *
"""
n=4
row=1
while row<=n:
    print("* " * row)
    row+=1
    
"""
1
22
333
4444
"""
n=4
row=1
while row<=n:
    print(str(row)*row)
    row+=1