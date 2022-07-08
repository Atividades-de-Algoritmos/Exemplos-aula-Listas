#
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
#
# data: 08/07/2022
#
# 2 – ler uma lista de 5 número reais e imprimir a lista
# na ordem inversa.
#

# Entrada de dados

lista = [] # Criando uma lista vazia para armazenar os dados

# Processamento de dados

for i in range(5): # Para cada 'i' -> Item no 'range()' -> Tamanho de 0 a 4 faça o seguinte
    lista.append(float(input("Digite um número: "))) # Adicione o valor flutuante solicitado na lista

# Saída de dados

lista2 = lista[::-1] # Criando uma lista vazia para armazenar os dados usando slice [::-1] para inverter

# ou

# lista2.reverse() # Aplicando o método built-in .reverse()

print(f'\nA lista: {lista}') # Imprimindo a lista normal

print(f'A lista invertida: {lista2}') # Imprimindo a lista invertida (lista2)

print("\nfim do programa") # Informando ao usuário que o programa chegou ao fim
