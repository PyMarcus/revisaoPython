# advinhe o número: de 1 a 20 aleatório
from random import randint

numero = randint(1, 20)
while True:
    try:
        digitado = int(input("Adivinhe um número: "))
    except ValueError as V:
        print("O valor inserido não é um número")
        print(f"Error: {v}")
    else:
        if digitado == numero:
            print("Parabéns!")
            break
        else:
            print("Incorreto!")
            print(f"O número era {numero}")