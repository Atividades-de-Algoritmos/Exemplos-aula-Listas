#
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
#
# data: 08/07/2022
#
# 1 – ler uma lista de 5 número inteiros e imprimir
# cada número juntamente com a sua posição na
# lista.

# Entrada de dados

lista = [] # Criando uma lista vazia para armazenar os dados

# Processamento de dados

for i in range(5): # Para cada 'i' -> item no 'range()' -> tamanho de 0 a 4 faça o seguinte
    lista.append(int(input("Digite um número: "))) # Adicione no fim da lista um valor inteiro solicitado do usuário

# Saída de dados

print() # Deixa uma linha de espaço no terminal, como um enter do teclado

for i in range(len(lista)): # Para cada 'i' -> Item no 'range()' -> tamanho de 'len()' -> quantidade de elementos da lista faça o seguinte
    print(f"O número {lista[i]} está na posição {i}") # Imprima o número e a posição da lista

print("\nfim do programa")

# Versão 2.0 do código

# By: Carlos Eduardo

# ---------------------------------------------------- #

"""l1 = list() # Criando uma lista vazia com list()
contador = 5 # Variável de contagem para o while

while contador > 0: # Enquanto a nossa variavel contadora for maior que 0 executará o código
    var = int(input('Digite um número: ')) # Solicitando um valor inteiro do usuário
    l1.append(var) # Adicionando var a minha lista de valores com .append()
    contador -= 1 # Diminuindo um valor da variável para representar que um ciclo do código acabou.

print() # Deixando uma linha no terminal, como se fosse o enter do teclado

for posicao, valor in enumerate(l1):
    print(f'O número {valor} está na posição {posicao}')

print('\nfim do programa')"""

# ---------------------------------------------------- #
