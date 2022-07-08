#
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
#
# data: 08/07/2022
#
# 4 – ler uma lista de 5 números e imprimir o menor e
# maior valor.

# Entrada de dados

lista = [] # Cria uma lista vazia para armazenar os dados

for i in range(5): # Para cada 'i' -> Item em 0 a 4 faça o seguinte
    lista.append(int(input("Digite um número: "))) # Adicione o número digitado na lista

# Processamento de dados

maior = max(lista) # Criando uma variável para armazenar o maior número usando max()
menor = min(lista) # Criando uma variável para armazenar o menor número usando min()

# Saída de dados

print(f"\nO maior número é {maior}") # Imprimindo o maior número
print(f"O menor número é {menor}") # Imprimindo o menor número

print('\nfim do programa') # Informando ao usuário que o programa terminou
