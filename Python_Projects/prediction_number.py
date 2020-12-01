num=int(input("Enter the number:"))
random=num*2+9
i=0
gameover=False
while gameover==False:
    if i==9:
        print('Limit Over')
        print('Enter q for Quit or p for Again Play')
        k=str(input('Enter q or p'))
        if k=='q':
            gameover=True
        elif k=='p':
            num=int(input("Enter the number:"))
            random=num*2+9
            i=0
            gameover=False

    if num==random:
        i+=1
        print(f'You Win! {i}')
        #i+=1
        gameover=True
    elif num>random:
        print('Too high')
        i+=1
        num=int(input("Enter the number:"))
    elif num<random:
        print('Too low')
        i+=1
        num=int(input("Enter the number:"))