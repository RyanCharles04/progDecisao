'''
Desenvolver um programa que pergunte um número e exiba a informação de que ele é positivo, negativo ou
nulo.
'''

num1 = float(input("Informe um número:"))

if ( num1 >= 1):
    print(f"O {num1:.0f} é positivo")

elif ( num1 <= -1):
    print(f"{num1:.0f} é negativo")
else:
    print(f"{num1:.0f} é nulo")
