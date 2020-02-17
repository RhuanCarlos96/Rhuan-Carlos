from itertools import combinations as inter
import Funcoes_Reversa as revers


def Elimina_Repetidos(Q):
    novo = []

    for j in Q:
        novo.append(j)

    Q = []

    for i in novo:
        if i not in Q:
            Q.append(i)

    Q_novo = []

    for j in Q:
        Q_novo.append(list(j))

    return Q


def Reducao_de_Dominio(matrix, tarefas, capacidade, ferramentas, jobs, t):
    S = revers.CrucialJobs_EstrategiaReversa(matrix, tarefas, capacidade, ferramentas, jobs)

    # Fill Nodes
    Z, Q = revers.FillNode(matrix, ferramentas, capacidade, tarefas, S)

    # Q é o conjunto de nos gerados

    cluster = {}
    nos_do_cluster = {}
    chaves_dos_nos = {}
    P = []

    from time import time
    now = time()
    nos_do_cluster, chaves_dos_nos, cluster = revers.Uptade(S, ferramentas, matrix,
                                                            cluster,
                                                            Q, nos_do_cluster,
                                                            chaves_dos_nos,
                                                            tarefas,
                                                            P)  # o conjunto de clusters que possuem ao menos um nó
    print("tempo de execucao:   ",time() - now)

    cheios = []
    for i in cluster:
        if cluster[i] != []:
            cheios.append(i)

    if len(cheios) == tarefas:
        return nos_do_cluster, chaves_dos_nos, cluster

    else:
        U = set(jobs) - set(cheios)  # conjunto de tarefas
        for h in range(1, capacidade + 1):

            for z in Z:
                for u in U:
                    E = []  # conjunto de tarefas
                    A = revers.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [u])  # Conjunto de ferramentas
                    # requeridas pela tarefa u

                    if revers.Distance1(z, A) == h:
                        E.append(u)

                    if E:
                        for e in E:
                            if e not in S:
                                S.append(e)

                            if len(revers.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [e])) == capacidade:

                                P.append(list(revers.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [e])))

                            else:
                                aux = revers.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [e])
                                tools = revers.ferramentas_que_nao_estao_na_tarefa(z, [e], matrix, ferramentas)

                                combinacoes = list(inter(tools, capacidade - len(aux)))

                                for c in combinacoes:
                                    aux2 = list(c)
                                    P.append(aux + aux2)

        print('Numero de nos ate entao gerados', len(Q))
        P = Elimina_Repetidos(P)
        print('Numero maximo a serem gerados ', len(P))
        nos_do_cluster, chaves_dos_nos, cluster = revers.Uptade(S, ferramentas, matrix,
                                                                cluster,
                                                                Q, nos_do_cluster,
                                                                chaves_dos_nos,
                                                                tarefas,
                                                                P)  # o conjunto de clusters que possuem ao menos um nó

        return nos_do_cluster, chaves_dos_nos, cluster
