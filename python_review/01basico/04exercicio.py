# 1) peca o nome , a idade e converta, peca um numero do tipo float e arredonde-o:
nome: str = str(input("Informe seu nome, por favor: "))
print(f"O nome informado é: {nome}")
print("O nome informado é: {}".format(nome))  # print do python2
print("O nome informado é: " + nome)  # print como linguagem javascript, java etc

# arredondando número
numero = 10.34
print(numero)
print(round(numero, 1)) # uma casa após a vírgula