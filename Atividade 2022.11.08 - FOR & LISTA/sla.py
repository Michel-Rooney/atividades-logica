pesos = []
nomes = []
idades = []
pares = []
impares = []
alturas_mulher = []
maior = 0
menor = 999999999
pessoa_maior = ''
pessoa_menor = ''
num_homens = 0


for i in range(1, 3):
    nome = str(input(f'Digite o nome da {i}ª Pessoa: '))
    peso = float(input(f'Digite o peso da {i}ª Pessoa: '))
    idade = int(input(f'Digite a idade {i}ª Pessoa: '))
    altura = float(input(f'Digite a altura da {i}ª Pessoa: '))
    sexo = int(input('Digite [1] Masculino\n[2] Feminino\n: '))
    sexo = 'M' if sexo == 1 else 'F'
    pares.append(idade) if idade % 2 == 0 else impares.append(idade)
    if altura > maior:
        maior = altura
        pessoa_maior = sexo
    if altura < menor:
        menor = altura
        pessoa_menor = sexo
    if sexo == 'F':
        alturas_mulher.append(altura)
    if sexo == 'M':
        num_homens += 1



    nomes.append(nome)
    pesos.append(peso)

    idades.append(idade)
percentual = len(nomes) 

print(nomes)
print(pesos)