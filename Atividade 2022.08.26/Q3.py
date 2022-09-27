p1 = float(input('Peso 1: '))
p2 = float(input('Peso 2: '))
p3 = float(input('Peso 3: '))
p4 = float(input('Peso 4: '))
p5 = float(input('Peso 5: '))
media_aritimetica_peso = (p1+p2+p3+p4+p5)/5

a1 = float(input('Altura 1: '))
a2 = float(input('Altura 2: '))
a3 = float(input('Altura 3: '))
a4 = float(input('Altura 4: '))

media_geoemtrica_altura = (a1*a2*a3*a4)/4

print(f'Pesos digitados P1: {p1}, P2: {p2}, P3: {p3}, P4: {p4}, P5: {p5}')
print(f'A media aritimetica dos pesos é {media_aritimetica_peso}\n')
print(f'Alturas digitadas A1: {a1}, A2: {a2}, A3: {a3}, A4: {a4}')
print(f'A geometrica da altura é {media_geoemtrica_altura}')
