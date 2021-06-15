# Em formato de texto
n = str(input('Digite um valor de 0 a 9999: '))
# Mostrando a unidade, dezena, centena e milhar
print(' A unidade é = {}\n A dezena é = {}\n A centena é = {}\n A milhar é = {}'.format(n[3], n[2], n[1], n[0]))

# Em formato de inteiro
num = int(input('Digite uma valor de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(' A unidade é = {}\n A dezena é = {}\n A centena é = {}\n A milhar é = {}'.format((u), (d), (c), (m)))
