# Oitava Questão

num = int(input("Digite um número inteiro positivo para descobrir se ele é Primo ou não: "))

if num > 1:
    for calc in range(2, num): # Verificar se o número é primo
        if num % calc == 0:
            print(f"O número {num} não é primo!")
            break
    else:
        print(f"O número {num} é primo") # Imprime que é primo