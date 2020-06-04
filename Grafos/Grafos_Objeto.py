import numpy as np
import Funcoes_Reversa as rv


class Grafos(object):

    def __init__(self, nos, cluster, chaves):
        self.__nos = nos  # Sequencia de ferramentas possiveis para execuçao de uma possivel tarefa
        self.__cluster = cluster  # As chaves dos dicionarios representam os clusters(tarefas), na qual o conteudo de cada
        # chave contém uma lista de valores que representam um sequência
        self.__chaves = chaves  # A chave do dicionario representa a soma dos quadrados dos elementos de um no, na qual
        # o conteudo respectivo esta chave é este no.

    def Elementos(self):

        print("Nos", self.__nos)
        print("Cluster", self.__cluster)
        print("Chaves", self.__chaves)

    # Determinando as arestas e os pesos das mesmas, na qual os pesos das mesmas configura o numero de trocas
    # de uma sequencia de ferramente a outra(Grafo Completo)
    def Matriz_Adjacencia(self):
        aux = []
        concatenado = np.array([])
        key = self.__nos.keys()

        for i in range(len(self.__nos)):
            for j in range(len(self.__nos)):
                if i == j:
                    aux.append(0)
                else:
                    if j in list(key) and i in list(key):
                        aux.append(rv.Distance1(self.__nos[i], self.__nos[j]))

            concatenado = np.concatenate((concatenado, aux))
            aux = []

        arestas = np.reshape(concatenado, (len(self.__nos), len(self.__nos)))

        return arestas

    # Definindo os clusters que fazem intersecção, de acordo com os nos presentes entre os clusters
    def Inteseccao(self):
        interseccao = {}
        for i in self.__chaves:
            if i not in list(interseccao.keys()):
                interseccao[i] = []
                for j in list(self.__cluster.keys()):
                    if i in self.__cluster[j]:
                        interseccao[i].append(j)
            else:
                for j in list(self.__cluster.keys()):
                    if i in self.__cluster[j]:
                        interseccao[i].append(j)

        return interseccao

    def Cluster(self):
        cluster = self.__cluster
        return cluster

    def Nos(self):
        nos = self.__nos
        return nos

    def Chaves(self):
        chaves = self.__chaves
        return chaves

