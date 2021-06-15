nome = (input('Qual o seu nome todo? '))
# Nome em maiúsculo
print(nome.upper())
# Nome em Minúsculo
print(nome.lower())
#contando a quantidade de letra ignorando os espaços
print('Seu nome todo tem {} letras'.format(len(nome) - nome.count(' ')))
#mostrando apenas o primeiro nome
dividido = (nome.split())
print('Seu primeiro nome é {} e tem {} letras'.format(dividido[0], len(dividido[0])))
