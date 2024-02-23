    # Nona Questão

list_nomes = input("Digite os nomes separados por espaço: ").split()
list_nomes_1 = [nome for nome in list_nomes if nome.startswith('A')]

if list_nomes_1:

    # Imprime a lista com nomes que começam com 'A'
    print(f"Nomes que começam com a letra 'A': {list_nomes_1}")
else:
    print("Nenhum nome encontrado que comece com a letra 'A'")