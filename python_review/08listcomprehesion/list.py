# forma resumida de representar listas e operacoes

lista = [x for x in range(1, 10)]
print(lista)

listaAoQuadrado = [x ** 2 for x in range(10, 1, -1)]
print(listaAoQuadrado)

numerosPares = [x for x in range(10) if x % 2 == 0]
print(numerosPares)

outro = [f'par: {x}' if x % 2 == 0 else f'impar: {x}' for x in range(10)]
print(outro)