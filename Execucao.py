import numpy as np
import AlgoritmoGenetico as gene
import Reducao_de_Dominio_Reversa as reducao
import time as tempo
import CompletandoNos as completando


def Execucao(tarefas, ferramentas, matrix, capacidade):

    jobs = np.arange(0, tarefas)  # conjunto de tarefas
    t = np.arange(0, ferramentas)  # conjunto de ferramentas
    # print('Conjunto de tarefas ', jobs)
    # print('Conjunto de ferramentas: ', t)

    nos, chaves, cluster = reducao.Reducao_de_Dominio(matrix, tarefas, capacidade, ferramentas,
                                                      jobs, t)

    antes = tempo.time()
    now = antes
    i = 0

    while now - antes <= 1 * 60:

        genetico = gene.Genetico(nos_do_cluster, cluster, chaves_dos_nos)

        # Definindo a populacao inicial de clusters
        genetico.Populacao_Inicial(tamanho_inicial=len(list(nos_do_cluster)))

        # Definindo os possiveis cromossomos clusters

        possiveis_cromossomos = genetico.Possiveis_Cromossomos_Inciais()
        antes1 = tempo.time()
        agora = antes1
        k = 0

        while agora - antes1 <= 10:
            if agora - antes1 == 0.0:
                genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
                genetico.Individuos_Cluster()
                genetico.Individuos_Nos()

            else:
                possiveis_cromossomos = genetico.Possiveis_Cromossomos_Entre_Geracoes()
                genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
                genetico.Individuos_Nos()

            melhor_fitness = genetico.Fitness()

            if k == 0:
                menor_troca = melhor_fitness
                k = k + 1

            else:
                if melhor_fitness < menor_troca:
                    menor_troca = melhor_fitness

            selecionados = genetico.Selecao_Torneio()
            individuos_filhos_clusters = genetico.CrossOver(selecionados=selecionados, probabilidade_crossover=0.7)
            genetico.Mutation_Swap(probabilidade_mutação=0.1, individuo_filho_cluster=individuos_filhos_clusters)
            agora = tempo.time()

        frequencias = genetico.GetFrequencia()
        matriz_final = frequencias.Matriz_de_Frequencia_Cluster(cluster=cluster)

        salvar = "matriz_frequencia" + str(i) + ".txt"

        np.savetxt(salvar, matriz_final, fmt='%.0f')

        cluster_a_serem_preenchidos = frequencias.Clusters_Piores(matriz_final=matriz_final, cluster=cluster,
                                                                  matrix=matrix, capacidade=capacidade,
                                                                  ferramentas=ferramentas)

        cluster, nos_do_cluster, chaves_dos_nos = completando.CompletandoNos(
            conjunto_de_tarefas=cluster_a_serem_preenchidos, cluster=cluster, matrix=matrix, capacidade=capacidade,
            tools=t, ferramentas=ferramentas, nos=nos_do_cluster, chaves=chaves_dos_nos)

        now = tempo.time()
        i += 1
