# Problema 1 - Seleção de Atividades
# Temos N atividades com seus horários de início e término.
# Uma pessoa só pode trabalhar em uma atividade de cada vez.
# De acordo com o problema, precisamos selecionar o número máximo de atividades que podem ser realizadas por uma única pessoa.


def problema_1():
    atividades = [["A1", 0, 6],
                ["A2", 3, 4],
                ["A3", 1, 2],
                ["A4", 5, 8],
                ["A5", 5, 7],
                ["A6", 8, 9]
                    ]
    
    #ordenando as atividades pelo horario de termino
    atividades.sort(key=lambda x: x[2])
    x = 0
    primeira_atividade = atividades[0][0]
    atividades_guloso  = []
    atividades_guloso.append(primeira_atividade)
    for y in range(len(atividades)):
        if atividades[y][1] > atividades[x][2]:
            atividades_guloso.append(atividades[y][0])
            x = y
    print(atividades_guloso)

# Temos um número de moedas de diferentes denominações e a quantia total de dinheiro.
# Encontre o número mínimo de moedas necessárias para compor a quantia dada.

# valor das moedas: {1, 2, 5, 10, 20, 50, 100, 1000}


def problema_2(esperado):
    moedas = [ 2, 1, 5, 10, 50, 100, 1000,20]
    #moedas = [ 1,2, 5, 10,20, 50, 100, 1000]
    moedas.sort()

    primeira_moeda = moedas[0]
    lista_moedas = []

    while sum(lista_moedas) < esperado:
        x = 0
        for y in range(len(moedas)):
            if moedas[y] > moedas[x] and sum(lista_moedas)+moedas[y] <= esperado :
                x = y
        lista_moedas.append(moedas[x])                 
              


    print(lista_moedas)
    print(sum(lista_moedas))

#problema_2(122)

# Problema da Mochila Fracionária
# Temos um conjunto de itens, cada um com um peso e um valor.
# Determine a quantidade de cada item a incluir em uma coleção, de modo que o peso total seja menor ou igual a um limite dado e o valor total seja o maior possível.
#peso, valor, ratio
'''def problema_3(maximo):
    itens = [[40,3],[50,5],[20,1],[10,2],[30,4]]
    itens = [x + [x[1]/x[0]] for x in itens]
    itens.sort(key=lambda x: x[2])

    mochila=[]
    peso = []
    while sum(peso) < maximo:
        x=0
        for y in range(len(itens)):
            if itens[y][2] > itens[x][2] and (sum(peso) + itens[y][0]) < maximo:
                print("soma peso",sum(peso))
                print("maximo", maximo)
                x = y
        peso.append(itens[x][0])
        mochila.append(itens[x])


    print("Valor Máximo total: ", sum([x[1] for x in mochila]))
    print(mochila)

problema_3(75)'''

def problema_3(maximo):
    itens = [[6,110],[7,120],[3,2]]
    
    # Adiciona um campo de valor-por-unidade-de-peso e ordena os itens por ele em ordem decrescente
    itens = [x + [x[1]/x[0]] for x in itens]
    itens.sort(key=lambda x: x[2], reverse=True)

    mochila = []
    valor_total = 0
    peso_restante = maximo
    
    for item in itens:
        peso, valor, razao = item
        
        # Se o item pode ser adicionado completamente, faça isso
        if peso_restante >= peso:
            mochila.append(item)
            valor_total += valor
            peso_restante -= peso
        else:
            # Se apenas uma parte do item pode ser adicionada, faça isso e saia do loop
            fracao = peso_restante / peso
            mochila.append([peso * fracao, valor * fracao, razao])
            valor_total += valor * fracao
            break  # Não é possível adicionar mais itens

    print("Valor Máximo total:", valor_total)
    print("\nItens na mochila:", mochila)

problema_3(10)
