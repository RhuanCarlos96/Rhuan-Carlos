import FuncaoLeitura as opter
import numpy as np
import Reducao_de_Dominio_Reversa as reducao
import AlgoritmoGenetico as gene
import Lendo_Arquivos as arquivo
import time
import CompletandoNos


def main():
    with open(
            "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\ChavesEtAl_2012\\ChavesEtAl_2012\\GrupoA\\L18-7.txt",
            'r') as f:
        tarefas, ferramentas, capacidade, matrix = opter.instancias(
            f)  # optendo todos os valores de instâncias recolhidas em um determinado arquivo

    jobs = np.arange(0, tarefas)  # conjunto de tarefas
    t = np.arange(0, ferramentas)  # conjunto de ferramentas
    nos, chaves, cluster, S = reducao.Reducao_de_Dominio(matrix, tarefas, capacidade, ferramentas,
                                                         jobs, t)

    pares_ja_uilizados = []
    j = 0
    print(len(nos))
    print(len(chaves))
    quantidade_de_nos = len(nos)
    print('Executando')
    menor = []
    tempo = []
    while j < 5:
        genetico = gene.Genetico(nos, cluster, chaves)

        # Definindo a populacao inicial de clusters
        genetico.Populacao_Inicial()

        # Definindo os possiveis cromossomos clusters

        possiveis_cromossomos = genetico.Possiveis_Cromossomos_Inciais()
        k = 0
        before = time.time()
        now = before

        while now - before < 10 * 60:
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
            tempo.append(round(tempo_do_menor, 2))
            now = time.time()
            k += 1

        frequencia = genetico.GetFrequencia()

        pares = frequencia.Clusters_Piores(frequencia.Matriz_de_Frequencia_Cluster(cluster), cluster, matrix,
                                           capacidade,
                                           ferramentas, pares_ja_uilizados)

        nos, chaves, cluster = CompletandoNos.aumentando_a_quantidade_de_nos(
            pares_clusters=pares, cluster=cluster,
            nos=nos, chaves=chaves, matrix=matrix,
            ferramentas=ferramentas, capacidade=capacidade,tamanho_de_nos_antigo=quantidade_de_nos)

        j += 1

        print('Rodando de novo')

    print(menor)
    print(tempo)
    fila = np.argsort(menor)
    print(menor[fila[0]])
    print(round(tempo[fila[0]],2))

    print('Finalizado!')


if __name__ == '__main__':
    main()
