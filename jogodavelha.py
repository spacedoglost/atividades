jogodavelha = [['','',''],['','',''],['','','']]
movimento = 0

def marcarX():
    while True:
        x = input('onde deseja marcar ')
        if x == '1' and (jogodavelha[0][0] != 'O' and jogodavelha[0][0] != 'X'):
            jogodavelha[0][0] = 'X'
            break
        elif x == '2' and (jogodavelha[0][1] != 'O' and jogodavelha[0][1] != 'X'):
            jogodavelha[0][1] = 'X'
            break
        elif x == '3' and (jogodavelha[0][2] != 'O' and jogodavelha[0][2] != 'X'):
            jogodavelha[0][2] = 'X'
            break
        elif x == '4' and (jogodavelha[1][0] != 'O' and jogodavelha[1][0] != 'X'):
            jogodavelha[1][0] = 'X'
            break
        elif x == '5' and (jogodavelha[1][1] != 'O' and jogodavelha[1][1] != 'X'):
            jogodavelha[1][1] = 'X'
            break
        elif x == '6' and (jogodavelha[1][2] != 'O' and jogodavelha[1][2] != 'X'):
            jogodavelha[1][2] = 'X'
            break
        elif x == '7' and (jogodavelha[2][0] != 'O' and jogodavelha[2][0] != 'X'):
            jogodavelha[2][0] = 'X'
            break
        elif x == '8' and (jogodavelha[2][1] != 'O' and jogodavelha[2][1] != 'X'):
            jogodavelha[2][1] = 'X'
            break
        elif x == '9' and (jogodavelha[2][2] != 'O' and jogodavelha[2][2] != 'X'):
            jogodavelha[2][2] = 'X'
            break
        else: 
            print('digite uma posição em que não tenha marcado O nem o X')
            
def marcarO():
    while True:
        x = input('onde deseja marcar ')
        if x == '1' and (jogodavelha[0][0] != 'X' and jogodavelha[0][0] != 'O'):
            jogodavelha[0][0] = 'O'
            break
        elif x == '2' and (jogodavelha[0][1] != 'X' and jogodavelha[0][1] != 'O'):
            jogodavelha[0][1] = 'O'
            break
        elif x == '3' and (jogodavelha[0][2] != 'X' and jogodavelha[0][2] != 'O'):
            jogodavelha[0][2] = 'O'
            break
        elif x == '4' and (jogodavelha[1][0] != 'X' and jogodavelha[1][0] != 'O'):
            jogodavelha[1][0] = 'O'
            break
        elif x == '5' and (jogodavelha[1][1] != 'X' and jogodavelha[1][1] != 'O'):
            jogodavelha[1][1] = 'O'
            break
        elif x == '6' and (jogodavelha[1][2] != 'X' and jogodavelha[1][2] != 'O'):
            jogodavelha[1][2] = 'O'
            break
        elif x == '7' and (jogodavelha[2][0] != 'X' and jogodavelha[2][0] != 'O'):
            jogodavelha[2][0] = 'O'
            break
        elif x == '8' and (jogodavelha[2][1] != 'X' and jogodavelha[2][1] != 'O'):
            jogodavelha[2][1] = 'O'
            break
        elif x == '9' and (jogodavelha[2][2] != 'X' and jogodavelha[2][2] != 'O'):
           jogodavelha[2][2] = 'O'
           break
        else:
           print('digite em uma posição em que não tenha marcado X nem o O')

def ganhouX():
    if jogodavelha[0][0] == 'X' and jogodavelha[0][1] == 'X' and jogodavelha[0][2] == 'X':
        return 'ganhou'
    elif jogodavelha[1][0] == 'X' and jogodavelha[1][1] == 'X' and jogodavelha[1][2] == 'X':
        return 'ganhou'
    elif jogodavelha[2][0] == 'X' and jogodavelha[2][1] == 'X' and jogodavelha[2][2] == 'X':
        return 'ganhou'
    elif jogodavelha[0][0] == 'X' and jogodavelha[1][0] == 'X' and jogodavelha[2][0] == 'X':
        return 'ganhou'
    elif jogodavelha[0][1] == 'X' and jogodavelha[1][1] == 'X' and jogodavelha[2][1] == 'X':
        return 'ganhou'
    elif jogodavelha[0][2] == 'X' and jogodavelha[1][2] == 'X' and jogodavelha[2][2] == 'X':
        return 'ganhou'
    elif jogodavelha[0][0] == 'X' and jogodavelha[1][1] == 'X' and jogodavelha[2][2] == 'X':
        return 'ganhou'
    elif jogodavelha[0][2] == 'X' and jogodavelha[1][1] == 'X' and jogodavelha[2][0] == 'X':
        return 'ganhou'  
      
def ganhouO():
    if jogodavelha[0][0] == 'o' and jogodavelha[0][1] == 'O' and jogodavelha[0][2] == 'O':
        return 'ganhou'
    elif jogodavelha[1][0] == 'O' and jogodavelha[1][1] == 'O' and jogodavelha[1][2] == 'O':
        return 'ganhou'
    elif jogodavelha[2][0] == 'O' and jogodavelha[2][1] == 'O' and jogodavelha[2][2] == 'O':
        return 'ganhou'
    elif jogodavelha[0][0] == 'O' and jogodavelha[1][0] == 'O' and jogodavelha[2][0] == 'O':
        return 'ganhou'
    elif jogodavelha[0][1] == 'O' and jogodavelha[1][1] == 'O' and jogodavelha[2][1] == 'O':
        return 'ganhou'
    elif jogodavelha[0][2] == 'O' and jogodavelha[1][2] == 'O' and jogodavelha[2][2] == 'O':
        return 'ganhou'
    elif jogodavelha[0][0] == 'O' and jogodavelha[1][1] == 'O' and jogodavelha[2][2] == 'O':
        return 'ganhou'
    elif jogodavelha[0][2] == 'O' and jogodavelha[1][1] == 'O' and jogodavelha[2][0] == 'O':
        return 'ganhou'      

print('jogo da velha')

while True:
    ganhouO()
    if ganhouO() == 'ganhou':
        print('jogador O ganhou')
        break
    for i in jogodavelha:
        print (i)
    marcarX()
    movimento += 1
    if movimento == 9:
        print('Deu velha')
        break
    for i in jogodavelha:
        print (i)
    ganhouX()
    if ganhouX() == "ganhou":
        print('jogador X ganhou')
        break
    marcarO()
    movimento += 1
    if movimento == 9:
        print('Deu velha')
        break