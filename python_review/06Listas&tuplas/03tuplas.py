# tuplas são iteráveis, assim como listas e strings, porém, assim como as strings, elas não podem ser alteradas
# ser alterada implica em não poder ser adicionado ou removido por métodos
tupla = (1, 2, 3, 4)
print(type(tupla))

novaTupla = tuple()
print(novaTupla)

outraNovaTupla = 1, 2, 3, 4
print(type(outraNovaTupla))
print(outraNovaTupla)

# vantagens da tupla : não se altera o conteúdo delas
# permitem otimizações e velocidade

