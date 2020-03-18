import numpy as np
import Reducao_de_Dominio_Reversa as reducao


def Running_Estrategia_Reversa(tarefas, ferramentas, matrix, capacidade):
    jobs = np.arange(0, tarefas)  # conjunto de tarefas
    t = np.arange(0, ferramentas)  # conjunto de ferramentas
    # print('Conjunto de tarefas ', jobs)
    # print('Conjunto de ferramentas: ', t)

    nos, chaves, cluster = reducao.Reducao_de_Dominio(matrix, tarefas, capacidade, ferramentas,
                                                      jobs, t)

    return len(nos), nos, chaves, cluster
