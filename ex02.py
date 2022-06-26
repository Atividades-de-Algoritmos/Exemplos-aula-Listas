# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 26/06/2022
#
# 2 – ler uma lista de 5 número reais e imprimir a lista
# na ordem inversa.
#
# entrada de dados
lista = [] # cria uma lista vazia para armazenar os dados

# processamento de dados
for i in range(5): # para cada i em 0 a 4 faça o seguinte
    lista.append(float(input("Digite um número: "))) # adiciona o número digitado na lista

# saida de dados
lista2 = lista[::-1] # cria uma lista vazia para armazenar os dados e aplica o método reverse()
# ou
# lista2 = lista[:] # cria uma lista vazia para armazenar os dados e
# lista2.reverse() # aplica o método reverse()

print(lista2) # imprime a lista invertida (lista2)
print("Fim do programa")

