import numpy as np


def instancias(archive):
    primeira_linha = archive.readline()
    primeira_linha = primeira_linha.rstrip("\n")
    primeira_linha = primeira_linha.split(" ")
    tam = len(primeira_linha)

    if (tam == 3):
        for i in range(tam):
            primeira_linha[i] = int(primeira_linha[i])

        n_tarefas = primeira_linha[0]
        n_ferramentas = primeira_linha[1]
        capacidade = primeira_linha[2]
        concatenado = np.array([])

        for i in range(n_ferramentas):

            linha = archive.readline()
            linha = linha.rstrip()
            linha = linha.split(" ")
            linha.pop(0)
            tam = len(linha)

            for i in range(tam):
                linha[i] = int(linha[i])

            concatenado = np.concatenate((concatenado, linha))

        matrix = np.reshape(concatenado, (n_ferramentas, n_tarefas))

    else:
        n_tarefas = int(primeira_linha[0])


        segunda_linha = archive.readline()
        segunda_linha = segunda_linha.rstrip("\n")
        segunda_linha = segunda_linha.split(" ")
        n_ferramentas = int(segunda_linha[0])

        terceira_linha = archive.readline()
        terceira_linha = terceira_linha.rstrip("\n")
        terceira_linha = terceira_linha.split(" ")
        capacidade = int(terceira_linha[0])

        concatenado = np.array([])

        for i in range(n_ferramentas):

            linha = archive.readline()
            linha = linha.rstrip()
            linha = linha.split("  ")
            tam = len(linha)

            for i in range(tam):
                linha[i] = int(linha[i])

            concatenado = np.concatenate((concatenado, linha))

        matrix = np.reshape(concatenado, (n_ferramentas, n_tarefas))

    return n_tarefas, n_ferramentas, capacidade, matrix



