'''
Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o
aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma
mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor
da média obtida pelo aluno.
'''

nota1 = float(input("Informe sua nota de matemática:"))
nota2 = float(input("Informe sua nota de português:"))
nota3 = float(input("Informe sua nota de ciências:"))
nota4 = float(input("Informe sua nota de geografia:"))

media = (nota1 + nota2 + nota3 + nota4) / 4

if ( media >= 5):
    print(f"O aluno ficou com {media:.2f} de média, foi Aprovado!!")
else:
    print(f"O aluno ficou com {media:.2f} de média, foi Reprovado!!")