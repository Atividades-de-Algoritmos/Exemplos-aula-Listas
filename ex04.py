# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 26/06/2022
#
#
# 4 – ler uma lista de 5 números e imprimir o menor e
# maior valor.

# entrada de dados
lista = [] # cria uma lista vazia para armazenar os dados

for i in range(5): # para cada i em 0 a 4 faça o seguinte
    lista.append(int(input("Digite um número: "))) # adiciona o número digitado na lista

# processamento de dados
maior = max(lista) # cria uma variável para armazenar o maior número
menor = min(lista) # cria uma variável para armazenar o menor número

# saida de dados
print(f"O maior número é {maior}") # imprime o maior número
print(f"O menor número é {menor}") # imprime o menor número
print("Fim do programa") 
