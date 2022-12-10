# Numa eleição existem três candidatos. Faça um programa que peça um número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato

total_eleitores = int(input('Digite a quantidade de eleitores: '))
c1, c2, c3 = 0, 0, 0
for i in range(1, total_eleitores+1):
    voto = int(input('Escolha o eleitor:\n[1] Candidato 01\n[2] Candidato 02\n[3] Candidato 03\n: '))
    if voto == 1: c1+=1
    elif voto == 2: c2+=1
    else: c3 += 1

print(f'Total votos: {total_eleitores}')
print(f'Candidato 01: {c1}')
print(f'Candidato 02: {c2}')
print(f'Candidato 03: {c3}')
