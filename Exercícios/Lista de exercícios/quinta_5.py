# Quinta Questão

from random import randint

# Criando as listas
list_numero = []
list_numero_par = []
quant_par = 0

# Cria um loop com o for 10 vezes
for i in range(10):

    sorteio_numeros = randint(1, 100)
    list_numero.append(sorteio_numeros)

    if (sorteio_numeros % 2) == 0:

        list_numero_par.append(sorteio_numeros)
        quant_par += 1

if quant_par >= 0:
    media_numero_par = sum(list_numero_par) / quant_par

else:
    media_numero_par = 0

# Printar resultados
print(f"A lista possui esses números: {list_numero}")
print(f"Dentre eles, existem uma quantidade de: {quant_par} e os números pares são: {list_numero_par}")
print(f"A media dos números será: {media_numero_par:.1f}")