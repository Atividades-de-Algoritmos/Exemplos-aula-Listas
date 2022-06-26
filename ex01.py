# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 26/06/2022
#
# 1 – ler uma lista de 5 número inteiros e imprimir
# cada número juntamente com a sua posição na
# lista.

# entrada de dados
lista = [] # cria uma lista vazia para armazenar os dados

# processamento de dados
for i in range(5): # para cada i em 0 a 4 faça o seguinte
    lista.append(int(input("Digite um número: "))) # adiciona o número digitado na lista

# saida de dados
for i in range(len(lista)): # para cada i em 0 a 4 faça o seguinte
    print(f"O número {lista[i]} está na posição {i}") # imprime o número e a posição da lista

print("Fim do programa")
