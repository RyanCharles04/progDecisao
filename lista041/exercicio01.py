'''
Desenvolver um programa que pergunte um número. Se este número for maior que 20, então ele deverá exibir a
metade deste número, senão, ele deverá exibir o número sem alterações.
'''

num = float(input("Informe um número:"))

if ( num > 20):
    metade = num / 2
    print(f"A metade desse número é: {metade:.0f}")
else:
    print(f"O número inserido é: {num:.0f}")