import os
import random
import time

##########################################
###            Slot Machine            ###
##########################################


def clear():
  os.system('cls')


money = 100
print(f"You Start With ${money}")


def bet():
    global wager, money
    wager = input("How much would you like to wager?(Type \"0\" to quit) ")
    money = money - int(wager)
    if money < 0:
        print("Wager too high")
        money = money + int(wager)
        bet()
    elif int(wager) == 0:
        print("Thanks for Playing!")
    elif int(wager) < 0:
        print("You can't bet negatives")
        bet()
    else:
        slot()


def slot():
    global num1, num2, num3, money
    num1 = 0
    num2 = 0
    num3 = 0
    for i in range(15,random.randint(15,30)):

        if num1 != 7:
            num1 += 1
        else:
            num1 = 1

        print(num1,num2,num3)
        time.sleep(0.1)
        clear()

    for i in range(15,random.randint(15,30)):

        if num2 != 7:
            num2 += 1
        else:
            num2 = 1

        print(num1,num2,num3)
        time.sleep(0.1)
        clear()

    for i in range(15,random.randint(15,30)):

        if num3 != 7:
            num3 += 1
        else:
            num3 = 1

        print(num1,num2,num3)
        time.sleep(0.1)
        clear()


    print(num1,num2,num3)
    
    if [num1, num2, num3].count(1) == 3:

        print("You Win 3x!")
        money = money + float(wager)*3
    
    if [num1, num2, num3].count(1) == 2 and [num1, num2, num3].count(1) != 3:
        
        print("You Win 1.5x!")
        money = money + float(wager)*1.5
    
    if num1 == 1 or num2 == 1 or num3 == 1:
        print("You Win 1.25x!")
        money = money + float(wager)*1.25
    
    if [num1, num2, num3].count(2) == 3:

        print("You Win 5x!")
        money = money + float(wager)*5
    
    elif [num1, num2, num3].count(2) == 1 and [num1, num2, num3].count(2) != 3:

        print("You Win 1.5x!")
        money = money + float(wager)*1.5
    
    if [num1, num2, num3].count(3) == 3:

        print("You Win 5x!")
        money = money + float(wager)*5
    
    if [num1, num2, num3].count(4) == 3:

        print("You Win 7x!")
        money = money + float(wager)*7
    
    if [num1, num2, num3].count(5) == 3:

        print("You Win 7x!")
        money = money + float(wager)*7
    
    if [num1, num2, num3].count(6) == 3:

        print("You Win 10x!")
        money = money + float(wager)*10
    
    if [num1, num2, num3].count(7) == 3:

        print("!!JACKPOT!! You Win 100x!")
        money = money + float(wager)*100

    money = round(money)
    print(f"You have ${money} left")
    bet()
bet()
