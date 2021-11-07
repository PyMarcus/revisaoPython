# funcoes lambdas são chamadas anonimas, pois não têm nome, mas recebem argumentos e retornam um valor
variavel = lambda x: x + 1
print(variavel(10))


variavel2 = lambda a, b: a + b
print(variavel2)

# lambda mais map:
lista = list(range(5))
lb = lambda a : a ** 2
print(list(map(lb, lista)))  # map faz a passagem de um iteravel à uma funcao


# lambda e filter
lb1 = lambda a: a % 2 == 0
print(list(filter(lb1, lista)))  # filtra de um iteravel se atender a condicao


