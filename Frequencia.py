import numpy as np
from operator import itemgetter
import Funcoes_Reversa as rv


class Frequencia(object):

    def __init__(self):

        self.__salva_nao_selecionados = []
        self.__salva_nao_selecionados_fitness = []
        self.__salva_selecionados = []
        self.__salva_selecionados_fitness = []
        self.__piores_fitness_nos = {}
        self.__piores_fitness_clusters = {}

    def Nao_selecionados(self, nao_selecionados, individuos_nos, individuos_fitness):
        for i in nao_selecionados:
            self.salva_nao_selecionados.append(individuos_nos[i])

        for i in nao_selecionados:
            self.salva_nao_selecionados_fitness.append(individuos_fitness[i])

    def Selecionados_Geracoes(self, selecionados, individuos_nos, individuos_fitness):
        for i in selecionados:
            self.salva_selecionados.append(individuos_nos[i])

        for i in selecionados:
            self.salva_selecionados_fitness.append(individuos_fitness[i])

    def Get_Nao_Selecionados(self):
        print('\n Nao selecionados : ')
        for i in self.salva_nao_selecionados:
            print(i)

    def Get_Nao_Selecionados_Fitness(self):
        print('\n Fitness dos nao selecionados atraves das geracoes : ')

        for i in self.salva_nao_selecionados_fitness:
            print(i)

    def Get_Selecionados(self):
        print('\nSelecionados atraves das geracoes : ')
        for i in self.__salva_selecionados:
            print(i)

    def Get_Selecionados_Fitness(self):
        print('\nFitness selecionados atraves das geracoes : ')
        for i in self.__salva_selecionados_fitness:
            print(i)

    def Calculando_Frequencia(self):
        frequencia_calculada = {}

        for i in range(len(self.__salva_nao_selecionados)):
            aux = self.__salva_nao_selecionados[i]
            for j in aux:
                if frequencia_calculada == {}:
                    frequencia_calculada[j] = 0
                else:
                    if j not in frequencia_calculada.keys():
                        frequencia_calculada[j] = 0

        for i in range(len(self.__salva_nao_selecionados) - 1):
            aux = self.__salva_nao_selecionados[i]
            for j in aux:
                if frequencia_calculada[j] == 0:
                    frequencia_calculada[j] = 1

                count = 0
                aux2 = self.__salva_nao_selecionados[i + 1]
                for l in aux2:
                    if l == j:
                        count += 1

                valor = frequencia_calculada[j] + count
                frequencia_calculada[j] = valor

        return frequencia_calculada

    def Piores_Fitness(self, individuos_fitness, individuos_nos, individuos_clusters):

        # Tupla do individuo com sua respectiva chave de individuo
        items = individuos_fitness.items()

        if self.__piores_fitness_nos == {}:
            # Definindo a metade dos individuos com os piores fitness
            # Individuos organizados por ordem decrescente
            aux = sorted(items, key=itemgetter(1), reverse=True)
            for i in range(int((len(aux)) / 2)):
                # A chave é o fitness da sequencia de nos em questão e o valor e o cluster e ou no.

                if aux[i][1] in list(self.__piores_fitness_nos.keys()):
                    self.__piores_fitness_nos[aux[i][1]].append(individuos_nos[aux[i][0]])
                    self.__piores_fitness_clusters[aux[i][1]].append(individuos_clusters[aux[i][0]])
                else:
                    self.__piores_fitness_nos[aux[i][1]] = []
                    self.__piores_fitness_clusters[aux[i][1]] = []
                    self.__piores_fitness_nos[aux[i][1]].append(individuos_nos[aux[i][0]])
                    self.__piores_fitness_clusters[aux[i][1]].append(individuos_clusters[aux[i][0]])



        else:
            tamanho_fixo = len(self.__piores_fitness_clusters)
            aux = sorted(items, key=itemgetter(1), reverse=True)
            aux2 = []

            for i in range(int(len(aux) / 2)):
                aux2.append(aux[i][1])

            piores_fitness_anterior = set(self.__piores_fitness_nos.keys())
            piores_fitness_anterior = list(piores_fitness_anterior)

            for i in range(len(aux)):
                if aux[i][1] in set(aux2):
                    if aux[i][1] in set(self.__piores_fitness_nos.keys()):
                        self.__piores_fitness_nos[aux[i][1]].append(individuos_nos[aux[i][0]])
                        self.__piores_fitness_clusters[aux[i][1]].append(individuos_clusters[aux[i][0]])
                    else:
                        self.__piores_fitness_nos[aux[i][1]] = []
                        self.__piores_fitness_clusters[aux[i][1]] = []
                        self.__piores_fitness_nos[aux[i][1]].append(individuos_nos[aux[i][0]])
                        self.__piores_fitness_clusters[aux[i][1]].append(individuos_clusters[aux[i][0]])

            piores_fitness_atuais = list(set(self.__piores_fitness_nos.keys()))

            # Definindo novo limite inferior
            for i in piores_fitness_atuais:
                if (min(piores_fitness_anterior) > i) and (i not in piores_fitness_anterior):
                    del self.__piores_fitness_nos[i]
                    del self.__piores_fitness_clusters[i]

            if len(self.__piores_fitness_clusters) > tamanho_fixo:
                keys = list(self.__piores_fitness_clusters.keys())
                keys.sort(reverse=True)
                chaves_finais = []
                for i in keys:
                    if len(chaves_finais) < tamanho_fixo:
                        chaves_finais.append(i)

                anterior = list(self.__piores_fitness_clusters)

                for i in anterior:
                    if i not in chaves_finais:
                        del self.__piores_fitness_nos[i]
                        del self.__piores_fitness_clusters[i]

    # Matriz de frequencia de pares dos piores nos:
    def Matriz_de_Frequencia(self, tamanho_dos_nos, nos):
        matriz_de_frequencia = np.zeros((tamanho_dos_nos, tamanho_dos_nos))
        for fitness in self.__piores_fitness_nos:
            for sequencia in self.__piores_fitness_nos[fitness]:
                for i in range(len(sequencia) - 1):
                    matriz_de_frequencia[sequencia[i], sequencia[i + 1]] = matriz_de_frequencia[
                                                                               sequencia[i], sequencia[i + 1]] + 1

        return matriz_de_frequencia

    def Matriz_de_Frequencia_Cluster(self, cluster):
        matriz_de_frequencia_cluster = np.zeros((len(cluster), len(cluster)))
        for fitness in self.__piores_fitness_clusters:
            for sequencia in self.__piores_fitness_clusters[fitness]:
                for i in range(len(sequencia) - 1):
                    matriz_de_frequencia_cluster[sequencia[i], sequencia[i + 1]] = matriz_de_frequencia_cluster[
                                                                                       sequencia[i], sequencia[
                                                                                           i + 1]] + 1

        return matriz_de_frequencia_cluster

    def Clusters_Piores(self, matriz_final, cluster, matrix, capacidade, ferramentas, pares_ja_utilizados):

        maior = matriz_final[0][0]
        for i in range(len(cluster)):
            for j in range(len(cluster)):
                if matriz_final[i][j] >= maior and len(
                        rv.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [i])) != capacidade \
                        and len(rv.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [j])) != capacidade:
                    if pares_ja_utilizados != []:
                        if str([i, j]) != str([pares_ja_utilizados[0], pares_ja_utilizados[1]]):
                            maior = matriz_final[i][j]
                            pares_clusters = []
                            pares_clusters.append(i)
                            pares_clusters.append(j)
                    else:
                        maior = matriz_final[i][j]
                        pares_clusters = []
                        pares_clusters.append(i)
                        pares_clusters.append(j)

        return pares_clusters
