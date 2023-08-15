'''
Desenvolver um programa que pergunte dois valores numéricos inteiros e apresente o valor da diferença entre o
maior valor e o menor valor lido.
'''

num1 = int(input("Informe um número inteiro:"))
num2 = int(input("Informe outro número inteiro:"))

resultado1 = num1 - num2
resultado2 = num2 - num1

if ( num1 > num2):
    print(f"O valor da diferença entre o maior e o menor valor informado é: {resultado1}")
else:
    print(f"O valor da diferença entre o maior e o menor valor informado é: {resultado2}")
