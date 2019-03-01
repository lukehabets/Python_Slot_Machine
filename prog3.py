import random

def main():
    credits = 20
    userQuit = 'n'
    userInput = 'n'
    userBet = 0
    
    print("Welcome to our Astronomy Slot Machine, You will start with 20 credits","\n")
    
    while(credits > 0 and userQuit != 'q'): #Main game loop

        rules(credits)
        
        userInput = input()

        if (userInput == 'B' or userInput == 'b'):
            if (userBet < 3 and userBet < credits):
                userBet = bet(userBet)
                credits = creditBetAdjust(credits)
                
        elif(userInput == 'S' or userInput == 's'):
            if(userBet > 0):
                spin()            
        elif(userInput == 'Q' or userInput == 'q'):
            userQuit = 'q'

        if (userInput != 'Q' and userInput != 'q'):
            print("Bet: ",userBet,"\n")
        
def rules(credits):
    print("To win, get 3 matching columns.","\n")
    print("A Wildcard will match with anything","\n")
    print("Press 'B' to place a bet (up to 3) and 'S' to spin","\n")
    print("Press 'Q' to quit","\n") #q or Q
    print("Credits left: ",credits,"\n")
    
def bet(creditsBet):
    creditsBet = creditsBet + 1
    return creditsBet

def creditBetAdjust(creditsHave):
    creditsHave = creditsHave - 1
    return creditsHave

def spin():
    MOON = 1
    STAR = 2
    PLANET = 3
    WILD = 4

    row1 = 0 #make this random instead of initialized to 0
    row2 = 0
    row3 = 0

    
    
main()
