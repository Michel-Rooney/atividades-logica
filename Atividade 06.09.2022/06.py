# Contrua um algoritmo que dado o peso de uma pessoa tu vai dizer se ela é magra, normal, ou gorda
# magra até 50kg; Normal entre 51 á 80; Gorda acima de 80 

peso = float(input('Digite seu peso: '))

if peso < 50:
    print('Você é magra')
elif peso >= 50 and peso <= 80:
    print('Normal')
else:
    print('Você possui ossos grandes')
