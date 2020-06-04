# import FuncaoLeitura as opter
# import numpy as np
# import Reducao_de_Dominio_Reversa as reducao
# import AlgoritmoGenetico as gene
# import statistics
# import time
# import CompletandoNos
# import argparse
# import sys
# import logging
# import os
#import Instancias
import Lendo_Arquivos
#Instancias.geradndo_arquivo_de_resultados()

print('entrei')
Lendo_Arquivos.Lendo_Arquivos()
print('saiu')
# def main(POP, CXPB, MUTPB, DATFILE, SEL):
#     valores = []
#     for root, dirs, files in os.walk("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instancias_para_ajustes"):
#         for name in files:
#             with open(os.path.join(root, name), 'r') as f:
#                 tarefas, ferramentas, capacidade, matrix = opter.instancias(
#                     f)  # optendo todos os valores de instâncias recolhidas em um determinado arquivo
#
#             jobs = np.arange(0, tarefas)  # conjunto de tarefas
#             t = np.arange(0, ferramentas)  # conjunto de ferramentas
#             nos, chaves, cluster, S = reducao.Reducao_de_Dominio(matrix, tarefas, capacidade, ferramentas,
#                                                                  jobs, t)
#
#             pares_ja_uilizados = []
#             j = 0
#             menor = []
#             tempo = []
#
#             while j < 2:
#                 genetico = gene.Genetico(nos, cluster, chaves)
#
#                 # Definindo a populacao inicial de clusters
#                 genetico.Populacao_Inicial(tamanho_da_populacao=POP)
#
#                 # Definindo os possiveis cromossomos clusters
#
#                 possiveis_cromossomos = genetico.Possiveis_Cromossomos_Inciais()
#                 before = time.time()
#                 now = before
#
#                 while now - before < 10 * 60:
#                     print(now - before)
#                     if now - before == 0:
#                         genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
#                         genetico.Individuos_Cluster()
#                         genetico.Individuos_Nos()
#
#                     else:
#                         possiveis_cromossomos = genetico.Possiveis_Cromossomos_Entre_Geracoes()
#                         genetico.Tratando_os_Cromossomos(prossiveis_cromossomos_nos=possiveis_cromossomos)
#                         genetico.Individuos_Nos()
#
#                     menor_troca, tempo_do_menor = genetico.Fitness(before)
#                     genetico.Selecao(taxa_de_selecao=SEL)
#                     genetico.CrossOver(taxa_de_cruzamento=CXPB)
#                     genetico.Mutation_Swap(taxa_de_mutação=MUTPB)
#                     menor.append(menor_troca)
#                     tempo.append(round(tempo_do_menor, 2))
#                     now = time.time()
#
#                 frequencia = genetico.GetFrequencia()
#
#                 pares = frequencia.Clusters_Piores(frequencia.Matriz_de_Frequencia_Cluster(cluster), cluster, matrix,
#                                                    capacidade,
#                                                    ferramentas, pares_ja_uilizados)
#
#                 pares_ja_uilizados = pares
#
#                 conjunto_de_nos_isolados = CompletandoNos.nos_isolados(cluster=cluster, grafo=genetico.GetGrafo())
#
#                 conjunto_de_nos_nao_isolados = CompletandoNos.nos_nao_isolados(cluster=cluster,
#                                                                                grafo=genetico.GetGrafo())
#
#                 nos, chaves, cluster = CompletandoNos.Completando_Clusters_Eliminando_Indiviais(pares_clusters=pares,
#                                                                                                 cluster=cluster,
#                                                                                                 nos=nos, chaves=chaves,
#                                                                                                 matrix=matrix,
#                                                                                                 ferramentas=ferramentas,
#                                                                                                 capacidade=capacidade,
#                                                                                                 tarefas=tarefas,
#                                                                                                 conjunto_de_nos_isolados=conjunto_de_nos_isolados,
#                                                                                                 conjunto_de_nos_nao_isolados=conjunto_de_nos_nao_isolados)
#                 j += 1
#
#                 # print('Rodando de novo')
#
#             fila = np.argsort(menor)
#             valores.append(menor[fila[0]])
#             # save the fo values in DATFILE
#     with open(DATFILE, 'w') as f:
#         f.write(str(round(statistics.mean(valores))))
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
#     # 4 args to test values
#     ap.add_argument('--pop', dest='pop', type=int, required=True, help='Population')
#     ap.add_argument('--cros', dest='cros', type=float, required=True, help='Crossover probability')
#     ap.add_argument('--mut', dest='mut', type=float, required=True, help='Mutation probability')
#     ap.add_argument('--selec', dest='selection', type=float, required=True, help='Taxa de selecao')
#
#     # 1 arg file name to save and load fo value
#     ap.add_argument('--datfile', dest='datfile', type=str, required=True,
#                     help='File where it will be save the score (result)')
#
#     args = ap.parse_args()
#     logging.debug(args)
#     # call main function passing args
#     main(args.pop, args.cros, args.mut, args.datfile, args.selection)
