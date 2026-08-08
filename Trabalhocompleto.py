n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro numero: ')) 
som = n1 + n2
mu = n1 * n2
div = n1 / n2
sub = n1 - n2
print(f'A soma do número {n1} mais {n2} é:{som}')
print(f'A multiplicação do número {n1} por {n2} é é:{mu}')
print(f'A divisão do número {n1} pelo número {n2} é:{div}')
print(f'A subtração entre o número {n1} menos {n2} é:{sub}')

#2

nome = input('Digite seu nome:')
idade = input('Digite sua idade:')
print(f'Seu nome é {nome}, você tem {idade} anos')

#3

nl = int(input('Digite um número:'))
if nl > 0:
    print(f'{nl} é positivo')
elif nl < 0:
    print(f'{nl} é negativo')
else:
    print(f'{nl} é zero')
    
#4

nota = int(input('Digite sua nota:'))
if nota >= 7:
    print('Aprovado')
else:
    print('Reprovado')
    
#5

numerot = int(input('Digite um número:'))
for i in range(1, 11):
    print(f'{numerot} x {i} = {numerot * i}')

#6
n = int(input('Digite um número:'))
soma = 0
for i in range(1,n+1):
    soma += i
print(f'A soma dos numeros de 1 até {n} é: {soma}')
    
#7
soma2 = 0
for i in range(10):
    numbers = int(input('Digite um número:'))
    soma2+=numbers
media = soma2/10
print(f' A soma é: {soma2}\n A média é:{media}')

#8
soma3 = 0
number3 = int(input('Digite um número(digite 0 quando quiser parar):'))
while number3 != 0:
    soma3 += number3
    number3 = int(input('Digite um número(digite 0 quando quiser parar):'))
    
print(f'Soma dos valores: {soma3}')

#9
def maior(a, b):
    if a > b:
        return a
    else:
        return b
numero1 = int(input('Digite o primeiro número:'))
numero2 = int(input('Digite o segundo número:'))
print(f'O maior número é: {maior(numero1,numero2)}')

#10
numeros4 = []
for i in range(5):
    numero4 = int(input('Digite um número:'))
    numeros4.append(numero4)
print(f'Maior valor:{max(numeros4)}')
print(f'Menor valor:{min(numeros4)}')

