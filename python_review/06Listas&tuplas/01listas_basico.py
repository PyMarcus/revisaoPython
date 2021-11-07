# listas são tipos abstratos de dados que possuem a capacidade de armazenar diversos tipos de dados, isso é 
# importante ao lidar com grandes quantidades de dados.

# lista vazia
lista = []
lista1 = list()

print(lista)
print(lista1)
print('---' *  30)

# lista definida
lista = [1, 2, 3, 4, 5]
lista1 = ['a', 'b', 'c']
lista2 = ['olá', 'opa', 1.3, 49, True, lista]
print(lista)
print(lista1)
print(lista2)
print('---' *  30)

# acessando valores por meio do índice(ponteiro)
lista[1] # retorna o valor 2
print(lista[1])
print('---' *  30)

# percorrer lista com for:
for i in range(len(lista2)):
    print(lista2[i], end=' ')
print()

# percorrendo com base nos próprios valores
for itens in lista2:
    print(itens, end=' ')
print()
print('---' *  30)


# utilizando enumerate para pegar os índices e valores
for indices, valores in enumerate(lista2):
    print(f"indice: {indices} - valor: {valores} ")
print('---' *  30)

# ideias pré matrizes, listas de listas
lista_lista = [[1, 2, 3], [5, 6, 7]]
print(lista_lista)

print(lista_lista[0]) # retorna o primeiro valor, ou seja, a primeira lista
print(lista_lista[0][0]) # retorna na primeira lista, o primeiro valor
print('---' *  30)

# percorrer lista de lista com o for:
for linha in range(len(lista_lista)):
    for coluna in range(len(lista_lista)):
        print(lista_lista[linha][coluna], end=' ')
    print()

print('---' *  30)

# percorrendo listas ao contrario:
for i in range(len(lista2) - 1, 0, -1):
    #pass  # ---obs: pass permite ,simplismente, ignorar a instrução anterior 
    print(lista2[i])

print('---' *  30)


print(lista2[::-1]) # exibe ao contrário
print(lista2[:3]) # exibe até o 3 item (slice)
print('---' *  30)

# concatenar listas:
lista_resultante = [1, 2, 3] + [4, 5, 6]
print(lista_resultante)

print([1, 2, 3] * 2) # repete os itens expandindo a lista 
print('---' *  30)

# remover pelo índex:
del lista2[0]  # remove o primeiro item
new  = lista2
print(new)



# verificar se há o item na lista
lista = [1, 2, 3, 4]
for itens in lista:
    if 5 in lista:
        print('está na lista')
    else:
        print('não está na lista')
    if 2 not in lista:
        print('2 não está na lista')
print('---' *  30)

# ou
print(2 in lista)

print('---' *  30)

# atribuição múltipla
valor1, valor2, valor3 = [], [], []
print(valor2)

print('---' *  30)

a, b, c, d = lista
print(c)

print('---' *  30)
