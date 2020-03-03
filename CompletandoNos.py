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
        j = 0
        p = 0
        cluster_intersseccoes = []
        chave = len(nos)

        if len(P) <= 200:
            while j <= round(len(P) * 0.10) and p < len(P):
                a = random.randint(0, len(P) - 1)
                for c in cluster:
                    if (set(rv.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [c])) &
                        (set(P[a]))) == set(rv.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [c])):
                        cluster_intersseccoes.append(c)

                if len(cluster_intersseccoes) >= 2:
                    for k in cluster_intersseccoes:
                        if (set(rv.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [k])) &
                            (set(P[a]))) == set(rv.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [k])):
                            if (rv.Calculando_a_Chave(P[a]) not in cluster[k]):
                                cluster[k].append(rv.Calculando_a_Chave(P[a]))
                                if rv.Calculando_a_Chave(P[a]) not in list(chaves.keys()):
                                    nos[chave] = P[a]
                                    chaves[rv.Calculando_a_Chave(P[a])] = []
                                    chaves[rv.Calculando_a_Chave(P[a])].append(chave)
                                    chave += 1
                                    j += 1
                    cluster_intersseccoes = []
                # else:
                #     for c in cluster:
                #         if (set(rv.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [c])) &
                #             (set(P[a]))) == set(rv.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [c])):
                #             if (rv.Calculando_a_Chave(P[a]) not in cluster[c]):
                #                 cluster[c].append(rv.Calculando_a_Chave(P[a]))
                #                 if a not in list(chaves.keys()):
                #                     nos[chave] = rv.Decodificando_Chave(P[a])
                #                     chaves[rv.Calculando_a_Chave(P[a])] = []
                #                     chaves[rv.Calculando_a_Chave(P[a])].append(chave)
                #                     chave += 1
                #                     j += 1
                p += 1

        else:
            #Definir o limite dinâmico da realimentação, para que o espaço de solução não exceda um tamanho acima de 2000 nos
            #( valor estipulado para fins de observação)

            while j < 20 and p < len(P):
                a = random.randint(0, len(P) - 1)
                for c in cluster:
                    if (set(rv.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [c])) &
                        (set(P[a]))) == set(rv.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [c])):
                        cluster_intersseccoes.append(c)

                if len(cluster_intersseccoes) >= 2:
                    for k in cluster_intersseccoes:
                        if (set(rv.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [k])) &
                            (set(P[a]))) == set(rv.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [k])):
                            if (rv.Calculando_a_Chave(P[a]) not in cluster[k]):
                                cluster[k].append(rv.Calculando_a_Chave(P[a]))
                                if rv.Calculando_a_Chave(P[a]) not in list(chaves.keys()):
                                    nos[chave] = P[a]
                                    chaves[rv.Calculando_a_Chave(P[a])] = []
                                    chaves[rv.Calculando_a_Chave(P[a])].append(chave)
                                    chave += 1
                                    j += 1
                    cluster_intersseccoes = []
                # else:
                #     for c in cluster:
                #         if (set(rv.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [c])) &
                #             (set(P[a]))) == set(rv.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [c])):
                #             if (rv.Calculando_a_Chave(P[a]) not in cluster[c]):
                #                 cluster[c].append(rv.Calculando_a_Chave(P[a]))
                #                 if a not in list(chaves.keys()):
                #                     nos[chave] = rv.Decodificando_Chave(P[a])
                #                     chaves[rv.Calculando_a_Chave(P[a])] = []
                #                     chaves[rv.Calculando_a_Chave(P[a])].append(chave)
                #                     chave += 1
                #                     j += 1
                p += 1
    return cluster, nos, chaves
