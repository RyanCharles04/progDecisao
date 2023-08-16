'''
Fazer um algoritmo que peça um número, e ao final, informe se o número está abaixo de 1000, entre 1000 e
5000, ou acima de 5000.
'''

num = float(input("Informe um número:"))

if ( num < 1000):
    print(f"{num:.0f} está abaixo de 1000!")
else:
    if ( num >= 1000 and num <= 5000 ):
        print(f"{num:.0f} está entre 1000 e 5000!")
    else:
        print(f"{num:.0f} está acima de 5000!")