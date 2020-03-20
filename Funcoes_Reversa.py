import numpy as np
import itertools as inter
import copy
import random


def tarefas_com_c_requerimentos(matrix, tarefas, capacidade, ferramentas):
    jc = []
    for i in range(tarefas):
        if np.count_nonzero(matrix[:, i]) == capacidade:
            jc.append(i)

    return jc


def tarefas_com_maior_requerimento(matrix, tarefas, capacidade, ferramentas):
    j_barra = []

    maior = len(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [0]))

    for i in range(tarefas):
        if len(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [i])) > maior:
            j_barra = []
            maior = len(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [i]))
            j_barra.append(i)
        else:
            if len(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [i])) == maior:
                j_barra.append(i)

    return j_barra


def ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, s):
    I = []
    for i in range(len(s)):
        for j in range(ferramentas):
            if matrix[j, s[i]] == 1:
                I.append(j)

    return I


def Best1(matrix, ferramentas, d, j_linha, j, conjunto_de_T):
    ##Função Best1 :
    value = False
    v = set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [j]))

    if j_linha == -1:
        if len(v - conjunto_de_T) > d:
            value = True

    else:
        if len(v - conjunto_de_T) > d:
            value = True

        else:
            value = False

    return value


def CrucialJobs_EstrategiaReversa(matrix, tarefas, capacidade, ferramentas, jobs):
    # Crucial Jobs - Estrategia reversa

    # Tarefas que requerem c ferramentas

    s = tarefas_com_c_requerimentos(matrix, tarefas, capacidade, ferramentas)

    if not s:
        s = tarefas_com_maior_requerimento(matrix, tarefas, capacidade, ferramentas)

    # Critério de parada 7 e 8
    conjunto_de_T = set()
    for i in s:
        conjunto_de_T = conjunto_de_T.union(set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [i])))

    if len(conjunto_de_T) == ferramentas:
        # print('Tarefas Cruciais', s)
        return s

    else:
        V = set(jobs) - set(s)

        V = list(V)

        while len(conjunto_de_T) != ferramentas:

            d = -2
            j_linha = -1

            for j in V:

                if Best1(matrix, ferramentas, d, j_linha, j, conjunto_de_T) == True:
                    d = len(set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [j])) - conjunto_de_T)
                    j_linha = j

            s.append(j_linha)

            V = list(set(V) - set([j_linha]))

            conjunto_de_T = conjunto_de_T.union(
                set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [j_linha])))

        # print('Tarefas Cruciais', s)
        return s


def Distance(aux, ferramentas, matrix, i_linha, j_linha, v):
    d = len(set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [aux[0]])) - set(
        ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [aux[1]])))

    if i_linha == 0 and j_linha == 0 and d > v:
        return d, True

    else:
        if d > v:
            return d, True

        else:
            return v, False


def Maior_Intesecção(restantes, uniao, ferramentas, matrix, v):
    d = len(set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [restantes])).intersection(uniao))

    if d == v:
        return d, True

    else:
        if d > v:
            return d, True

        else:
            return v, False


def requerimentos_de_ferramentas(ferramentas, matrix):
    quantidade_de_requerimentos = []

    for i in range(ferramentas):
        quantidade_de_requerimentos.append(np.count_nonzero(matrix[i, :]))

    return quantidade_de_requerimentos


def Preechendo_Nos(matrix, ferramentas, ferramentas_ilinha, ferramentas_jlinha, tarefas_restantes, capacidade, tarefas):
    # Iniciando o conjunto de tarefas Z a ser retornado com C capacidade com -1
    f_linha = [-1] * capacidade
    # Definindo o conjunto Ti / Tj , Tj / Ti , Ti e Tj e Ti U Tj, respectivamente :
    conjunto_diferenca_i_linha_menos_j_linha = set(ferramentas_ilinha) - set(ferramentas_jlinha)
    # print('Conjunto Ti/ Tj', conjunto_diferenca_i_linha_menos_j_linha)
    conjunto_diferenca_j_linha_menos_i_linha = set(ferramentas_jlinha) - set(ferramentas_ilinha)
    # print('Conjunto Tj/ Ti', conjunto_diferenca_j_linha_menos_i_linha)
    conjunto_interseccao = set(ferramentas_ilinha).intersection(set(ferramentas_jlinha))
    # print('Conjunto Ti e Tj', conjunto_interseccao)
    conjunto_uniao = set(ferramentas_ilinha).union(set(ferramentas_jlinha))
    # print('Conjunto Tj U Ti', conjunto_uniao)

    # Identificando os indice e a popularidade de cada ferramenta do conjunto de diferença
    # e preenchendo f_linha a partir dos slots das ferramentas menos populares de j'-i' com o
    # conjunto Fi' - Fj'

    # print('\n1º passo - Preenchendo os slots relativos as tarefas menos populares de Tj / Ti com Ti/Tj : ')
    if conjunto_diferenca_j_linha_menos_i_linha != {} and conjunto_diferenca_i_linha_menos_j_linha != {}:
        aux = []
        aux2 = []
        for i in range(len(ferramentas_jlinha)):
            if ferramentas_jlinha[i] in conjunto_diferenca_j_linha_menos_i_linha:
                aux.append(i)
                aux2.append(requerimentos_de_ferramentas(ferramentas, matrix)[ferramentas_jlinha[i]])

        # print('\nPopulariedade de Tj/Ti : ', aux2)
        # print('Slots : ', aux, '\n')

        aux2 = np.argsort(aux2)
        aux3 = []
        for i in aux2:
            aux3.append(aux[i])

        k = 0
        for i in aux3:
            if k < len(conjunto_diferenca_i_linha_menos_j_linha):
                f_linha[i] = list(conjunto_diferenca_i_linha_menos_j_linha)[k]
                k += 1

        aux = []
        for i in range(len(f_linha)):
            if f_linha[i] == -1:
                aux.append(i)

    # print('Z :', f_linha)

    # Preenchendo com o conjunto interseccao de i' e j'
    # print('\n2º passo - Adicionando a Z o conjunto intersecção de Ti e Tj :')
    if conjunto_interseccao:
        k = 0
        aux = []
        for i in range(len(f_linha)):
            if f_linha[i] == -1:
                aux.append(i)

        for i in conjunto_interseccao:
            if k < len(aux):
                f_linha[aux[k]] = i
                k += 1
    # print('Z : ', f_linha)
    # Preenchendo o restante do no com conjunto de ferramentas com maior interssecacao com a uniao de f_i e f_j.
    tarefas_restantes = list(tarefas_restantes)
    maior_inteseccao = []

    # print(
    #     '\n3º passo - Preencnhendo os no com as ferramentas das ferramentas restantes com maior intersecção com Ti U Tj')
    for i in tarefas_restantes:
        f = set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [i]))
        maior_inteseccao.append(len(f.intersection(conjunto_uniao)))

    aux2 = np.argsort(np.array(maior_inteseccao))
    aux2 = aux2[::-1][:len(tarefas_restantes)]

    aux = []
    for i in range(len(f_linha)):
        if f_linha[i] == -1:
            aux.append(i)

    k = 0
    while aux != [] and k < len(aux2):
        f = ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [tarefas_restantes[aux2[k]]])
        diferenca = list(set(f) - conjunto_uniao)
        aux3 = []

        if diferenca:
            for i in diferenca:
                aux3.append(requerimentos_de_ferramentas(ferramentas, matrix)[i])

            aux4 = np.argsort(aux3)
            p = 0

            for i in range(len(diferenca)):
                if p < len(aux) and (diferenca[aux4[i]] not in f_linha):
                    f_linha[aux[p]] = diferenca[aux4[i]]
                    p += 1

            aux = []
            for i in range(len(f_linha)):
                if f_linha[i] == -1:
                    aux.append(i)
        k += 1

    # print(' Z : ', set(f_linha))
    # Complentando os nos quando houver necessidade
    if aux:
        aux2 = []
        for i in ferramentas_ilinha:
            aux2.append(
                requerimentos_de_ferramentas(ferramentas, matrix)[i])

        aux2 = np.argsort(aux2)
        aux2 = aux2[::-1][:len(aux2)]
        k = 0
        indices = []
        for i in range(len(aux2)):
            if k < len(aux) and ferramentas_ilinha[aux2[i]] not in f_linha:
                f_linha[aux[k]] = ferramentas_ilinha[aux2[i]]
                indices.append(aux[k])
                k += 1
        aux = list(set(aux) - set(indices))
        while -1 in f_linha:
            T = range(0,capacidade)
            aux2 = []
            for i in T:
                aux2.append(
                    requerimentos_de_ferramentas(ferramentas, matrix)[i])

            aux2 = np.argsort(aux2)
            aux2 = aux2[::-1][:len(aux2)]
            k = 0
            for i in range(len(aux2)):
                if k < len(aux) and T[aux2[i]] not in f_linha:
                    f_linha[aux[k]] = T[aux2[i]]
                    indices.append(aux[k])
                    k += 1

    # print(' Z : ', set(f_linha))
    return f_linha


def FirstNodes(S, matrix, tarefas, capacidade, ferramentas):
    # print('\n')
    # print('Tarefas      Ferramentas')
    # for i in range(tarefas):
    #     print(i, '          ', ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [i]))

    maior = []
    Tarefas_Maior_Distancia = []
    for i in S:
        for j in S:
            Tarefas_Maior_Distancia.append((i, j))
            maior.append(len(set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [i])) - set(
                ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [j]))))

    maior = np.argsort(np.array(maior))
    # Definindo o par que possui a maior distancia
    i_linha = Tarefas_Maior_Distancia[maior[len(maior) - 1]][0]
    j_linha = Tarefas_Maior_Distancia[maior[len(maior) - 1]][1]
    # Completando i_linha com j_linha:
    ferramentas_ilinha = ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [i_linha])
    ferramentas_jlinha = ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [j_linha])

    # print('\n')
    # print('Tarefa i*', i_linha, ' : ', ferramentas_ilinha)
    # print('Tarefa j*', j_linha, ' : ', ferramentas_jlinha)

    tarefas_restantes = set(S) - set(Tarefas_Maior_Distancia)
    # Preenchendo f_ilinha
    Z = []

    # print('Completando i* através de j*')
    Z.append(Preechendo_Nos(matrix, ferramentas, ferramentas_ilinha, ferramentas_jlinha, tarefas_restantes, capacidade,
                            tarefas))

    # print('\nCompletando j* através de i*')
    Z.append(Preechendo_Nos(matrix, ferramentas, ferramentas_jlinha, ferramentas_ilinha, tarefas_restantes, capacidade,
                            tarefas))

    return Z, i_linha, j_linha


def RemJobs(S, Tarefas_a_ser_Retiradas):
    # Identificando tarefas remanescentes a partir de S:
    X = set(S) - set(Tarefas_a_ser_Retiradas)

    return X


def Best2(matrix, ferramentas, d, j_asterisco, j, L):
    ##Função Best1 :
    value = False
    v = set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [j]))

    if j_asterisco == -3:
        if len(v - set(L)) > d:
            value = True

    else:
        if len(v - set(L)) > d:
            value = True

        else:
            value = False

    return value


def FillNodes(matrix, ferramentas, j_asterisco, L_asterisco, capacidade):
    T_j_asterisco = ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [j_asterisco])

    requerimento = requerimentos_de_ferramentas(ferramentas, matrix)

    req_L_asterisco = []
    for l in L_asterisco:
        req_L_asterisco.append(requerimento[l])

    req_L_asterisco = np.array(req_L_asterisco)
    indices = np.argsort(-req_L_asterisco)

    for l in range(len(L_asterisco)):

        if (L_asterisco[indices[l]] not in T_j_asterisco) and (len(T_j_asterisco) != capacidade):
            T_j_asterisco.append(L_asterisco[indices[l]])

    return T_j_asterisco


def FillNode(matrix, ferramentas, capacidade, tarefas, S):
    # FillNodes  - Estratégia Reversa

    jc = tarefas_com_c_requerimentos(matrix, tarefas, capacidade, ferramentas)
    Z = []  # conjunto de nós cruciais

    if jc:
        for i in jc:
            Z.append(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [i]))

        X = RemJobs(S, jc)

    # FirstNodes
    else:
        Z, i_linha, j_linha = FirstNodes(S, matrix, tarefas, capacidade, ferramentas)

        X = RemJobs(S, [i_linha, j_linha])
    while X:
        d_asterisco = -3
        j_asterisco = -3
        L_asterisco = -3

        for L in Z:
            for j in X:
                if Best2(matrix, ferramentas, d_asterisco, j_asterisco, j, L):
                    d_asterisco = (len(
                        set(L).union(set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [j]))))) - capacidade
                    L_asterisco = L
                    j_asterisco = j

        # Fill Nodes:
        L_linha = FillNodes(matrix, ferramentas, j_asterisco, L_asterisco, capacidade)

        X = X - set([j_asterisco])
        Z.append(L_linha)

    Q = Copia(Z)
    return Z, Q


def Calculando_a_Chave(Z):
    key = ""
    for z in Z:
        key = key + " " + str(z)

    return key


def Uptade(S, ferramentas, matrix, cluster, Q, nos_do_clusters, chaves_dos_nos, tarefas, P):
    # Função Uptade: define os clusters que serão formados a partir do nó gerado Q, assim, pode possuir cluster que
    # compartilhem ferramentas.Em que utiliza com entrada o conjunto S e I, já que S  é o conjunto de tarefas
    # cruciais que construiu  o nó crucial Z, ou seja,se tiver C ferramentas, P=[jc] se não P=[S] e atualiza
    # os nós completando-os com o nó I gerado para que todos possam ter C ferramentas.

    # Definindo os crusters criados,através do uso do dicionario(tabela hash)

    if cluster == {}:
        chaves = 0
        # Definindo os nos em ordem crescente de aparecimento.

        for q in Q:
            chaves_dos_nos[Calculando_a_Chave(q)] = []

        for q in Q:
            nos_do_clusters[chaves] = q
            chaves_dos_nos[Calculando_a_Chave(q)].append(chaves)
            chaves += 1

        # Definindo os nos pertencentes aos clusters de acordo com as suas chaves, na qual representam os nós.
        for s in range(tarefas):
            cluster[s] = []

        for q in Q:
            for s in cluster:
                if (set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [s])) &
                    (set(q))) == set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [s])):
                    if Calculando_a_Chave(q) not in cluster[s]:
                        cluster[s].append(Calculando_a_Chave(q))

    else:
        if P != []:
            if len(P) > 300:
                # Calculando o limite dinamico, ou seja, quando nos podem existir no espaço de solução no GTSP
                indice = list(range(0, len(P)))

                cluster_vazios = 0

                for i in cluster:
                    if cluster[i] == []:
                        cluster_vazios += 1

                cluster_cheios = len(cluster) - cluster_vazios

                if cluster_vazios < cluster_cheios:
                    LimD = int((len(P) - len(Q)) / cluster_vazios)
                    Distribuição_Media_Cluster = int(LimD / len(cluster))
                else:
                    LimD = int((len(P) - len(Q)) / cluster_cheios)
                    Distribuição_Media_Cluster = int(LimD / len(cluster))

                # print('LimD', LimD)
                # print('Distribuiçao Media', Distribuição_Media_Cluster)
                chave = len(nos_do_clusters)
                indice_intesseccao = []
                cluster_intersseccoes = []
                for p in range(len(P)):
                    for c in cluster:
                        if (set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [c])) &
                            (set(P[p]))) == set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [c])):
                            cluster_intersseccoes.append(c)

                    if len(cluster_intersseccoes) >= 2:
                        indice_intesseccao.append(p)
                        for k in cluster_intersseccoes:
                            if (set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [k])) &
                                (set(P[p]))) == set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [k])):
                                if (Calculando_a_Chave(P[p]) not in cluster[k]) and (
                                        len(cluster[k]) < Distribuição_Media_Cluster):
                                    cluster[k].append(Calculando_a_Chave(P[p]))
                                    if Calculando_a_Chave(P[p]) not in list(chaves_dos_nos.keys()):
                                        nos_do_clusters[chave] = P[p]
                                        chaves_dos_nos[Calculando_a_Chave(P[p])] = []
                                        chaves_dos_nos[Calculando_a_Chave(P[p])].append(chave)
                                        chave += 1

                    cluster_intersseccoes = []

                indice = list(set(indice) - set(indice_intesseccao))
                random.shuffle(indice)
                P_novo = []
                chave = len(nos_do_clusters)
                for i in indice:
                    P_novo.append(P[i])
                for p in P_novo:
                    for c in cluster:
                        if (set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [c])) &
                            (set(p))) == set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [c])):
                            if (Calculando_a_Chave(p) not in cluster[c]) and (
                                    len(cluster[c]) < Distribuição_Media_Cluster):
                                cluster[c].append(Calculando_a_Chave(p))
                                if p not in list(chaves_dos_nos.keys()):
                                    nos_do_clusters[chave] = Decodificando_Chave(p)
                                    chaves_dos_nos[Calculando_a_Chave(p)] = []
                                    chaves_dos_nos[Calculando_a_Chave(p)].append(chave)
                                    chave += 1
            else:
                # Calculando o limite dinamico, ou seja, quando nos podem existir no espaço de solução no GTSP
                indice = list(range(0, len(P)))
                chave = len(nos_do_clusters)
                indice_intesseccao = []
                cluster_intersseccoes = []
                for p in range(len(P)):
                    for c in cluster:
                        if (set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [c])) &
                            (set(P[p]))) == (
                                set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [c]))):
                            cluster_intersseccoes.append(c)

                    if len(cluster_intersseccoes) >= 2:
                        indice_intesseccao.append(p)
                        for k in cluster_intersseccoes:
                            if (set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [k])) &
                                (set(P[p]))) == (set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [k]))):
                                if (Calculando_a_Chave(P[p]) not in cluster[k]):
                                    cluster[k].append(Calculando_a_Chave(P[p]))
                                    if Calculando_a_Chave(P[p]) not in list(chaves_dos_nos.keys()):
                                        nos_do_clusters[chave] = P[p]
                                        chaves_dos_nos[Calculando_a_Chave(P[p])] = []
                                        chaves_dos_nos[Calculando_a_Chave(P[p])].append(chave)
                                        chave += 1

                    cluster_intersseccoes = []

                indice = list(set(indice) - set(indice_intesseccao))
                random.shuffle(indice)
                P_novo = []
                chave = len(nos_do_clusters)
                for i in indice:
                    P_novo.append(P[i])
                for p in P_novo:
                    for c in cluster:
                        if (set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [c])) &
                            (set(p))) == (set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [c]))):
                            if (Calculando_a_Chave(p) not in cluster[c]):
                                cluster[c].append(Calculando_a_Chave(p))
                                if p not in list(chaves_dos_nos.keys()):
                                    nos_do_clusters[chave] = Decodificando_Chave(p)
                                    chaves_dos_nos[Calculando_a_Chave(p)] = []
                                    chaves_dos_nos[Calculando_a_Chave(p)].append(chave)
                                    chave += 1

    return nos_do_clusters, chaves_dos_nos, cluster


def Distance1(i, j):
    return len(set(i) - set(j))


def ferramentas_que_nao_estao_na_tarefa(Z, E, matrix, ferramentas):
    tools = list(set(Z) - set(ferramentas_da_tarefas_do_conjunto_s(matrix, ferramentas, [E])))
    tools.sort()
    return tools


def Copia(elemento):
    copia = copy.deepcopy(elemento)

    return copia


def Decodificando_Chave(chave):
    chave = list(chave)
    chave_decodificada = []
    for i in chave:
        if i != ' ':
            chave_decodificada.append(int(i))

    return chave_decodificada
