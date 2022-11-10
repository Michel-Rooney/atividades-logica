class ParImpar:
    def __init__(self, repeticao: int, intervalo_inicio: 0, intervalo_fim: int):
        self.repeticao = repeticao
        self.intervalo_inicio = intervalo_inicio
        self.intervalo_fim = intervalo_fim
        self.pares = 0
        self.impares = 0
        self.contador = 1

    def leiaInt(self, texto: str) -> int:
        while True:
            try:
                num = int(input(texto))
            except (ValueError, TypeError):
                print('Valor inválido, digite apenas núneros inteiros')
            else:
                return num
    
    def check_inverlavo(self, num) -> bool:
        if (self.intervalo_inicio < num) and (num < self.intervalo_fim):
            return True
        return False

    def check_par_impar(self, num):
        if num % 2 == 0:
            self.pares += 1
        if num % 2 == 1:
            self.impares += 1

    def loop(self) -> dict:
        while self.contador <= self.repeticao:
            num = self.leiaInt('Digite um número: ')
            if not self.check_inverlavo(num):
                print(f'O valor precisa ser entre [{self.intervalo_inicio}, {self.intervalo_fim}]')
            else:
                self.check_par_impar(num)
                self.contador += 1

        return {'pares': self.pares, 'impar': self.impares}


repeticao = int(input('Digite a quantidade da repetição: '))
intervalo_inicio = int(input('Digite o valor de inicio do intervalo: '))
intervalo_fim = int(input('Digite o ultimo valor do intrevalo: '))

sla = ParImpar(repeticao, intervalo_inicio, intervalo_fim)
num = sla.loop()

print(num['pares'])
print(num['impar '])

