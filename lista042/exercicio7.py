'''
Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais.
'''

num1 = float(input("Informe um número:"))
num2 = float(input("Informe outro número:"))

maior = num1

if ( maior < num2 ):
    maior = num2
    print(f"O maior valor inserido é {maior}")

menor = num1

if ( menor > num2 ):
    menor = num2
    print(f"O menor valor inserido é {menor}")

else:
    print(f"Amos números inseridos são iguais")