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
    taxa_de_cruzamento = 0.7
    taxa_de_mutacao = 0.1
    tamanho_da_populacao = 150
    taxa_de_crescimento = 0.5
    taxa_de_selecao = 0.97
    while j < 5:
        genetico = gene.Genetico(nos, cluster, chaves)

        # Definindo a populacao inicial de clusters
        genetico.Populacao_Inicial(tamanho_da_populacao=tamanho_da_populacao)

        # Definindo os possiveis cromossomos clusters

        possiveis_cromossomos = genetico.Possiveis_Cromossomos_Inciais()
        before = time.time()
        now = before

        while now - before < 5 * 60:
            print(now-before)
            if now - before == 0:
                genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
                genetico.Individuos_Cluster()
                genetico.Individuos_Nos()

            else:
                possiveis_cromossomos = genetico.Possiveis_Cromossomos_Entre_Geracoes()
                genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
                genetico.Individuos_Nos()

            menor_troca, tempo_do_menor = genetico.Fitness(before)
            genetico.Selecao(taxa_de_selecao=taxa_de_selecao)
            genetico.CrossOver(taxa_de_cruzamento=taxa_de_cruzamento)
            genetico.Mutation_Swap(taxa_de_mutação=taxa_de_mutacao)
            menor.append(menor_troca)
            tempo.append(round(tempo_do_menor, 2))
            now = time.time()

        frequencia = genetico.GetFrequencia()

        pares = frequencia.Clusters_Piores(frequencia.Matriz_de_Frequencia_Cluster(cluster), cluster, matrix,
                                           capacidade,
                                           ferramentas, pares_ja_uilizados)

        nos, chaves, cluster = CompletandoNos.aumentando_a_quantidade_de_nos(
            pares_clusters=pares, cluster=cluster,
            nos=nos, chaves=chaves, matrix=matrix,
            ferramentas=ferramentas, capacidade=capacidade,tamanho_de_nos_antigo=quantidade_de_nos,taxa_de_crescimento=taxa_de_crescimento)

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
