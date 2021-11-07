# através da lista abaixo, converter para string, acrescentar vírgulas e ,antes da ultima palavra, colocar and
lista = ['gato', 'cachorro', 'cocota', 'papagaio']
frase = ''
for indice, itens in enumerate(lista):
    if indice < len(lista) - 1:
        frase = frase + itens + ', '
    else:
        frase = frase[:len(frase) - 2]
        frase += ' and ' + itens

print(frase)

# outra forma:
nova = ', '.join(lista[:len(lista) -1 ]) # join une elementos da lista, enquanto split separa
print(nova + ' and ' + lista[-1])
