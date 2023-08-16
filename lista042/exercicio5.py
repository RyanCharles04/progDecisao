'''
Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.
'''

estado = (input("Informe uma sigla de um estado brasileiro:"))

if ( estado == "RJ"):
    print(f"A sigla {estado} está na Região Sudeste!")
elif ( estado == "SP"):
    print(f"A sigla {estado} está na Região Sudeste!")
elif ( estado == "ES"):
    print(f"A sigla {estado} está na Região Sudeste!")
elif ( estado == "MG"):
    print(f"A sigla {estado} está na Região Sudeste!")
else:
    print(f"A sigla {estado} não corresponde à um estado da Região Sudeste!")
