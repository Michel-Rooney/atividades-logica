# Armazene as alturas de 10 pessoas em uma lista. Exiba a lista e a altura média da lista

alturas = []
for i in range(1, 11):
    altura = int(input('Digite a sua altura: '))
    alturas.append(altura)
    
print(alturas)
media = sum(alturas) / len(alturas)
print(media)

