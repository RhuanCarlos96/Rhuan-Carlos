import FuncaoLeitura as opter
import numpy as np
import Reducao_de_Dominio_Reversa as reducao
import AlgoritmoGenetico as gene
import CompletandoNos as completando
import Funcoes_Reversa as reversa


def main():
    print('entrou')
    # arquivo.Lendo_Arquivos()

    with open(
            "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Teste_No_PC\\Teste_No_PC\\ChavesEtAl_2012\\ChavesEtAl_2012\\GrupoA\\L20-2.txt",
            "r") as archive:
        tarefas, ferramentas, capacidade, matrix = opter.instancias(
            archive)  # optendo todos os valores de instâncias recolhidas em um determinado arquivo

        print('A maquina possui:\n*tarefas:', tarefas, '\n*ferramentas:', ferramentas, '\n*capacidade:', capacidade)

    jobs = np.arange(0, tarefas)  # conjunto de tarefas
    t = np.arange(0, ferramentas)  # conjunto de ferramentas
    print('Conjunto de tarefas ', jobs)
    print('Conjunto de ferramentas: ', t)
    #
    nos, chaves, cluster = reducao.Reducao_de_Dominio(matrix, tarefas, capacidade, ferramentas,
                                                      jobs, t)

    for i in cluster:
        print(i, ':', len(cluster[i]))
    # print('Tamanho dos Nos', len(nos))
    # print('Tamanho das chaves', len(chaves))

    print('Executando...')
    k = 0
    genetico = gene.Genetico(nos, cluster, chaves)

    # Definindo a populacao inicial de clusters
    genetico.Populacao_Inicial(tamanho_inicial=len(list(nos)))

    # Definindo os possiveis cromossomos clusters

    possiveis_cromossomos = genetico.Possiveis_Cromossomos_Inciais()

    while k < 1:
        if k == 0:
            genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
            genetico.Individuos_Cluster()
            genetico.Individuos_Nos()

        else:
            possiveis_cromossomos = genetico.Possiveis_Cromossomos_Entre_Geracoes()
            genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
            genetico.Individuos_Nos()

        k+=1

        # melhor_fitness = genetico.Fitness()
        #
        # if k == 0:
        #     menor_troca = melhor_fitness
        #     k = k + 1
        #
        # else:
        #     if melhor_fitness < menor_troca:
        #         menor_troca = melhor_fitness
        #
        # selecionados = genetico.Selecao_Torneio()
        # individuos_filhos_clusters = genetico.CrossOver(selecionados=selecionados, probabilidade_crossover=0.7)
        # genetico.Mutation_Swap(probabilidade_mutação=0.1, individuo_filho_cluster=individuos_filhos_clusters)

    print('Finalizado!')

    # cluster, nos, chaves = completando.CompletandoNos([4], cluster, matrix, capacidade, t, ferramentas, nos, chaves)
    #
    # print('Tamanho dos Nos', len(nos))
    # print('Tamanho das chaves', len(chaves))


if __name__ == '__main__':
    main()
