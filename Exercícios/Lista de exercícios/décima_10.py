# Décima Questão

# Importar as bibliotecas

from random import randint
from time import sleep

# Definir os itens
jogadas = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0,2)

print(''' Suas opções são:

[0] PEDRA
[1] PAPEL
[2] TESOURA
''')

# Turno do jogador

jogador = int(input(' Qual a sua jogada?'))

print('3')
sleep(1)
print('2')
sleep(1)
print('1!')
sleep(2)

print(f' Seu adversário jogou:{jogadas[computador]}')
print(f' Seu adversário jogou:{jogadas[jogador]}')
print('-= ' * 11)