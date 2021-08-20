#Voting System Project
nominee_1=input("Enter Your name 1:")
nominee_2=input("Enter Your name 2:")

nom_1_votes=0
nom_2_votes=0

votes_id=[1,2,3,4,5,6,7,8,9,10]

num_of_voter=len(votes_id)

while True:
    if votes_id==[]:
        print("Voting Session is Over!!")
        if nom_1_votes>nom_2_votes:
            percent=(nom_1_votes/num_of_voter)*100
            print(nominee_1, " has won the election with ",percent," % votes")
            break
            
        elif nom_2_votes>nom_1_votes:
            percent=(nom_2_votes/num_of_voter)*100
            print(nominee_2, " has won the election with ",percent," % votes")
            break
    else:
        voter=int(input("Enter your voter id no.:"))
        if voter in votes_id:
            print("You are voter!!!")
            votes_id.remove(voter)
            vote=int(input("enter your vote for Bjp:1 or Congress:2="))
            if vote==1:
                nom_1_votes+=1
                print("Thank you for casting your vote to Bjp!!")
            elif vote==2:
                nom_2_votes+=1
                print("Thank you for casting your vote to Congress!!")
        else:
             print("You have already voted or Your voter id doesnot exist!!")
