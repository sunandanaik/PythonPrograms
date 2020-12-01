import random

#prints random number
value=random.randint(1,10)

#print(value)
 #now user has to enter number

#print(num)

#now define function to evaluate prediction


def check_predict(num):
    if value == num:
       print("Awesome!! Your prediction is correct !")
    else:
        print("Sorry!! Your prediction was wrong !,the correct number is",value)
        predict_num()

def predict_num():
    num=eval(input("Enter a number between 1 to 10 and predict:"))
    check_predict(num)  #function calling
    
predict_num()