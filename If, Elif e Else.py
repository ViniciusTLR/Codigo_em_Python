nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda  nota: "))
resultado = (nota1 + nota2) /2

print('Sua média foi = {}', resultado)

if resultado > 6.0:
    print('Parabéns, você foi APROVADO!')
elif resultado == 6.0:
    print('Eita, Aprovado, mas passou raspando!')
else:
    print('Que pena, você foi REPROVADO!')
