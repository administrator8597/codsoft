import random
l = ["rock", "scissor", "paper"]
print("***********************************************")
print("This is a Simple Rock-Paper-Scissor Game")
print("Made By Raju Das")
print("***********************************************")
while True:
    ccount = 0
    ucount = 0

    uc = int(input('''
Game Start--
1 Yes
2 No|Exit
          '''))

    if uc == 1:
        for a in range(1, 6):
            userinput = int(input('''
--------------------------------------
Enter the number of your choice (1-3):
--------------------------------------
            1. Rock                  
            2. Scissor               
            3. Paper                 

        '''))

            if userinput == 1:
                uchoice = "rock"
            elif userinput == 2:
                uchoice = "scissor"
            elif userinput == 3:
                uchoice = "paper"
            else:
                print("Invalid Input")
                continue  

            cchoice = random.choice(l)
            print("User choice:", uchoice)
            print("Computer choice:", cchoice)

            if cchoice == uchoice:
                print("Game Draw..\n")
                ucount += 1
                ccount += 1
            elif (uchoice == "rock" and cchoice == "scissor") or (uchoice == "paper" and cchoice == "rock") or (
                    uchoice == "scissor" and cchoice == "paper"):
                print("You Win..\n")
                ucount += 1
            else:
                print("Computer Wins...\n")
                ccount += 1

        if ucount == ccount:
            print("Finally Game Draw...")
        elif ucount > ccount:
            print("Finally You Win...")
        else:
            print("Finally Computer Wins...")

        print("User Score:", ucount)
        print("Computer Score:", ccount)

    elif uc == 2:
        print("Game Exit..")
        break
    else:
        print("Sorry You Choose Wrong Option..")
        print("Please Try Again..")
       