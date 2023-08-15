'''
Desenvolver um programa que pergunte um número inteiro qualquer e verifique se ele está na faixa de 1 a 10.
'''

num1 = float(input("Informe um número inteiro:"))

if ( num1 >= 10):
    print(f" {num1:.0f} está entre 1 à 10.")
else:
    print(f"{num1:.0f} não está entre 1 à 10")