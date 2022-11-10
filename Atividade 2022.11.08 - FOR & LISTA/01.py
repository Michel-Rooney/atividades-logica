nomes = []
pesos = []
for i in range(1, 11):
    nome = str(input(f'Digite o nome da {i}ª Pessoa: '))
    peso = float(input(f'Digite o peso da {i}ª Pessoa'))
    nomes.append(nome)
    pesos.append(peso)

print(nomes)
print(pesos)