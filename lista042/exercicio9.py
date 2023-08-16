'''
Fazer um algoritmo que pergunte a idade de uma pessoa, e ao final, informe na tela se a pessoa é menor de
idade, se é maior de idade, ou se é maior de 65 anos.
'''

idade = int(input("Informe a sua idade: "))

if  ( idade > 65 ):
    print(f"{idade} anos, você tem mais de 65 anos de idade")
elif( idade >= 18 ):
    print(f"{idade} anos, você é maior de idade")
else:
    print(f"{idade} anos, você é menor de idade")