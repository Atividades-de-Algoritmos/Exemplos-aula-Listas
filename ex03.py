#
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
#
# data: 08/07/2022
#
# 3 – ler uma lista de 4 notas e em seguida mostra
# as notas e a média.

# Processamento e entrada de dados

lista = [] # Criando uma lista vazia para armazenar os dados
soma = 0 # Criando uma variável para armazenar a soma das notas

for i in range(4): # Para cada 'i' -> item no 'range(4)' tamanho de 0 a 3 faça o seguinte
    lista.append(float(input(f"Digite uma nota[{i+1}]: "))) # Adicione a nota digitada no fim da lista com .append()
    soma += lista[i] # Soma a nota digitada na variável soma

# Saída de dados

print(f"\nAs notas são: {lista}") # Imprimindo a lista de notas
print(f"A média é: {soma/4}") # Imprimindo a média das notas

# ou

# print(f"A média é: {sum(lista)/len(lista)}") # Imprimindo a média das notas sum() soma todos os elementos da lista e o len() conta a quantidade de elementos existentes na lista

print("\nfim do programa") # Informando ao usuário que o programa terminou
