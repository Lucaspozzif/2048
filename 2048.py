#Desenvolvimento do jogo 2048 na linguagem python.
#Objetivo do jogo: somar os valores iguais de forma que eles alcançem 2048 sem que todos os espaços vazios se preencham
import random
import copy

#Variável game representa os valores que serão exibidos
game = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ]
#Variável endless representa se o jogo vai continuar além de 2048, como por exemplo 4096 ou até mais.
endless = False
score = 0

#Função showGame: exibe a variável game no display usando os valores de game como expoentes de 2.
def showGame ():
    global game
    line =[
    [2**game[0][0],2**game[0][1],2**game[0][2],2**game[0][3]],
    [2**game[1][0],2**game[1][1],2**game[1][2],2**game[1][3]],
    [2**game[2][0],2**game[2][1],2**game[2][2],2**game[2][3]],
    [2**game[3][0],2**game[3][1],2**game[3][2],2**game[3][3]]]

    #Como 2^0 é 1, todos os valores de 1 são substituidos por 0
    #Os números são convertidos em strings para que possam ter sempre 4 dígitos ou mais (no caso do modo endless)
    for i in range(len(line)):
        for j in range(len(line[i])):
            if(line[i][j] == 1):
                line[i][j] = '0000'
            elif(len(f'{line[i][j]}') < 4):
                while(len(f'{line[i][j]}')<4):
                    line[i][j] = f'0{line[i][j]}'           

    print(line[0])
    print(line[1])
    print(line[2])
    print(line[3])

    movementDetector(input(f'Pontos: {score} '))

#Função move: recebe as linhas e colunas, remove os zeros e retorna uma lista com 4 valores, deixando os zeros no fim sempre
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

#Função concat: Une valores duplicados que estão lado a lado, substituindo um deles por zero e somando +1 ao outro
def concat(i0, i1, i2, i3, j0,j1,j2,j3):
    global game
    global endless
    global score
    #Variável zero verifica se existe algum valor zero no jogo
    zero = False
    #Variável win verifica se existe algum valor 11 (pois 2¹¹ = 2048)
    win = False
    for i in range(len(game)):
        for j in range(len(game[i])):
            if(game[i][j] == 0):
                zero = True
            if(game[i][j] == 11):
                win = True
    if(win == True and endless == False):
        winner()
    elif(zero == False):
        loser()


    itemList = [game[i0][j0],game[i1][j1],game[i2][j2],game[i3][j3]]
    if(itemList[0] == itemList[1] != 0):
        itemList[0] += 1
        score += 2**itemList[0]
        itemList[1] = 0
    if(itemList[1] == itemList[2] != 0):
        itemList[1] += 1
        score += 2**itemList[1]
        itemList[2] = 0
    if(itemList[2] == itemList[3] != 0):
        itemList[2] += 1
        score += 2**itemList[2]
        itemList[3] = 0
    game[i0][j0] = itemList[0]
    game[i1][j1] = itemList[1]
    game[i2][j2] = itemList[2]
    game[i3][j3] = itemList[3]

#Função generateNum: Procura aleatoriamente por um valor igual a zero dentro de game e o substitui por 1 ou 2.
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
    #Caso o jogador tente realizar um movimento que não altera a posição de nenhum número, um novo número não deve ser gerado.
    #então, a função de gerar números só é acessada caso haja modificação na posição dos números.
    if(oldGame != game):
        generateNum()
    showGame()    
    return game

def loser():
    print('Você perdeu!!!')
    if input('Pressione qualquer tecla para jogar novamente: '): 
        print('loser')
        run()
    
def winner():
    global endless
    print('Você venceu!!!')
    end = input('Pressione "A" para continuar jogando, pressione qualquer outra tecla para reiniciar: ')
    if(end.lower() == 'a'):
        endless = True
        showGame()
    else:
        
        run()

def run():
    global game
    game = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
        ]
    generateNum()
    generateNum()
    showGame()

print('Jogo 2048, digite "w", "a", "s" e "d" para jogar')
run()