# estruturas de controle
# condicoes if e else
# if else simples:

if 3 > 2:
    print(True)
else:
    print(False)

# elif
if 3 > 2:
    print(True)
elif 2 > 1:
    print(False)
else:
    print("fim")

# para otimizar os códigos, pode-se aninhar as estruturas condicionais:
if 2 > 4:
    print("2 é maior que 4")
else:
    if 2 < 4:
        print("ok")
    else:
        print("not")

# utilizando os operadores:
if 2 < 3 and 4 < 5:
    print("oi")
elif 2 < 4 or 5 < 1:
    print("opa")
if 2 not in [1, 3, 4]:
    print("nao está")
elif 2 in (2, 2, 2):
    print("está")

