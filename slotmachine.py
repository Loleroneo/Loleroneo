import os
import random
import time
import tkinter as tk
from tkinter import simpledialog, messagebox

##########################################
###            Slot Machine            ###
##########################################


# Initialize tkinter
root = tk.Tk()
root.title('Slot Machine')

#global variables
money = 100
wager = 0

# Create labels to display money and slot numbers
money_label = tk.Label(root, text=f"You Start With ${money}", font=("Arial", 14))
money_label.pack(pady=10)

slot_label = tk.Label(root, text="0  0  0", font=("Arial", 50))
slot_label.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Entry widget to get the wager amount from the player
wager_label = tk.Label(root, text="Enter your wager:", font=("Arial", 12))
wager_label.pack()

wager_entry = tk.Entry(root, font=("Arial", 12))
wager_entry.pack(pady=5)


def update(num1,num2,num3):
    slot_label.config(text=f"{num1}  {num2}  {num3}")
    root.update()


def bet():
    global wager, money
    try:
        wager = float(wager_entry.get())
    except ValueError:
        result_label.config(text="Invalid input. Please enter a number.")
        return

    if wager > money:
        result_label.config(text="Wager too high")
        bet()

    elif wager == 0:
        result_label.config(text="Thanks for Playing!")
        root.quit()

    elif wager < 0:
        result_label.config(text="You can't bet negatives")
        bet()

    else:
        slot()


def mUpdate():
    global money
    money_label.config(text=f"You have ${money} left")

def slot():
    global num1, num2, num3, money
    num1 = 0
    num2 = 0
    num3 = 0
    for i in range(50,random.randint(50,75)):

        num1 = num1 + 1 if num1 != 7 else 1
        update(num1,num2,num3)
        time.sleep(0.1)

    for i in range(50,random.randint(50,75)):

        num2 = num2 + 1 if num2 != 7 else 1
        update(num1,num2,num3)
        time.sleep(0.1)

    for i in range(50,random.randint(50,75)):

        num3 = num2 + 1 if num2 != 7 else 1
        update(num1,num2,num3)
        time.sleep(0.1)

    
    if [num1, num2, num3].count(1) == 3:

        print("You Win 3x!")
        money = money + float(wager)*3
    
    if [num1, num2, num3].count(1) == 2 and [num1, num2, num3].count(1) != 3:
        
        result_label.config(text="You Win 1.5x!")
        money = money + float(wager)*1.5
    
    if num1 == 1 or num2 == 1 or num3 == 1:
        result_label.config(text="You Win 1.25x!")
        money = money + float(wager)*1.25
    
    if [num1, num2, num3].count(2) == 3:

        result_label.config(text="You Win 5x!")
        money = money + float(wager)*5
    
    if [num1, num2, num3].count(3) == 3:

        result_label.config(text="You Win 5x!")
        money = money + float(wager)*5
    
    if [num1, num2, num3].count(4) == 3:

        result_label.config(text="You Win 7x!")
        money = money + float(wager)*7
    
    if [num1, num2, num3].count(5) == 3:

        result_label.config(text="You Win 7x!")
        money = money + float(wager)*7
    
    if [num1, num2, num3].count(6) == 3:

        result_label.config(text="You Win 10x!")
        money = money + float(wager)*10
    
    if [num1, num2, num3].count(7) == 3:

        result_label.config(text="!!JACKPOT!! You Win 100x!")
        money = money + float(wager)*100

    else:
        money = money - float(wager)
    
    mUpdate()

# Button to start the game
spin_button = tk.Button(root, text="Spin", command=bet, font=("Arial", 14))
spin_button.pack(pady=10)

# Start the tkinter loop
root.mainloop()