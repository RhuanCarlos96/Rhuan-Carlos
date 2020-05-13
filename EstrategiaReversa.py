# import FuncaoLeitura as opter
# import numpy as np
# import Reducao_de_Dominio_Reversa as reducao
# import AlgoritmoGenetico as gene
# import Lendo_Arquivos as arquivo
# import time
# import CompletandoNos
# import argparse
# import sys
# import logging

import Instancias

# def main(POP,CXPB,MUTPB,DATFILE,CRESC,SEL):
#     with open(
#             "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\ChavesEtAl_2012\\ChavesEtAl_2012\\GrupoA\\L18-7.txt",
#             'r') as f:
#         tarefas, ferramentas, capacidade, matrix = opter.instancias(
#             f)  # optendo todos os valores de instâncias recolhidas em um determinado arquivo
#
#     jobs = np.arange(0, tarefas)  # conjunto de tarefas
#     t = np.arange(0, ferramentas)  # conjunto de ferramentas
#     nos, chaves, cluster, S = reducao.Reducao_de_Dominio(matrix, tarefas, capacidade, ferramentas,
#                                                          jobs, t)
#
#     pares_ja_uilizados = []
#     j = 0
#     print(len(nos))
#     print(len(chaves))
#     quantidade_de_nos = len(nos)
#     #print('Executando')
#     menor = []
#     tempo = []
#
#     while j < 5:
#         genetico = gene.Genetico(nos, cluster, chaves)
#
#         # Definindo a populacao inicial de clusters
#         genetico.Populacao_Inicial(tamanho_da_populacao=POP)
#
#         # Definindo os possiveis cromossomos clusters
#
#         possiveis_cromossomos = genetico.Possiveis_Cromossomos_Inciais()
#         before = time.time()
#         now = before
#
#         while now - before < 30:
#             print(now-before)
#             if now - before == 0:
#                 genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
#                 genetico.Individuos_Cluster()
#                 genetico.Individuos_Nos()
#
#             else:
#                 possiveis_cromossomos = genetico.Possiveis_Cromossomos_Entre_Geracoes()
#                 genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
#                 genetico.Individuos_Nos()
#
#             menor_troca, tempo_do_menor = genetico.Fitness(before)
#             genetico.Selecao(taxa_de_selecao=SEL)
#             genetico.CrossOver(taxa_de_cruzamento=CXPB)
#             genetico.Mutation_Swap(taxa_de_mutação=MUTPB)
#             menor.append(menor_troca)
#             tempo.append(round(tempo_do_menor, 2))
#             now = time.time()
#
#         frequencia = genetico.GetFrequencia()
#
#         pares = frequencia.Clusters_Piores(frequencia.Matriz_de_Frequencia_Cluster(cluster), cluster, matrix,
#                                            capacidade,
#                                            ferramentas, pares_ja_uilizados)
#
#         nos, chaves, cluster = CompletandoNos.aumentando_a_quantidade_de_nos(
#             pares_clusters=pares, cluster=cluster,
#             nos=nos, chaves=chaves, matrix=matrix,
#             ferramentas=ferramentas, capacidade=capacidade,tamanho_de_nos_antigo=quantidade_de_nos,taxa_de_crescimento=CRESC)
#
#         j += 1
#
#         # print('Rodando de novo')
#
#     fila = np.argsort(menor)
#     # save the fo values in DATFILE
#     with open(DATFILE, 'w') as f:
#         f.write(str(menor[fila[0]]))
#
#     # print('Finalizado!')
#
#
# if __name__ == '__main__':
#     # just check if args are ok
#     with open('args.txt', 'w') as f:
#         f.write(str(sys.argv))
#
#     # loading example arguments
#     ap = argparse.ArgumentParser(description='Feature Selection using GA to TSP problem')
#     ap.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
#     # 5 args to test values
#     ap.add_argument('--pop', dest='pop', type=int, required=True, help='Population size')
#     ap.add_argument('--cros', dest='cros', type=float, required=True, help='Crossover probability')
#     ap.add_argument('--mut', dest='mut', type=float, required=True, help='Mutation probability')
#     ap.add_argument('--cresc', dest='crescimento', type=float, required=True, help='Crescimento da populacao')
#     ap.add_argument('--selec', dest='selection', type=float, required=True, help='Taxa de selecao')
#
#
#     # 1 arg file name to save and load fo value
#     ap.add_argument('--datfile', dest='datfile', type=str, required=True,
#                     help='File where it will be save the score (result)')
#
#     args = ap.parse_args()
#     logging.debug(args)
#     # call main function passing args
#     main(args.pop, args.cros, args.mut, args.datfile, args.crescimento, args.selection)

Instancias.Lendo_Instancias()
print('saiuaaaa')