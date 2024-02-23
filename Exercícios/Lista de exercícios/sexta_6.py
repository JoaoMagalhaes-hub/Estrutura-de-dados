# Sexta Questão

fatorial = 1

num = int(input("Digite um número inteiro positivo: "))

if num == 0 or num == 1:
    fatorial = 1
else:
    for calc in range(1, num + 1):

        fatorial *= calc

# Imprime o resultado
print(f'O fatorial de {num} é: {fatorial}')