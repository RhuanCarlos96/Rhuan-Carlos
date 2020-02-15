import Funcoes_Reversa as rv
import itertools as inter
import random


def CompletandoNos(conjunto_de_tarefas, cluster, matrix, capacidade, tools, ferramentas, nos, chaves):
    for tarefa in conjunto_de_tarefas:
        P = []
        ferramentas_requeridas = set(rv.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [tarefa]))
        combinacoes = list(
            inter.combinations(list(set(tools) - ferramentas_requeridas), capacidade - len(ferramentas_requeridas)))

        for c in combinacoes:
            aux = set(c)
            P.append(list(ferramentas_requeridas.union(aux)))

        k = len(nos)
        j = 0
        Q = []
        p = 0

        while j < round(len(P) * 0.30) and p < len(P):
            a = random.randint(0, len(P) - 1)
            if rv.Calculando_a_Chave(P[a]) not in list(chaves.keys()):
                nos[k + j] = P[a]
                chaves[rv.Calculando_a_Chave(P[a])] = []
                chaves[rv.Calculando_a_Chave(P[a])].append(k + j)
                j += 1
                Q.append(P[a])
            else:
                p += 1

        for q in Q:
            for s in cluster:
                if len(set(rv.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [s])) &
                       (set(q))) == len(set(rv.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [s]))):
                    if rv.Calculando_a_Chave(q) not in cluster[s]:
                        cluster[s].append(rv.Calculando_a_Chave(q))

    return cluster, nos, chaves
