# Uma pessoa não poderá comparecer. Pergunte quem e remova da lista de convidados e exiba a lista atulizada

convidados = []
for i in range(1, 4):
    convidado = str(input(f'Digite o nome do {i}º convidado: ')).capitalize()
    convidados.append(convidado)

print(convidados)
remover = str(input('Digite o nome dá pessoa que não poderá comparecer: ')).capitalize()
convidados.remove(remover)
print(f'A nova lista de convidados: {convidados}')
