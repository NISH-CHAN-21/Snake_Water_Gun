# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors"
# where players use hand gestures to represent a snake, water, or a gun. 
# The gun beats the snake, the water beats the gun, and the snake beats the water.

import random
p=0
c=0

def game():
    
    global p
    global c      
    
    char=["SNAKE","WATER","GUN"]
    
    lst=[["DRAW","WIN","LOSE"],
        ["LOSE","DRAW","WIN"],
        ["WIN","LOSE","DRAW"]]

    comp=random.randint(0,2)
    per=(input("""                                       PRESS:
                                        0 - SNAKE
                                        1 - WATER
                                        2 - GUN\n
                                        """))
    
    if (per not in ["0","1","2"]):
        raise ValueError("................WRONG INPUT...........GAME OVER............")
    
    print("YOU CHOOSE: ",char[int(per)],"\n")
    print("COMPUTER CHOOSE: ",char[comp],"\n")    
    print(lst[int(per)][comp],"\n")
    
    if(lst[int(per)][comp]=="WIN"):
        p+=1
    elif(lst[int(per)][comp]=="LOSE"):
        c+=1
    else:
        pass
    print(f"THE CURRENT SCORE IS: COMPUTER - {c} AND PLAYER - {p}\n")
    
    x=(input("""                                       WOULD YOU LIKE TO PLAY AGAIN PRESS:
                                            1 - YES
                                            0 - NO\n
                                            """))
    
    if x=="0":
        return None
    elif x=="1":
        game()
    else:
        raise ValueError("...................WRONG INPUT.................GAME OVER...............")

game()
    







