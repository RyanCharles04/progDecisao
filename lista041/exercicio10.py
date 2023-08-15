'''
Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo
número informado é ou não um divisor do primeiro número informado.
'''

num1 = int(input("Informe um número inteiro:"))
num2 = int(input("Informe outro número inteiro:"))

resto = num2 % num1

if ( resto == 0 ):
    print(f"{num2} é divisível por {num1}!")

else:
    print(f"{num2} não é divisível {num1}!")

