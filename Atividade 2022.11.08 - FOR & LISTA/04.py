sexos = []
alturas_mulher = []
maior = 0
menor = 9999999999
s_menor = ''
s_maior = ''
quant_homens = 0

n = int(input('Digite o número de repetições: '))

for i in range(1, n+1):
    altura = float(input(f'Digite a altura da {i} Pessoa: '))
    sexo = int(input('[1] Masculino\n[2] Feminino\n: '))
    sexo = 'M' if sexo == 1 else 'F'
    sexos.append(sexo)

    if altura > maior:
        maior = altura
        s_maior = sexo
    if altura < menor:
        menor = altura
        s_menor = sexo

    if sexo == 'F':
        alturas_mulher.append(altura)
    if sexo == 'M':
        quant_homens += 1

media = sum(alturas_mulher) / len(alturas_mulher) 
perc = (quant_homens * 100) / len(sexos)

print(f'A maior altura {maior} e é {s_maior}')
print(f'A menor altura {menor} e é {s_menor}')
print(f'A média de alturas entre as mulheres é {media:.2f}')
print(f'Tem {quant_homens} homens e a porcentagem é {perc:.2f}%')
