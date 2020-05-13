import Verifcar
import os
import FuncaoLeitura as opter
import Reducao_de_Dominio_Reversa as reducao
import numpy as np
from Grafos import Grafos_Objeto


# Abrindo arquivos para teste:

def Lendo_Instancias():
    with open(
            "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instances\\Catanzaro\\Tabela3\\datD10",
            'r') as f:
        tarefas, ferramentas, capacidade, matrix = opter.instancias(
            f)  # optendo todos os valores de instâncias recolhidas em um determinado arquivo

    jobs = np.arange(0, tarefas)  # conjunto de tarefas
    t = np.arange(0, ferramentas)  # conjunto de ferramentas
    print(tarefas)
    print(capacidade)
    nos, chaves, cluster, S = reducao.Reducao_de_Dominio(matrix, tarefas, capacidade, ferramentas,
                                                         jobs, t)

    grafo = Grafos_Objeto.Grafos(nos, cluster, chaves)

    print(len(nos))
    print(len(chaves))
    print('S :')
    for s in cluster:
        print(s, " : ", len(cluster[s]))
        print()

