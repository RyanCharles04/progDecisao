'''
Desenvolver um programa que pergunte um valor numérico inteiro e faça a exibição desse valor caso seja
divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem “Valor não é divisível por
4 e 5”.
'''

num = int(input("Insira um número inteiro:"))

div4 = num % 4
div5 = num % 5

if ( div4 == 0 and div5 == 0 ):
    print(f"{num} é divisível por 4 e 5!")
else:
    print(f"{num} não é divisível por 4 e 5!")