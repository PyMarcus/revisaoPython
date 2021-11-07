# métodos são funções atribuídas à valores

# encontrar valor em uma lista
from typing import List


lista = [1, 2, 3]
print(lista.index(2)) # retorna o índice do valor 2

# adicionar valor à uma lista
lista.append(4) # acrescenta ao final
lista.append(0)
print(lista)

lista.insert(1, 'oi') # acrescenta 'oi' à segunda posicao
print(lista)

# remover valor
lista.remove('oi')
print(lista)

# ordernar (colocar em ordem crescente)
lista.sort()
print(lista)

# colocar em ordem decrescente
lista.sort(reverse=True)
print(lista)
