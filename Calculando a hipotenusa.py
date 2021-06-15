import math

oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))

hipt = math.hypot(adjacente, oposto)
print('{:.3f}'.format(hipt))
