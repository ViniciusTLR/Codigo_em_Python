from random import randint
print('***Acerte qual foi o número que o computador escolheu de 1 a 5***\n')
aleatorio = randint(0, 5)

print('Computador: "Pensei em um número, tente adivinhar qual foi!"\n')
num = int(input('Qual foi o número que o computador pensou? '))

if num == aleatorio:
    print('Você acertou, o numero que o computador pensou foi {}'.format(aleatorio))
else:
    print('Você errou, o numero que o computador pensou foi {}'.format(aleatorio))

