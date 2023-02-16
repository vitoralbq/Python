from random import randrange
v= int(input('Digite o número que estou pensando? (você possui 3 tentativas): '))

x= randrange(10)

if v!=x:
    print('você possui mais 2 chances')
    v= int(input('Digite o número que estou pensando? (você possui 2 tentativas): ')) 
    if v!=x:
        print('você só possui mais 1 chance')
        v= int(input('Digite o número que estou pensando? (você possui 1 tentativas): '))
        if v!=x:
            print('Você perdeu :(')
            print(f'o número era {x}')
        else:
            print('Parabéns, você acertou!')

    else:
        print('Parabéns, você acertou!')
else: 
    print('Parabéns, você acertou de primeira')