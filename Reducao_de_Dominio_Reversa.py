from itertools import combinations as inter
import Funcoes_Reversa as revers
import random


def Reducao_de_Dominio(matrix, tarefas, capacidade, ferramentas, jobs, t):
    S = revers.CrucialJobs_EstrategiaReversa(matrix, tarefas, capacidade, ferramentas, jobs)

    # Fill Nodes
    Z, Q = revers.FillNode(matrix, ferramentas, capacidade, tarefas, S)
    # Q é o conjunto de nos gerados
    cluster = {}
    nos_do_cluster = {}
    chaves_dos_nos = {}
    P = []
    E = []
    nos_do_cluster, chaves_dos_nos, cluster = revers.Uptade(ferramentas, matrix,
                                                            cluster,
                                                            Q, nos_do_cluster,
                                                            chaves_dos_nos,
                                                            tarefas,
                                                            P,E)  # o conjunto de clusters que possuem ao menos um nó

    cheios = []
    for i in cluster:
        if cluster[i] != []:
            cheios.append(i)

    if len(cheios) == tarefas:
        return nos_do_cluster, chaves_dos_nos, cluster,S

    else:
        U = set(jobs) - set(cheios)  # conjunto de tarefas
        for h in range(1, capacidade + 1):

            for z in Z:
                E = []
                for u in U:
                    # conjunto de tarefas

                    if revers.Distance1(z, revers.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [u])) == h:
                        E.append(u)

                if E:
                    E = set(E)
                    for e in E:
                        if len(revers.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [e])) == capacidade:
                            P.append(list(revers.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [e])))
                        else:
                            aux = revers.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [e])
                            tools = revers.ferramentas_que_nao_estao_na_tarefa(z, [e], matrix, ferramentas)

                            combinacoes = list(inter(tools, capacidade - len(aux)))
                            if len(combinacoes) < 100:
                                for c in combinacoes:
                                    aux2 = list(c)
                                    if aux + aux2 not in Q:
                                        P.append(aux + aux2)
                            else:
                                o = 0
                                indice = list(range(0,len(combinacoes)))
                                random.shuffle(indice)
                                while o < 150 and o < len(combinacoes):
                                    aux2 = list(combinacoes[indice[o]])
                                    if aux + aux2 not in Q:
                                        P.append(aux + aux2)
                                        o+=1

        if P:
            nos_do_cluster, chaves_dos_nos, cluster = revers.Uptade(ferramentas, matrix,
                                                                    cluster,
                                                                    Q, nos_do_cluster,
                                                                    chaves_dos_nos,
                                                                    tarefas,
                                                                    P,E)  # o conjunto de clusters que possuem ao menos um nó





        return nos_do_cluster, chaves_dos_nos, cluster,S
