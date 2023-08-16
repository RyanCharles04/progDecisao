'''
Fazer um algoritmo que pergunte 3 números, e ao final, guarde na variável maior o maior destes 3 números
inseridos. O valor da variável maior deverá ser exibido ao final.
'''

num1 = float(input("Informe um número:"))
num2 = float(input("Informe outro número:"))
num3 = float(input("Informe o último número:"))

maior = num1

if ( maior < num2):
    maior = num2

if ( maior < num3 ):
    maior = num3

print(f"O maior valor inserido foi {maior:.0f}")