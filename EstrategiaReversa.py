import FuncaoLeitura as opter
import numpy as np
import Reducao_de_Dominio_Reversa as reducao
import AlgoritmoGenetico as gene


def main():
    print('entrou')
    # arquivo.Lendo_Arquivos()

    with open(
            "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Teste_No_PC\\Teste_No_PC\\ChavesEtAl_2012\\ChavesEtAl_2012\\GrupoE\\L6-1.txt",
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

    genetico = gene.Genetico(nos, cluster, chaves)

    # Definindo a populacao inicial de clusters
    genetico.Populacao_Inicial(tamanho_inicial=len(list(nos)))

    # Definindo os possiveis cromossomos clusters

    possiveis_cromossomos = genetico.Possiveis_Cromossomos_Inciais()
    i = 0
    print('Executando...')
    while i <= 6:
        if i == 0:
            genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
            genetico.Individuos_Cluster()
            genetico.Individuos_Nos()

        else:
            possiveis_cromossomos = genetico.Possiveis_Cromossomos_Entre_Geracoes()
            genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
            genetico.Individuos_Nos()

        genetico.Fitness()
        print(genetico.GetFitness())
        genetico.Selecao()
        individuos_filhos_clusters = genetico.CrossOver(probabilidade_crossover=0.65)
        genetico.Mutation_Swap(probabilidade_mutação=0.1, individuo_filho_cluster=individuos_filhos_clusters)
        i += 1

    print('Fim da execução!!')


if __name__ == '__main__':
    main()
