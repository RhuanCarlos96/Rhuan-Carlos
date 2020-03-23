import AlgoritmoGenetico as gene
import time
import numpy as np


def Running_Genetic(nos, cluster, chaves):
    genetico = gene.Genetico(nos, cluster, chaves)

    # Definindo a populacao inicial de clusters
    genetico.Populacao_Inicial(tamanho_inicial=len(list(nos)))

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
