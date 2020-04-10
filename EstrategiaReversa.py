import FuncaoLeitura as opter
import numpy as np
import Reducao_de_Dominio_Reversa as reducao
import AlgoritmoGenetico as gene
import Lendo_Arquivos as arquivo
import time

def main():
    with open(
            "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\ChavesEtAl_2012\\ChavesEtAl_2012\\GrupoE\\L2-6.txt",
            "r") as archive:
        tarefas, ferramentas, capacidade, matrix = opter.instancias(
            archive)  # optendo todos os valores de instâncias recolhidas em um determinado arquivo

        print('A maquina possui:\n*tarefas:', tarefas, '\n*ferramentas:', ferramentas, '\n*capacidade:', capacidade)

    jobs = np.arange(0, tarefas)  # conjunto de tarefas
    t = np.arange(0, ferramentas)  # conjunto de ferramentas
    print('Conjunto de tarefas ', jobs)
    print('Conjunto de ferramentas: ', t)
    #
    nos, chaves, cluster, S = reducao.Reducao_de_Dominio(matrix, tarefas, capacidade, ferramentas,
                                                         jobs, t)

    print('S : ',S)
    print('Executando...\n')

    # pares_ja_uilizados = []
    # genetico = gene.Genetico(nos, cluster, chaves)
    #
    # # Definindo a populacao inicial de clusters
    # genetico.Populacao_Inicial()
    #
    # # Definindo os possiveis cromossomos clusters
    #
    # possiveis_cromossomos = genetico.Possiveis_Cromossomos_Inciais()
    # k = 0
    # before = time.time()
    # now = before
    # menor = []
    # tempo = []
    #
    # while now - before < 60:
    #     if k == 0:
    #         genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
    #         genetico.Individuos_Cluster()
    #         genetico.Individuos_Nos()
    #
    #     else:
    #         possiveis_cromossomos = genetico.Possiveis_Cromossomos_Entre_Geracoes()
    #         genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
    #         genetico.Individuos_Nos()
    #
    #     menor_troca, tempo_do_menor = genetico.Fitness(before)
    #     menor.append(menor_troca)
    #     tempo.append(tempo_do_menor)
    #     now = time.time()
    #     k += 1
    #
    # frequencia = genetico.GetFrequencia()
    # print(frequencia.Matriz_de_Frequencia_Cluster(cluster))
    #
    # pares = frequencia.Clusters_Piores(frequencia.Matriz_de_Frequencia_Cluster(cluster),cluster,matrix,capacidade,ferramentas,pares_ja_uilizados)
    # pares_ja_uilizados.append(pares)
    # print(pares)

    arquivo.Lendo_Arquivos()

    print('Finalizado!')

    # cluster, nos, chaves = completando.CompletandoNos([4], cluster, matrix, capacidade, t, ferramentas, nos, chaves)
    #
    # print('Tamanho dos Nos', len(nos))
    # print('Tamanho das chaves', len(chaves))



if __name__ == '__main__':
    main()
