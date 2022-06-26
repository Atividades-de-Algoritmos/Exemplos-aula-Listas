#
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 26/06/2022
#
#
# 3 – ler uma lista de 4 notas e em seguida mostra
# as notas e a média.

# entrada de dados
lista = [] # cria uma lista vazia para armazenar os dados
soma = 0 # cria uma variável para armazenar a soma das notas

for i in range(4): # para cada i em 0 a 3 faça o seguinte
    lista.append(float(input(f"Digite uma nota[{i+1}]: "))) # adiciona a nota digitada na lista e incrementa o contador
    soma += lista[i] # soma a nota digitada na variável soma

# saida de dados
print(f"As notas são: {lista}") # imprime a lista de notas
print(f"A média é: {soma/4}") # imprime a média das notas
# ou
# print(f"A média é: {sum(lista)/len(lista)}") # imprime a média das notas

print("Fim do programa")