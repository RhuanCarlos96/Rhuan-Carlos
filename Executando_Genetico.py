import AlgoritmoGenetico as gene
import time
import numpy as np
import CompletandoNos


def Running_Genetic(nos, cluster, chaves):
    genetico = gene.Genetico(nos, cluster, chaves)

    # Definindo a populacao inicial de clusters
    genetico.Populacao_Inicial()

    # Definindo os possiveis cromossomos clusters

    possiveis_cromossomos = genetico.Possiveis_Cromossomos_Inciais()
    k = 0
    before = time.time()
    now = before
    menor = []
    tempo = []

    while now - before < 3:
        if k == 0:
            genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
            genetico.Individuos_Cluster()
            genetico.Individuos_Nos()

        else:
            possiveis_cromossomos = genetico.Possiveis_Cromossomos_Entre_Geracoes()
            genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
            genetico.Individuos_Nos()

        menor_troca, tempo_do_menor = genetico.Fitness(before)
        menor.append(menor_troca)
        tempo.append(tempo_do_menor)
        genetico.Selecao()
        genetico.CrossOver(probabilidade_crossover=0.75)
        genetico.Mutation_Swap(probabilidade_mutação=0.1)
        k += 1
        now = time.time()

    organizar = np.argsort(menor)
    return menor[organizar[0]], tempo[organizar[0]]


def Runnig_Genetic_with_Realimentation(nos, chaves, cluster, matrix, capacidade, ferramentas):
    pares_ja_uilizados = []
    j = 0
    menor = []
    tempo = []
    while j < 3:
        genetico = gene.Genetico(nos, cluster, chaves)

        # Definindo a populacao inicial de clusters
        genetico.Populacao_Inicial()

        # Definindo os possiveis cromossomos clusters

        possiveis_cromossomos = genetico.Possiveis_Cromossomos_Inciais()
        k = 0
        before = time.time()
        now = before
        menor = []
        tempo = []

        while now - before < 3 :
            if k == 0:
                genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
                genetico.Individuos_Cluster()
                genetico.Individuos_Nos()

            else:
                possiveis_cromossomos = genetico.Possiveis_Cromossomos_Entre_Geracoes()
                genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
                genetico.Individuos_Nos()

            menor_troca, tempo_do_menor = genetico.Fitness(before)
            menor.append(menor_troca)
            tempo.append(tempo_do_menor)
            now = time.time()
            k += 1

        frequencia = genetico.GetFrequencia()

        pares = frequencia.Clusters_Piores(frequencia.Matriz_de_Frequencia_Cluster(cluster), cluster, matrix,
                                           capacidade,
                                           ferramentas, pares_ja_uilizados)

        nos, chaves, cluster = CompletandoNos.Completando_Clusters_Eliminando_Indiviais(
            pares_clusters=pares, cluster=cluster,
            nos=nos, chaves=chaves, matrix=matrix,
            ferramentas=ferramentas, capacidade=capacidade)

        j += 1

    organizar = np.argsort(menor)
    return menor[organizar[0]], tempo[organizar[0]]
