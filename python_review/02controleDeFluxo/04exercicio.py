# criar um loop para exibir o nome 10 vezes, mas, na 5 parar o loop e pular da 3 para a 4 direto
for quantidade in range(0, 10):
    if quantidade == 3:
        continue
    elif quantidade == 5:
        break
    else:
        print(f'{quantidade} Nome')
    