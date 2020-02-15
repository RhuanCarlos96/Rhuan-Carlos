import numpy as np
from operator import itemgetter
import Funcoes_Reversa as rv


class Frequencia(object):

    def __init__(self):

        self.salva_nao_selecionados = []
        self.salva_nao_selecionados_fitness = []
        self.salva_selecionados = []
        self.salva_selecionados_fitness = []
        self.piores_fitness_nos = {}
        self.piores_fitness_clusters = {}

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
        for i in self.salva_selecionados:
            print(i)

    def Get_Selecionados_Fitness(self):
        print('\nFitness selecionados atraves das geracoes : ')
        for i in self.salva_selecionados_fitness:
            print(i)

    def Calculando_Frequencia(self):
        frequencia_calculada = {}

        for i in range(len(self.salva_nao_selecionados)):
            aux = self.salva_nao_selecionados[i]
            for j in aux:
                if frequencia_calculada == {}:
                    frequencia_calculada[j] = 0
                else:
                    if j not in frequencia_calculada.keys():
                        frequencia_calculada[j] = 0

        aux = []
        aux2 = []
        for i in range(len(self.salva_nao_selecionados) - 1):
            aux = self.salva_nao_selecionados[i]
            for j in aux:
                if frequencia_calculada[j] == 0:
                    frequencia_calculada[j] = 1

                count = 0
                aux2 = self.salva_nao_selecionados[i + 1]
                for l in aux2:
                    if l == j:
                        count += 1

                valor = frequencia_calculada[j] + count
                frequencia_calculada[j] = valor

        return frequencia_calculada

    def Piores_Fitness(self, individuos_fitness, individuos_nos, individuos_clusters):

        items = individuos_fitness.items()

        aux = []

        if self.piores_fitness_nos == {}:

            # Definindo a metade dos individuos com os piores fitness
            aux = sorted(items, key=itemgetter(1), reverse=True)

            for i in range(int((len(aux)) / 2)):
                # A chave e o fitness da sequencia de nos em questão
                if self.piores_fitness_nos == {}:
                    self.piores_fitness_nos[aux[i][1]] = []
                    self.piores_fitness_clusters[aux[i][1]] = []
                    self.piores_fitness_nos[aux[i][1]].append(individuos_nos[aux[i][0]])
                    self.piores_fitness_clusters[aux[i][1]].append(individuos_clusters[aux[i][0]])
                else:
                    if aux[i][1] in list(self.piores_fitness_nos.keys()):
                        self.piores_fitness_nos[aux[i][1]].append(individuos_nos[aux[i][0]])
                        self.piores_fitness_clusters[aux[i][1]].append(individuos_clusters[aux[i][0]])
                    else:
                        self.piores_fitness_nos[aux[i][1]] = []
                        self.piores_fitness_clusters[aux[i][1]] = []
                        self.piores_fitness_nos[aux[i][1]].append(individuos_nos[aux[i][0]])
                        self.piores_fitness_clusters[aux[i][1]].append(individuos_clusters[aux[i][0]])



        else:
            aux = sorted(items, key=itemgetter(1), reverse=True)
            aux2 = []

            for i in range(int(len(aux) / 2)):
                aux2.append(aux[i][1])

            piores_fitness_anterior = set(self.piores_fitness_nos.keys())
            piores_fitness_anterior = list(piores_fitness_anterior)

            for i in range(len(aux)):
                if aux[i][1] in set(aux2):
                    if aux[i][1] in set(self.piores_fitness_nos.keys()):
                        self.piores_fitness_nos[aux[i][1]].append(individuos_nos[aux[i][0]])
                        self.piores_fitness_clusters[aux[i][1]].append(individuos_clusters[aux[i][0]])
                    else:
                        self.piores_fitness_nos[aux[i][1]] = []
                        self.piores_fitness_clusters[aux[i][1]] = []
                        self.piores_fitness_nos[aux[i][1]].append(individuos_nos[aux[i][0]])
                        self.piores_fitness_clusters[aux[i][1]].append(individuos_clusters[aux[i][0]])

            piores_fitness_atuais = list(set(self.piores_fitness_nos.keys()))

            # Definindo novo limite inferior
            for i in piores_fitness_atuais:
                if (min(piores_fitness_anterior) > i) and (i not in piores_fitness_anterior):
                    del self.piores_fitness_nos[i]
                    del self.piores_fitness_clusters[i]

            piores_fitness_atuais = list(set(self.piores_fitness_nos))
            count = 0
            piores = set(piores_fitness_atuais)
            diferenca = set(piores_fitness_atuais) - set(piores_fitness_anterior)
            if diferenca:
                if min(diferenca) > min(piores_fitness_anterior):
                    for i in diferenca:
                        if (i != max(piores_fitness_atuais)) and (i <= 18):
                            for j in piores_fitness_anterior:
                                if (i > j) and (i not in piores_fitness_anterior) and (j == min(piores)):
                                    del self.piores_fitness_nos[j]
                                    del self.piores_fitness_clusters[j]
                                    piores = set(self.piores_fitness_nos)


    # Matriz de frequencia de pares dos piores nos:
    def Matriz_de_Frequencia(self, tamanho_dos_nos, nos):
        matriz_de_frequencia = np.zeros((tamanho_dos_nos, tamanho_dos_nos))
        for fitness in self.piores_fitness_nos:
            for sequencia in self.piores_fitness_nos[fitness]:
                for i in range(len(sequencia) - 1):
                    matriz_de_frequencia[sequencia[i], sequencia[i + 1]] = matriz_de_frequencia[
                                                                               sequencia[i], sequencia[i + 1]] + 1

        return matriz_de_frequencia

    def Matriz_de_Frequencia_Cluster(self, cluster):
        matriz_de_frequencia_cluster = np.zeros((len(cluster), len(cluster)))
        for fitness in self.piores_fitness_clusters:
            for sequencia in self.piores_fitness_clusters[fitness]:
                for i in range(len(sequencia) - 1):
                    matriz_de_frequencia_cluster[sequencia[i], sequencia[i + 1]] = matriz_de_frequencia_cluster[
                                                                                       sequencia[i], sequencia[
                                                                                           i + 1]] + 1

        return matriz_de_frequencia_cluster

    def Clusters_Piores(self, matriz_final, cluster, matrix, capacidade, ferramentas):

        # Determinar quais cluster os pares  de nos com mais frequência em cada coluna que noa possui  C capacidade:
        S = rv.tarefas_com_c_requerimentos(matrix=matrix, tarefas=len(list(cluster.keys())) - 1, capacidade=capacidade,
                                           ferramentas=ferramentas)

        if S == []:
            S = rv.tarefas_com_maior_requerimento(matrix=matrix, tarefas=len(list(cluster.keys())),
                                                  capacidade=capacidade, ferramentas=ferramentas)

        maior = np.where(matriz_final == np.amax(matriz_final))

        listOfCordinates = list(zip(maior[0], maior[1]))

        clusters_a_serem_prenchidos = []

        for cord in listOfCordinates:
            if cord[0] not in S and cord[0] not in clusters_a_serem_prenchidos:
                clusters_a_serem_prenchidos.append(cord[0])

            if cord[1] not in S and cord[1] not in clusters_a_serem_prenchidos:
                clusters_a_serem_prenchidos.append(cord[1])

        while clusters_a_serem_prenchidos == []:
            for cord in listOfCordinates:
                matriz_final[cord[0], cord[1]] = 0

            maior = np.where(matriz_final == np.amax(matriz_final))

            listOfCordinates = list(zip(maior[0], maior[1]))

            for cord in listOfCordinates:
                if cord[0] not in S and cord[0] not in clusters_a_serem_prenchidos:
                    clusters_a_serem_prenchidos.append(cord[0])

                if cord[1] not in S and cord[1] not in clusters_a_serem_prenchidos:
                    clusters_a_serem_prenchidos.append(cord[1])

        return clusters_a_serem_prenchidos
