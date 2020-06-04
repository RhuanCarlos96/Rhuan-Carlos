import itertools
import random

import numpy

import Funcoes_Reversa
from Grafos import Grafos_Objeto


def Grafo(nos, cluster, chaves):
    grafo = Grafos_Objeto.Grafos(nos, cluster, chaves)
    return grafo


def Sem_Intersseccao(cluster,par_de_cluster, grafo):
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


def nos_isolados(cluster, grafo):
    sem_interseccao = {}

    for k in cluster:
        for c in cluster[k]:
            if c in list(grafo.Inteseccao().keys()):
                if len(grafo.Inteseccao()[c]) == 1:
                    if grafo.Inteseccao()[c][0] not in list(sem_interseccao.keys()):
                        sem_interseccao[grafo.Inteseccao()[c][0]] = []
                        sem_interseccao[grafo.Inteseccao()[c][0]].append(c)


    return sem_interseccao


def nos_nao_isolados(cluster, grafo):
    com_interseccao = {}

    for k in cluster:
        for c in cluster[k]:
            if c in list(grafo.Inteseccao().keys()):
                if len(grafo.Inteseccao()[c])>= 2:
                    for i in grafo.Inteseccao()[c]:
                        if i not in list(com_interseccao.keys()):
                            com_interseccao[i] = []
                            com_interseccao[i].append(c)
                        else:
                            if c not in com_interseccao[i]:
                                com_interseccao[i].append(c)



    return com_interseccao


def Gerando_Novo_Nos(par_de_cluster, capacidade, matrix, ferramentas, cluster, nos, chaves):
    tarefa_i = par_de_cluster[0]
    tarefa_j = par_de_cluster[1]

    # print('Tarefa i', tarefa_i)
    # print('Tarefa_j', tarefa_j)
    grafo = Grafo(nos=nos, cluster=cluster, chaves=chaves)
    sem_interseccao = Sem_Intersseccao(cluster=cluster, par_de_cluster=par_de_cluster,
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

    if len(ferramentas_j) != capacidade:
        novo_nos_j = Opcoes_de_Completar(diferencai_j, ferramentas_j, capacidade, populariedade, sem_interseccao[1],
                                         len(nos))

    if len(ferramentas_i) != capacidade:
        novo_nos_i = Opcoes_de_Completar(diferencaj_i, ferramentas_i, capacidade, populariedade, sem_interseccao[0],
                                         len(nos))

    aux = []
    aux1 = []

    if isinstance(novo_nos_i[0],list):
        for i in novo_nos_i:
            i.sort()
            if i not in aux:
                aux.append(i)
    else:
        novo_nos_i.sort()
        if novo_nos_i not in aux:
            aux.append(novo_nos_i)

    if isinstance(novo_nos_j[0],list):
        for i in novo_nos_j:
            i.sort()
            if i not in aux:
                aux.append(i)
    else:
        novo_nos_j.sort()
        if novo_nos_j not in aux:
            aux.append(novo_nos_j)

    return aux


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
            while len(novo_nos) < int(0.50 * tamanho_do_no) and len(escolhidos) < len(combinacao):
                escolha_aleatoria = random.randint(0, len(combinacao) - 1)
                if escolha_aleatoria not in escolhidos:
                    novo_nos.append(aux + list(combinacao[escolha_aleatoria]))
                    escolhidos.append(escolha_aleatoria)
        else:
            while len(novo_nos) < int(0.30 * tamanho_do_no) and len(escolhidos) < len(combinacao):
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
                                              ferramentas, capacidade, tarefas, conjunto_de_nos_isolados,
                                              conjunto_de_nos_nao_isolados):
    novos_nos = Gerando_Novo_Nos(par_de_cluster=pares_clusters, capacidade=capacidade,
                                 matrix=matrix, ferramentas=ferramentas, cluster=cluster,
                                 nos=nos, chaves=chaves)

    # cluster_auxiliar
    cluster_auxiliar = {}
    for i in range(tarefas):
        cluster_auxiliar[i] = []

    cluster_intersseccao = []
    k = len(chaves)
    for p in range(len(novos_nos)):
        confirmado = 0
        for c in cluster_auxiliar:
            if (set(Funcoes_Reversa.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [c])) &
                (set(novos_nos[p]))) == set(
                Funcoes_Reversa.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [c])):
                if (Funcoes_Reversa.Calculando_a_Chave(novos_nos[p]) not in cluster_auxiliar[c]) :
                    cluster_intersseccao.append(c)
                    if Funcoes_Reversa.Calculando_a_Chave(novos_nos[p]) not in list(chaves.keys()):
                        confirmado +=1
                        nos[k] = novos_nos[p]
                        chaves[Funcoes_Reversa.Calculando_a_Chave(novos_nos[p])] = []
                        chaves[Funcoes_Reversa.Calculando_a_Chave(novos_nos[p])].append(k)
                        k += 1
        if len(cluster_intersseccao) >= 2 and confirmado==1:
            #print(cluster_intersseccao)
            for i in cluster_intersseccao:
                if i in list(conjunto_de_nos_isolados.keys()):
                    aux = conjunto_de_nos_isolados[i]
                    if len(aux)>1:
                        remover = random.choice(aux)
                        aux.remove(remover)
                        del nos[chaves[remover][0]]
                        del chaves[remover]

                    conjunto_de_nos_isolados[i] = aux

                cluster_auxiliar[i].append(Funcoes_Reversa.Calculando_a_Chave(novos_nos[p]))


        else:
            if cluster_intersseccao and confirmado==1:
                for i in cluster_intersseccao:
                    cluster_auxiliar[i].append(Funcoes_Reversa.Calculando_a_Chave(novos_nos[p]))


        cluster_intersseccao = []

    for i in conjunto_de_nos_nao_isolados:
        aux = conjunto_de_nos_nao_isolados[i]
        if aux:
            for j in aux:
                if j not in cluster_auxiliar[i]:
                    cluster_auxiliar[i].append(j)

    for i in conjunto_de_nos_isolados:
        aux = conjunto_de_nos_isolados[i]
        if aux:
            for j in aux:
                if j not in cluster_auxiliar[i]:
                    cluster_auxiliar[i].append(j)

    cluster = Funcoes_Reversa.Copia(cluster_auxiliar)

    nos_final = {}
    chaves_final = {}

    k = 0

    for i in nos:
        nos_final[k] = nos[i]
        chaves_final[Funcoes_Reversa.Calculando_a_Chave(nos[i])] = []
        chaves_final[Funcoes_Reversa.Calculando_a_Chave(nos[i])].append(k)
        k += 1

    nos = Funcoes_Reversa.Copia(nos_final)
    chaves = Funcoes_Reversa.Copia(chaves_final)

    return nos, chaves, cluster


def aumentando_a_quantidade_de_nos(pares_clusters, cluster, nos, chaves, matrix,
                                   ferramentas, capacidade, tamanho_de_nos_antigo,taxa_de_crescimento):
    novos_nos = Gerando_Novo_Nos(par_de_cluster=pares_clusters, capacidade=capacidade,
                                 matrix=matrix, ferramentas=ferramentas, cluster=cluster,
                                 nos=nos, chaves=chaves)

    k = len(chaves)
    for p in range(len(novos_nos)):
        for c in cluster:
            if (set(Funcoes_Reversa.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [c])) &
                (set(novos_nos[p]))) == set(
                Funcoes_Reversa.ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [c])):
                if (Funcoes_Reversa.Calculando_a_Chave(novos_nos[p]) not in cluster[c]):
                    if len(nos) <= (int(tamanho_de_nos_antigo * taxa_de_crescimento) + tamanho_de_nos_antigo):
                        cluster[c].append(Funcoes_Reversa.Calculando_a_Chave(novos_nos[p]))
                        if Funcoes_Reversa.Calculando_a_Chave(novos_nos[p]) not in list(chaves.keys()):
                            nos[k] = novos_nos[p]
                            chaves[Funcoes_Reversa.Calculando_a_Chave(novos_nos[p])] = []
                            chaves[Funcoes_Reversa.Calculando_a_Chave(novos_nos[p])].append(k)
                            k += 1



    return nos, chaves, cluster
