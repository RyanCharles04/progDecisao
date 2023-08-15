'''
Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente.
'''

a = int(input("Informe um número:"))
b = int(input("Informe outro número:"))
c = int(input("Informe o último número:"))

# 1- a tem que ser menor que b
if ( a > b):
    aux = a
    a = b
    b = aux
#garantido até aqui que entre a e b, o menor está em a


# 2- a tem que ser menor que c
if ( a > c):
    aux = a
    a = c
    c = aux
#garantido até aqui que entre a é o menor dos 3


#necessário garantir que b seja menor que c
if ( b > c):
    aux = b
    b = c
    c = aux
#garantido até aqui que entre b e c, o b é menor, ou seja, o c é o maior


print(f"Os números enseridos em ordem crescente são: {a},{b} e {c}")