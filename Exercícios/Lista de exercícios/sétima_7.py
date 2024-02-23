# Sétima Questão

num = int(input("Digite um número limite para a sequência de Fibonacci: "))
list_fib = [0, 1]

#Irá imprimir até chegar no limite
while list_fib[-1] + list_fib[-2] <= num:

    result = list_fib[-1] + list_fib[-2]
    list_fib.append(result)

# Imprime os resultados
print(f"Resultado da Sequência de Fibonacci até o número {num}: {list_fib}")