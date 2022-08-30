# Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever
# o percentual que cada um representa em relação ao total de eleitores

eleitores = int(input('Total de eleitores: '))
v_brancos = int(input('Total de votos brancos: '))
v_nulos = int(input('Toal de votos nulos: '))
v_validos = int(input('Total de votos validos: '))

porc_brancos =  (v_brancos*100)/eleitores
porc_nulos =  (v_nulos*100)/eleitores
porc_validos =  (v_validos*100)/eleitores

print(f''' 
Eleitores: {eleitores}
Porcentagem de votos brancos: {porc_brancos}
Porcentagem de votos nulos: {porc_nulos}
Porcentagem de votos validos: {porc_validos}
''')

