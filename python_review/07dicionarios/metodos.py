# métodos principais de um dicionário:

dicionario = {}
# adicionar valores
# forma 1
dicionario['primeiro'] = 1
print(dicionario)

# forma 2
dicionario.setdefault('segundo', 2) # se a chave não existir, ele cria, se existir, ele ignora
print(dicionario)
dicionario.setdefault('primeiro', 3)
print(dicionario)

# método keys()
print(dicionario.keys()) # exibe as chaves
# método values()
print(dicionario.values()) # exibe os valores
# método itens
print(dicionario.items()) # exibe chaves e valores

# percorrer um dicionario:
for key, value in dicionario.items():
    print(f"chave: {key} - valor: {value}")

# método get: pesquisa se existe a chave e retorna um valor , caso nao
print(dicionario.get('primeiro', 'N tem')) # retorna nao tem se nao existir

print("OLA MUNDO".center(20)) # alinha ao centro
print("Ola".rjust(20,'-')) # justifica à direita


