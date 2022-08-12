listaFibo = [0, 1]
check2 = int()

print()
print('-=-' * 9, 'SEQUÊNCIA DE FIBONACCI', '-=-' * 9)
print()

f = int(input('Quantos termos você quer mostrar? '))
sf = int(input('Qual valor você quer verificar se está na Sequência de Fibonacci? '))
t = int(0)
a = 0
b = 1
c = 0

print()
print(f'Sequência de Fibonacci em {f} termos: ')
while t < f-2:
    t += 1
    c = a + b
    a = b
    b = c
    listaFibo.append(c)

print(listaFibo)

for check in range(0, len(listaFibo)):
    if listaFibo[check] == sf:
        print()
        print(f'O valor escolhido está na Sequência na posição {check} (contando a partir de 0)')
    else:
        check2 += 1
if check2 == f:
    print()
    print('O valor escolhido NÃO está na Sequência...')

print('-=-' * 26)