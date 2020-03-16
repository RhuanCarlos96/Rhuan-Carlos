import AlgoritmoGenetico as gene
import time


def Running_Genetic(nos, cluster, chaves):
    genetico = gene.Genetico(nos, cluster, chaves)

    # Definindo a populacao inicial de clusters
    genetico.Populacao_Inicial(tamanho_inicial=len(list(nos)))

    # Definindo os possiveis cromossomos clusters

    possiveis_cromossomos = genetico.Possiveis_Cromossomos_Inciais()
    before = time.time()
    now = before
    k = 0
    while now - before < 4 * 60:
        print('Geração:', k + 1)
        if k == 0:
            genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
            genetico.Individuos_Cluster()
            genetico.Individuos_Nos()

        else:
            possiveis_cromossomos = genetico.Possiveis_Cromossomos_Entre_Geracoes()
            genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
            genetico.Individuos_Nos()

        genetico.Fitness()
        genetico.Selecao()
        genetico.CrossOver(probabilidade_crossover=0.76)
        genetico.Mutation_Swap(probabilidade_mutação=0.1)
        k += 1
        now = time.time()