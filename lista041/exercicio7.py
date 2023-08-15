'''
Desenvolver um programa que pergunte um valor inteiro positivo ou negativo, e exiba como resposta o módulo
deste valor, ou seja, o número lido como sendo positivo.
'''

valor1 = int(input("Informe um número inteiro:"))
valor2 = valor1 * (-1)

if ( valor1 > 0):
    print(f"O módulo desse valor é: {valor1} ")
else:
    print(f"O módulo desse valor é: {valor2}")