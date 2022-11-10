# Utilize o insert() e append() para adicionar mais um convidado respectivamente no meio da lista e no final

convidados = []
for i in range(1, 4):
    convidado = str(input(f'Digite o nome do {i}º convidado: ')).capitalize()
    convidados.append(convidado)

print(convidados)
final = str(input('Digite mais um convidado para para add no final da lista: ')).capitalize()
convidados.append(final)
print(convidados)
meio = str(input('Digite mais um convidado para add no meio da lista: ')).capitalize()
metade = int((len(convidados) / 2))
convidados.insert(metade, meio)
print(convidados)
