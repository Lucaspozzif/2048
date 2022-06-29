import random
import copy
game = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ]

def showGame ():
    global game
    print(game[0])
    print(game[1])
    print(game[2])
    print(game[3])

    movementDetector(input())

def move(i0, i1, i2, i3, j0,j1,j2,j3):
    global game
    itemList = [game[i0][j0],game[i1][j1],game[i2][j2],game[i3][j3]]
    itemList = [x for x in itemList if x != 0]
    
    while len(itemList) < 4:
        itemList.append(0)
    game[i0][j0] = itemList[0]
    game[i1][j1] = itemList[1]
    game[i2][j2] = itemList[2]
    game[i3][j3] = itemList[3]

def concat(i0, i1, i2, i3, j0,j1,j2,j3):
    global game
    itemList = [game[i0][j0],game[i1][j1],game[i2][j2],game[i3][j3]]
    if(itemList[0] == itemList[1] != 0):
        itemList[0] += 1
        itemList[1] = 0
    if(itemList[1] == itemList[2] != 0):
        itemList[1] += 1
        itemList[2] = 0
    if(itemList[2] == itemList[3] != 0):
        itemList[2] += 1
        itemList[3] = 0
    game[i0][j0] = itemList[0]
    game[i1][j1] = itemList[1]
    game[i2][j2] = itemList[2]
    game[i3][j3] = itemList[3]

def generateNum():
    global game
    while True:
        randomLine = random.randint(0,3)
        if(0 in game[randomLine]):
            randomItem = random.randint(0,3)
            if(game[randomLine][randomItem] == 0):
                randomValue = random.randint(0,9)
                if(randomValue == 0):
                    game[randomLine][randomItem] = 2
                else:
                    game[randomLine][randomItem] = 1
                break
    return game

def movementDetector(key):
    global game
    oldGame = copy.deepcopy(game)
    if(key =='w'):
        i = len(game)-1
        while i >= 0:
            move(0,1,2,3,i,i,i,i)
            concat(0,1,2,3,i,i,i,i)
            move(0,1,2,3,i,i,i,i)
            i -= 1
    elif(key == 's'):
        i = len(game)-1
        while i >= 0:
            move(3,2,1,0,i,i,i,i)
            concat(3,2,1,0,i,i,i,i)
            move(3,2,1,0,i,i,i,i)
            i -= 1
    elif(key == 'a'):
        i = len(game)-1
        while i >= 0:
            move(i,i,i,i,0,1,2,3)
            concat(i,i,i,i,0,1,2,3)
            move(i,i,i,i,0,1,2,3)
            i -= 1
    elif(key == 'd'):
        i = len(game)-1
        while i >= 0:
            move(i,i,i,i,3,2,1,0)
            concat(i,i,i,i,3,2,1,0)
            move(i,i,i,i,3,2,1,0)
            i -= 1
    if(oldGame != game):
        generateNum()
    showGame()    
    return game

generateNum()
generateNum()
showGame()
 