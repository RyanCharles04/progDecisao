'''
Fazer um algoritmo que peça um número, e ao final, informe se o número digitado está acima de 1000 ou
abaixo de 1000.
'''

num = float(input("Informe um número:"))

if ( num > 1000):
    print(f"{num:.0f} está acima de 1000!")

else:
    if ( num < 1000 ):
        print(f"{num:.0f} está abaixo de 1000!")
    else:
        print(f"O número é 1000!")