'''
Fazer um algoritmo que pergunte o ano de nascimento de uma pessoa e o ano atual. Ao final o algoritmo
deverá exibir na tela a idade da pessoa. Porém, se o usuário inserir o ano de nascimento com valor maior
que o ano atual, o cálculo de idade não deverá ser feito, e então deverá surgir a seguinte mensagem na tela:
“Dados inseridos estão incorretos”.
'''

nasc = int(input("Informe o ano de seu nascimento:"))
ano_atual = int(input("Informe o ano atual:"))
idade = (ano_atual - nasc)

if ( ano_atual > nasc ):
    print(f"Você tem {idade} anos.")
else:
    print(f"Dados inseridos estão incorretos.")



