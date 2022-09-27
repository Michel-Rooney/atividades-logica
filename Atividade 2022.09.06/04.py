# Faça um algoritmo para ler duas variáveis caracter e testar se a concatenação das duas forma a frase "MENINA BONITA". Escrever se forma ou não forma.

txt1 = str(input('Digite um palavra: ')).upper()
txt2 = str(input('Digite outra palavra: ')).upper()

concatenacao = txt1 + ' ' + txt2

if concatenacao == 'MENINA BONITA':
    print('As duas palavras que você digitou forma a frase "MENINA BONITA"')
else:
    print('O que você digitou não forma a frase "MENINA BONITA"')
