# variaveis sao formas de reservar espaços em memória para receber determinados valores
# assim, pode-se reutilizar, sobreescrever esses valores
# o nome da variavel substitui o endereco de memoria para facilitar a producao
# o valor inserido é alocado para a mesma
variavel = 3 # há agora uma referencia na memória para o nome variavel e seu valor é 3


# entrada interativa pelo usuario
variavel = input()  # variavel é sobreescrita pelo valor arbitrário que será solicitado pelo usuário

# saída, output, no monitor para exibir o valor da variavel
print(variavel)

# input interativo:
variavel = input("Informe alguma coisa: ")
print(f"Saída: {variavel}")

# input com casting
variavel = int(input("Informe um número inteiro: ")) # define que o número será inteiro, se for digitado outro tipo de dado
# será apresentado o erro Value error
print(f"O número informado é : {variavel}")



