'''
Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá ser exibida na tela
como resposta a média do aluno, e se ele está aprovado, reprovado ou em prova final. Estas condições
devem seguir as regras da tabela abaixo:
'''

nome = input("Qual é seu nome?")
nota1 = float(input("Informe a nota da sua prova 1:"))
nota2 = float(input("Informe a nota da sua prova 2:"))

media = (nota1 + nota2) / 2

if ( media < 3 ):
    print(f"Você ficou com {media}, está reprovado!")
elif ( media >= 3 and media <= 6,9 ):
    print(f"Você ficou com {media}, está na prova final!")
else:
    print(f"Você ficou com {media}, está Aprovado!")