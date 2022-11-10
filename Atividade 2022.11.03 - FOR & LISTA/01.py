# LISTA DE CONVIDADOS
# Crie uma lista que inclua pelo menos três pesssoas para um jantar. Em seguida otimiza sua lista para exibir uma mensagem para cada pessoa convidando-a para jantar

convidados = []
for i in range(1, 4):
    convidado = str(input(f'Digite o nome do {i}º convidado: '))
    convidados.append(convidado)

for i in convidados:
    print(f'{i} você quer jantar?')
