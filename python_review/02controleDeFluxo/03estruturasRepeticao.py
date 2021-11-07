# estruturas de repetição executa diversas vezes uma instrucao, poupando assim linhas de códigos e agilizando a producao
# são bastante utilizada


# loop while
from typing import ContextManager


i = -1
while i < 2:
    print(i)
    i += 1

# while com mais de uma condicao
x = 0
while x < 3 and x != 2:
    print(x)
    x = x + 1

# while + entrada de dados
variavel = True
while variavel:
    inp = input()
    if inp == 'Marcus':
        print(inp)
        variavel = False

# ou entao>
while True:
    inp = input("Digite: ")
    if inp == 'Marcus':
        break

# funcao range() cria uma sequencia q vai de x a y podendo ou nao pular de valor a valor
print(list(range(0, 10))) # nao se considera o ultimo algarismo, para isso, use +1
print(list(range(0, 10, 3))) # de 3 em 3

# continue e a funcao for:
for i in range(0, 10):
    if i == 2:
        continue # vai pular para o inicio do loop, ou seja, o 2 não vai aparecer
    print(i)

# for itens
itens = ['maça', 'banana', 'laranja']
for item in itens:
    print(item, end=' ') # ao invés de saltar uma linha \n, imprimirá tudo na mesma

print()
for quantidade in range(len(itens)):
    print(quantidade)

