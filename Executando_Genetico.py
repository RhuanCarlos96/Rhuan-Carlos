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
    while j < 5:
        genetico = gene.Genetico(nos, cluster, chaves)

        # Definindo a populacao inicial de clusters
        genetico.Populacao_Inicial(tamanho_da_populacao=200)

        # Definindo os possiveis cromossomos clusters
        possiveis_cromossomos = genetico.Possiveis_Cromossomos_Inciais()
        before = time.time()
        now = before

        while now - before < 6*60:
            if now - before == 0:
                genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
                genetico.Individuos_Cluster()
                genetico.Individuos_Nos()

            else:
                possiveis_cromossomos = genetico.Possiveis_Cromossomos_Entre_Geracoes()
                genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
                genetico.Individuos_Nos()

            menor_troca, tempo_do_menor = genetico.Fitness(before)
            genetico.Selecao(taxa_de_selecao=0.95)
            genetico.CrossOver(taxa_de_cruzamento=0.75)
            genetico.Mutation_Swap(taxa_de_mutação=0.1)
            menor.append(menor_troca)
            tempo.append(round(tempo_do_menor, 2))
            now = time.time()

        frequencia = genetico.GetFrequencia()

        pares = frequencia.Clusters_Piores(frequencia.Matriz_de_Frequencia_Cluster(cluster), cluster, matrix,
                                           capacidade,
                                           ferramentas, pares_ja_uilizados)


        pares_ja_uilizados = pares

        conjunto_de_nos_isolados = CompletandoNos.nos_isolados(cluster=cluster, grafo=genetico.GetGrafo())

        conjunto_de_nos_nao_isolados = CompletandoNos.nos_nao_isolados(cluster=cluster,grafo=genetico.GetGrafo())

        nos, chaves, cluster = CompletandoNos.Completando_Clusters_Eliminando_Indiviais(pares_clusters=pares,
                                                                                        cluster=cluster,
                                                                                        nos=nos, chaves=chaves,
                                                                                        matrix=matrix,
                                                                                        ferramentas=ferramentas,
                                                                                        capacidade=capacidade,
                                                                                        tarefas=len(cluster),
                                                                                        conjunto_de_nos_isolados=conjunto_de_nos_isolados,
                                                                                        conjunto_de_nos_nao_isolados=conjunto_de_nos_nao_isolados)

        j += 1

    organizar = np.argsort(menor)
    return menor[organizar[0]], tempo[organizar[0]]
