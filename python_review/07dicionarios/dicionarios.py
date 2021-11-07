# dicionários são estruturas que armazenam dados, porém , ao contrário das listas
# seus índices podem ser texto. Desse modo, é melhor para organizar

# criar um dicionario
dicionario = {}
dicionario = dict()
dicionario = {'carro':'ferrari', 'pais': 'Brazil', 1: 2}
print(dicionario)

# acessar o valor em um dicionário:
pais = dicionario['pais']
print(pais)
dois = dicionario[1]
print(dois)

"""
OBS: nas listas, a ordem é importante para verificar se são iguais, no dicionário não
"""