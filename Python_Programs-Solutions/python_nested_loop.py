#2 level
i_loop_count=2
j_loop_count=3

for i in range(1, i_loop_count+1):  #outer for loop
    print("i -->",i)
    for j in range(1, j_loop_count+1): #inner for loop
        print("\t j-->", j)
    print()
    
#3 Level
i_loop_count=2
j_loop_count=3

print("3-Level Loop")
for i in range(1, i_loop_count+1):  #outer for loop
    print("i -->",i)
    for j in range(1, j_loop_count+1): #inner for loop
        print("\t j-->", j)
        for k in range(1, i_loop_count+1):
            print("\t\tk->", k)
    print()
    
#next question
for i in range(1,6):
    for j in range(1,6):
        print(i,",",j, end="| ")
    print()
    
#Write a program to print following pattern.  
# 1 
# 2   2 
# 3   3 3 
# 4   4 4 4 
# 5   5 5 5 5
count=10
for i in range(1,count+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()