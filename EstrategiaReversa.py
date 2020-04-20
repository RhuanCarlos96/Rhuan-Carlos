import FuncaoLeitura as opter
import numpy as np
import Reducao_de_Dominio_Reversa as reducao
import AlgoritmoGenetico as gene
import Lendo_Arquivos as arquivo
import time
import CompletandoNos


def main():
    with open("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\ChavesEtAl_2012\\ChavesEtAl_2012\\GrupoA\\L1-1.txt", 'r') as f:
        tarefas, ferramentas, capacidade, matrix = opter.instancias(
            f)  # optendo todos os valores de instâncias recolhidas em um determinado arquivo

    jobs = np.arange(0, tarefas)  # conjunto de tarefas
    t = np.arange(0, ferramentas)  # conjunto de ferramentas
    print(capacidade)
    nos, chaves, cluster, S = reducao.Reducao_de_Dominio(matrix, tarefas, capacidade, ferramentas,
                                                         jobs, t)

    pares_ja_uilizados = []
    j = 0
    print(len(nos))
    print(len(chaves))
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


        while now - before < 5*60:
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

    print('Finalizado!')


if __name__ == '__main__':
    main()
