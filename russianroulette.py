import random

players = 0
playerList = []
bullets = [1,2,3,4,5,6]
griddy = 0
bullet = 0

def play():
    global bullets, griddy
    for player in playerList:
        print(f"{player}'s turn")
        input('ready?')

        griddy = random.randint(0,len(bullets)-1)
        bullet = bullets[griddy]

        if bullet == 6:
            playerList.remove(player)
            print('\n BANG \n')
            bullets = [1,2,3,4,5,6]
        
        else:
            print('\n click... \n')
            bullets.remove(bullet)
    
    if len(playerList) > 1:
        play()
    
    else:
        print(f"{playerList[0]} is the last player standing!")
        print('\n')
        ans = input("play again? (Y/N) ")

        if ans == 'Y' or ans == 'y':
            start()
        
        else:
            print(f'{playerList[0]} lives to see another day...')

def start():
    global players, playerList
    players = int(input('how many players? '))
    playerList = []
    for player in range(players):
        playerList.append(1+player)
    play()


start()
