n = int(input('Digite a quantidade do loop: '))
idades = []
for i in range(1, n+1):
    idade = int(input(f'Digite a {i}ª idade: '))
    idades.append(idade)

print(idades)