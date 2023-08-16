'''
Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso)
correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o
número inserido não corresponder à um dia da semana.
'''

num = float(input("Informe um número entre 1 a 7:"))

if ( num == 1 ):
    print(f"{num:.0f} corresponde ao primeiro dia da semana, Domingo!")
elif (num == 2):
    print(f"{num:.0f} corresponde ao segundo dia da semana, Segunda!")
elif ( num == 3):
    print(f"{num:.0f} corresponde ao terceiro dia da semana, Terça!")
elif ( num == 4):
    print(f"{num:.0f} corresponde ao quarto dia da semana, Quarta!")
elif ( num == 5):
    print(f"{num:.0f} corresponde ao quinto dia da semana, Quinta!")
elif ( num == 6):
    print(f"{num:.0f} corresponde ao sexto dia da semana, Sexta!")
elif ( num == 7):
    print(f"{num:.0f} corresponde ao sétimo dia da semana, Sabádo!")
else:
    print(f"{num:.0f} não corresponde à um dia da semana!")