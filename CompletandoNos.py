import itertools
import random

import numpy

import Funcoes_Reversa
from Grafos import Grafos_Objeto


def Grafo(nos, cluster, chaves):
    grafo = Grafos_Objeto.Grafos(nos, cluster, chaves)
    return grafo


def Sem_Intersseccao(nos, cluster, chaves, par_de_cluster, grafo):
    sem_interseccao_nos = 0
    sem_interseccao = []
    for c in par_de_cluster:
        for k in cluster[c]:
            if k in list(grafo.Inteseccao().keys()):
                if len(grafo.Inteseccao()[k]) == 1:
                    sem_interseccao_nos += 1
        sem_interseccao.append(sem_interseccao_nos)
        sem_interseccao_nos = 0

    return sem_interseccao


def Escolhendo_No_Isolado(nos, cluster, chaves, par_de_cluster, grafo, novas_chaves):
    sem_interseccao_nos = []
    sem_interseccao = []
    for c in par_de_cluster:
        for k in cluster[c]:
            if k in list(grafo.Inteseccao().keys()):
                if len(grafo.Inteseccao()[k]) == 1:
                    sem_interseccao_nos.append(chaves[k][0])

        escolhido = random.choice(sem_interseccao_nos)
        while escolhido in novas_chaves:
            escolhido = random.choice(sem_interseccao_nos)

        sem_interseccao.append(escolhido)

        sem_interseccao_nos = []

    return sem_interseccao


def Gerando_Novo_Nos(par_de_cluster, capacidade, matrix, ferramentas, cluster, nos, chaves):
    tarefa_i = par_de_cluster[0]
    tarefa_j = par_de_cluster[1]

    print('Tarefa i', tarefa_i)
    print('Tarefa_j', tarefa_j)
    grafo = Grafo(nos=nos, cluster=cluster, chaves=chaves)
    sem_interseccao = Sem_Intersseccao(nos=nos, cluster=cluster, chaves=chaves, par_de_cluster=par_de_cluster,
                                       grafo=grafo)

    ferramentas_i = Funcoes_Reversa.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [tarefa_i])
    ferramentas_j = Funcoes_Reversa.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [tarefa_j])

    # print('Ferramentas i', ferramentas_i)
    #
    # print('Ferramentas j', ferramentas_j)

    populariedade = Funcoes_Reversa.requerimentos_de_ferramentas(ferramentas=ferramentas, matrix=matrix)
    populariedade = numpy.argsort(populariedade)
    populariedade = populariedade[::-1][:len(populariedade)]

    # Ferramentas que estao em i porém nao estao em j
    diferencai_j = Funcoes_Reversa.ferramentas_que_nao_estao_na_tarefa(ferramentas_i, tarefa_j, matrix, ferramentas)
    # Ferramentas que estao em j porém nao estao em i
    diferencaj_i = Funcoes_Reversa.ferramentas_que_nao_estao_na_tarefa(ferramentas_j, tarefa_i, matrix, ferramentas)

    novo_nos_j = Opcoes_de_Completar(diferencai_j, ferramentas_j, capacidade, populariedade, sem_interseccao[1],
                                     len(nos))

    novo_nos_i = Opcoes_de_Completar(diferencaj_i, ferramentas_i, capacidade, populariedade, sem_interseccao[0],
                                     len(nos))

    aux = []
    aux1 = []

    if isinstance(novo_nos_i[0], list):
        for i in novo_nos_i:
            aux.append(set(i))
            aux1.append(i)
    else:
        aux.append(novo_nos_i)

    if isinstance(novo_nos_j[0], list):
        for i in novo_nos_j:
            aux.append(set(i))
            aux1.append(i)
    else:
        aux.append(novo_nos_j)

    if aux:
        novo_nos_set = []
        novos_nos = []
        if isinstance(aux[0], set):
            for i in range(len(aux)):
                if aux[i] not in novo_nos_set:
                    novo_nos_set.append(aux[i])
                    novos_nos.append(aux1[i])
        else:
            for i in range(len(aux)):
                if aux[i] not in novos_nos:
                    novos_nos.append(aux[i])

    return novos_nos


def Novo_Nos(combinacao, aux, tamanho, tamanho_do_no):
    novo_nos = []
    escolhidos = []
    if tamanho > 0:
        while len(novo_nos) < tamanho and len(escolhidos) < len(combinacao):
            escolha_aleatoria = random.randint(0, len(combinacao) - 1)
            if escolha_aleatoria not in escolhidos:
                novo_nos.append(aux + list(combinacao[escolha_aleatoria]))
                escolhidos.append(escolha_aleatoria)
    else:
        if tamanho_do_no <= 20:
            while len(novo_nos) < int(0.20 * tamanho_do_no) and len(escolhidos) < len(combinacao):
                escolha_aleatoria = random.randint(0, len(combinacao) - 1)
                if escolha_aleatoria not in escolhidos:
                    novo_nos.append(aux + list(combinacao[escolha_aleatoria]))
                    escolhidos.append(escolha_aleatoria)
        else:
            while len(novo_nos) < int(0.10 * tamanho_do_no) and len(escolhidos) < len(combinacao):
                escolha_aleatoria = random.randint(0, len(combinacao) - 1)
                if escolha_aleatoria not in escolhidos:
                    novo_nos.append(aux + list(combinacao[escolha_aleatoria]))
                    escolhidos.append(escolha_aleatoria)

    return novo_nos


def Opcoes_de_Completar(diferenca, ferramentas, capacidade, populariedade, tamanho, tamanho_do_cluster):
    if len(diferenca) > capacidade - len(ferramentas):
        combinacao = itertools.combinations(diferenca, capacidade - len(ferramentas))
        novo_nos = Novo_Nos(list(combinacao), ferramentas, tamanho, tamanho_do_cluster)
    else:
        if len(diferenca) == capacidade - len(ferramentas):
            novo_nos = ferramentas + diferenca
        else:
            aux = ferramentas + diferenca
            restantes = set(populariedade) - set(aux)
            combinacao = itertools.combinations(restantes, capacidade - len(aux))
            novo_nos = Novo_Nos(list(combinacao), aux, tamanho, tamanho_do_cluster)

    return novo_nos


def Completando_Clusters_Eliminando_Indiviais(pares_clusters, cluster, nos, chaves, matrix,
                                              ferramentas, capacidade):
    novos_nos = Gerando_Novo_Nos(par_de_cluster=pares_clusters, capacidade=capacidade,
                                 matrix=matrix, ferramentas=ferramentas, cluster=cluster,
                                 nos=nos, chaves=chaves)

    ##Primeiro identificando os nos que nao fazendo interssecacao nos clusters em questao:
    cluster_intersseccoes = []
    indice_intesseccao = []
    chave = len(chaves)
    novas_chaves = []
    for p in range(len(novos_nos)):
        for c in cluster:
            if (set(Funcoes_Reversa.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [c])) &
                (set(novos_nos[p]))) == set(
                Funcoes_Reversa.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [c])):
                cluster_intersseccoes.append(c)

        no_ja_presente = []
        if len(cluster_intersseccoes) >= 2:
            indice_intesseccao.append(p)
            for k in cluster_intersseccoes:
                if (Funcoes_Reversa.Calculando_a_Chave(novos_nos[p]) not in cluster[k]):
                    cluster[k].append(Funcoes_Reversa.Calculando_a_Chave(novos_nos[p]))
                    if Funcoes_Reversa.Calculando_a_Chave(novos_nos[p]) not in list(chaves.keys()):
                        nos[chave] = novos_nos[p]
                        chaves[Funcoes_Reversa.Calculando_a_Chave(novos_nos[p])] = []
                        chaves[Funcoes_Reversa.Calculando_a_Chave(novos_nos[p])].append(chave)
                        novas_chaves.append(chave)
                        chave += 1
                else:
                    no_ja_presente.append(k)

            if no_ja_presente == []:
                grafo = Grafo(nos=nos, cluster=cluster, chaves=chaves)

                sem_interseccoes = Sem_Intersseccao(nos=nos, cluster=cluster, chaves=chaves,
                                                    par_de_cluster=cluster_intersseccoes, grafo=grafo)

                if numpy.count_nonzero(sem_interseccoes) == len(cluster_intersseccoes):
                    nos_escolhidos = Escolhendo_No_Isolado(nos=nos, cluster=cluster, chaves=chaves,
                                                           par_de_cluster=cluster_intersseccoes, grafo=grafo,
                                                           novas_chaves=novas_chaves)
                    q = 0
                    for i in nos_escolhidos:
                        deletar = Funcoes_Reversa.Calculando_a_Chave(nos[i])
                        del chaves[deletar]
                        del nos[i]
                        lista = list(cluster.get(cluster_intersseccoes[q]))
                        lista.remove(deletar)
                        cluster[cluster_intersseccoes[q]] = []
                        cluster[cluster_intersseccoes[q]] = lista
                        q += 1


                else:
                    if numpy.count_nonzero(sem_interseccoes) > 0:
                        indices = numpy.flatnonzero(sem_interseccoes)
                        cluster_restantes = []
                        for i in indices:
                            cluster_restantes.append(cluster_intersseccoes[i])

                        nos_escolhidos = Escolhendo_No_Isolado(nos=nos, cluster=cluster, chaves=chaves,
                                                               par_de_cluster=cluster_restantes, grafo=grafo,
                                                               novas_chaves=novas_chaves)
                        q = 0
                        for i in nos_escolhidos:
                            deletar = Funcoes_Reversa.Calculando_a_Chave(nos[i])
                            del chaves[deletar]
                            del nos[i]
                            lista = list(cluster.get(cluster_restantes[q]))
                            lista.remove(deletar)
                            cluster[cluster_restantes[q]] = []
                            cluster[cluster_restantes[q]] = lista
                            q += 1

        else:
            for k in cluster_intersseccoes:
                if (Funcoes_Reversa.Calculando_a_Chave(novos_nos[p]) not in cluster[k]):
                    cluster[k].append(Funcoes_Reversa.Calculando_a_Chave(novos_nos[p]))
                    if Funcoes_Reversa.Calculando_a_Chave(novos_nos[p]) not in list(chaves.keys()):
                        nos[chave] = novos_nos[p]
                        chaves[Funcoes_Reversa.Calculando_a_Chave(novos_nos[p])] = []
                        chaves[Funcoes_Reversa.Calculando_a_Chave(novos_nos[p])].append(chave)
                        novas_chaves.append(chave)
                        chave += 1

        cluster_intersseccoes = []

    print('Tamanho dos nos', len(nos))
    print('Tamanho dos nos',len(chaves))
    nos_finais = {}
    chaves_finais = {}

    chave = 0

    for i in nos:
        nos_finais[chave] = nos[i]
        chaves_finais[Funcoes_Reversa.Calculando_a_Chave(nos[i])] = []
        chaves_finais[Funcoes_Reversa.Calculando_a_Chave(nos[i])].append(chave)
        chave += 1

    print('Tamanho dos nos', len(nos_finais))
    print('Tamanho dos nos', len(chaves_finais))

    return nos_finais, chaves_finais, cluster
