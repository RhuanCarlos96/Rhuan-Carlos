import Executando_Estrategia_Reversa
import Executando_Genetico
import numpy
import statistics


def Execucao(tarefas, ferramentas, matrix, capacidade):
    tamanho, nos, chaves, cluster = Executando_Estrategia_Reversa.Running_Estrategia_Reversa(tarefas, ferramentas,
                                                                                             matrix, capacidade)

    melhor_solucao = []
    melhor_tempo = []

    for i in range(2):
        menor, tempo = Executando_Genetico.Running_Genetic(nos=nos, cluster=cluster, chaves=chaves)
        melhor_solucao.append(menor)
        melhor_tempo.append(tempo)

    organizado = numpy.argsort(melhor_solucao)

    return tamanho, melhor_solucao[organizado[0]], round(melhor_tempo[organizado[0]],2), round(statistics.mean(
        melhor_solucao), 3), round(statistics.pstdev(melhor_solucao), 3), round(statistics.mean(melhor_tempo), 3)