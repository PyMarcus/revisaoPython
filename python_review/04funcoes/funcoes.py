# funções são subrotinas que permitem o reuso de códigos e facilitam a manutenção do mesmo
import sys
# criar uma funcao envolve definir a palavra reservada def

def funcao():
    print("Isso é uma funcao")

# funcao com parâmetro
def funcao2(nome):
    print(f"O parametro nome recebeu: {nome}")


# utilizando return (definir método):
def funcao3(num):
    return num * 2 # retorna num * 2

# construcao de funcao moderna em python(nao curto)
def funcaoComTIpage(x:int) -> int:
    return x + 1


# chamar a funcao
funcao()


# funcao recursiva:
def funcao4(num):
    if num >= 8:
        sys.exit() # finaliza execucao do programa
    print(num) 
    return funcao4(num * 2) # recursividade é uma funcao chamar a si própria, quase como em um loop

# funcao com argumentos nomeados (ou seja, se nada for passado ela retorna isso)
def mostraNome(nome="MV"):
    if nome == "MV":
        return None
    else:
        return nome



# a linha abaixo garante a execução local do programa, ou seja, ao chamar os códigos acima dessa linha, não será executado nada além deles
if __name__ == '__main__':
    funcao2('nome')  # nome é o argumento passado para o parametro da funcao
    variavel = funcao3(3)
    print(variavel)
    print("valor: " + str(funcaoComTIpage(1)))
    print(mostraNome("Joao"))
    print(mostraNome())

    print(funcao4(3))
    print('i')
