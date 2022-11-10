# Modifique a lista inserindo mais um convidado e exiba novamente

convidados = []
for i in range(1, 4):
    convidado = str(input(f'Digite o nome do {i}º convidado: '))
    convidados.append(convidado)

convidados.insert(0, 'Miguel')
print('Eu adicionei o Miguel a lista de convidados')
print(convidados)