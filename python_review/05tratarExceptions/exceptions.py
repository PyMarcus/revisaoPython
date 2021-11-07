# exceptions são erros que impedem, se não tratados, a execução do programa
from typing import Mapping


def dividePorZero():
    try:
        print(3 / 0)
    except ZeroDivisionError:
        print("Você tentou dividir por zero, operação inexistente")


def tratandoErro():
    try:
        dados = int(input("Digite uma letra"))
    except ValueError:
        print("Você digitou um valor incompatível")
    else:
        print("ok")
    finally:
        print("rodou")  # finally é executado msm com exception, ou seja, dando erro ou não

# forcar excessão:
def force():
    print("Erro abaixo")
    raise TypeError("erro!")


tratandoErro()
force()



dividePorZero()
