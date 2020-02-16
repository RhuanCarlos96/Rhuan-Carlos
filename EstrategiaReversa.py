import FuncaoLeitura as opter
import numpy as np
import Reducao_de_Dominio_Reversa as reducao
import AlgoritmoGenetico as gene


def main():
    print('entrou')
    # arquivo.Lendo_Arquivos()

    with open(
            "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Teste_No_PC\\ChavesEtAl_2012\\ChavesEtAl_2012\\GrupoE\\L1-1.txt",
            "r") as archive:
        tarefas, ferramentas, capacidade, matrix = opter.instancias(
            archive)  # optendo todos os valores de instâncias recolhidas em um determinado arquivo

        print('A maquina possui:\n*tarefas:', tarefas, '\n*ferramentas:', ferramentas, '\n*capacidade:', capacidade)

    jobs = np.arange(0, tarefas)  # conjunto de tarefas
    t = np.arange(0, ferramentas)  # conjunto de ferramentas
    print('Conjunto de tarefas ', jobs)
    print('Conjunto de ferramentas: ', t)
    print(matrix)
    #
    nos, chaves, cluster = reducao.Reducao_de_Dominio(matrix, tarefas, capacidade, ferramentas,
                                                      jobs, t)


    genetico = gene.Genetico(nos, cluster, chaves)

    # Definindo a populacao inicial de clusters
    genetico.Populacao_Inicial(tamanho_inicial=len(list(nos)))

    # Definindo os possiveis cromossomos clusters

    possiveis_cromossomos = genetico.Possiveis_Cromossomos_Inciais()



    genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
    genetico.Individuos_Cluster()
    genetico.Individuos_Nos()



    genetico.Fitness()

    selecionados = genetico.Selecao_Torneio()
    genetico.CrossOver(selecionados=selecionados, probabilidade_crossover=0.7)



if __name__ == '__main__':
    main()
