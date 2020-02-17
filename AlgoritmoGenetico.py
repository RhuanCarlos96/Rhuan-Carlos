from Grafos import Grafos_Objeto as grafo
import random
import copy
import Frequencia as frequencia


def Individuos(cromossomo):
    individuos_grupos = {}
    individuos = 0
    for q in cromossomo:
        individuos_grupos[individuos] = q
        individuos += 1

    return individuos_grupos


def Removendo_Cidades(cidade, cidades, cidades_keys):
    for i in cidades_keys:
        if cidade in cidades[i]:
            cidades[i].remove(cidade)

    return cidades


def Vazias(filho, cidades_keys, cidades):
    nao_estao_vazias = set(cidades_keys) - set(filho)
    p = 0
    menor_fronteira = -1
    for v in nao_estao_vazias:
        aux = []
        if p == 0:
            menor_fronteira = v

        else:
            if len(cidades[v]) < len(cidades[menor_fronteira]):
                menor_fronteira = v

            else:
                if (len(cidades[v]) == len(cidades[menor_fronteira])):
                    aux.append(v)
                    aux.append(menor_fronteira)
                    menor_fronteira = random.choice(aux)
        p += 1

    return menor_fronteira


def Filho_CrossOver(cidades):
    cidades_keys = list(cidades.keys())

    # Para o primeiro filho escolho aleatoriamente uma "cidade"
    filho = []
    cidade = random.choice(cidades_keys)
    filho.append(cidade)
    # Eliminando este elemento nas outras cidades

    while len(filho) < len(cidades_keys):
        cidades = Removendo_Cidades(cidade, cidades, cidades_keys)

        # Escolhendo a proxima cidade que faz fronteira com a primeira que possui menor fronteira

        if cidades[cidade] == []:
            cidade = Vazias(filho, cidades, cidades)
            cidades_fronteiras = cidades[cidade]

        else:
            cidades_fronteiras = cidades[cidade]

        menor_fronteira = -1
        k = 0
        for i in cidades_fronteiras:
            aux = []
            if k == 0:
                menor_fronteira = i
            else:
                if (len(cidades[i]) < len(cidades[menor_fronteira])):
                    if cidades[i] != []:
                        menor_fronteira = i
                    else:
                        filho.append(i)
                        menor_fronteira = Vazias(filho, cidades_keys, cidades)
                else:
                    if (len(cidades[i]) == len(cidades[menor_fronteira])):
                        if cidades[i] != [] and cidades[menor_fronteira] != []:
                            aux.append(i)
                            aux.append(menor_fronteira)
                            menor_fronteira = random.choice(aux)
                        else:
                            filho.append(i)
                            menor_fronteira = Vazias(filho, cidades_keys, cidades)

            k += 1

        filho.append(menor_fronteira)
        cidade = menor_fronteira

    return filho


def Copia(elemento):
    copia = copy.deepcopy(elemento)

    return copia


def Substring(individo1, individuo2):
    individuo_filho = [-1] * len(individo1)
    print('Individuo', individo1)
    print('Individuo2', individuo2)
    cont = 0
    a = random.randint(0, len(individo1) - 1)
    print('indice escolhido', a)

    if len(individuo_filho) % 2 == 0:
        string = individo1[a:a + int(len(individo1) / 2)]

        if len(string) == int(len(individuo_filho) / 2):
            for i in range(len(string)):
                individuo_filho[a + i] = string[i]

            cont = a + int(len(individuo2) / 2)
            k = 0
            q_filho = cont
            while k < int(len(individuo2) / 2):
                if cont < len(individuo2):
                    if individuo2[cont] not in individuo_filho and q_filho < len(individuo_filho):
                        individuo_filho[q_filho] = individuo2[cont]
                        k += 1
                        q_filho += 1
                    else:
                        if q_filho == len(individuo_filho):
                            q_filho = 0
                else:
                    if cont == len(individuo2):
                        cont = 0
                        if individuo2[cont] not in individuo_filho and q_filho < len(individuo_filho):
                            individuo_filho[q_filho] = individuo2[cont]
                            k += 1
                            if q_filho == len(individuo_filho):
                                q_filho = 0
                            else:
                                q_filho += 1
                cont += 1

        else:
            for i in range(len(string)):
                individuo_filho[a + i] = string[i]

            restante = int(len(individuo_filho) / 2) - len(string)

            cont = 0
            while cont < restante:
                individuo_filho[cont] = individo1[cont]
                cont += 1
            k = 0
            q_filho = cont
            while k < int(len(individuo2) / 2):
                if cont < len(individuo2):
                    if individuo2[cont] not in individuo_filho and q_filho < len(individuo_filho):
                        individuo_filho[q_filho] = individuo2[cont]
                        k += 1
                        q_filho += 1
                    else:
                        if q_filho == len(individuo_filho):
                            q_filho = 0
                else:
                    if cont == len(individuo2):
                        cont = 0
                        if individuo2[cont] not in individuo_filho and q_filho < len(individuo_filho):
                            individuo_filho[q_filho] = individuo2[cont]
                            k += 1
                            if q_filho == len(individuo_filho):
                                q_filho = 0
                            else:
                                q_filho += 1
                cont += 1
    else:
        string = individo1[a:a + int(len(individo1) / 2)]

        if len(string) == int(len(individuo_filho) / 2):
            for i in range(len(string)):
                individuo_filho[a + i] = string[i]

            cont = a + int(len(individuo2) / 2)
            k = 0
            q_filho = cont
            while k < int(len(individuo2) / 2) + 1:
                if cont < len(individuo2):
                    if individuo2[cont] not in individuo_filho and q_filho < len(individuo_filho):
                        individuo_filho[q_filho] = individuo2[cont]
                        k += 1
                        q_filho += 1
                    else:
                        if q_filho == len(individuo_filho):
                            q_filho = 0
                else:
                    if cont == len(individuo2):
                        cont = 0
                        if individuo2[cont] not in individuo_filho and q_filho < len(individuo_filho):
                            individuo_filho[q_filho] = individuo2[cont]
                            k += 1
                            if q_filho == len(individuo_filho):
                                q_filho = 0
                            else:
                                q_filho += 1
                cont += 1

        else:
            for i in range(len(string)):
                individuo_filho[a + i] = string[i]

            restante = int(len(individuo_filho) / 2) - len(string)

            cont = 0
            while cont < restante:
                individuo_filho[cont] = individo1[cont]
                cont += 1
            k = 0
            q_filho = cont
            while k < int(len(individuo2) / 2) + 1:
                if cont < len(individuo2):
                    if individuo2[cont] not in individuo_filho and q_filho < len(individuo_filho):
                        individuo_filho[q_filho] = individuo2[cont]
                        k += 1
                        q_filho += 1
                    else:
                        if q_filho == len(individuo_filho):
                            q_filho = 0
                else:
                    if cont == len(individuo2):
                        cont = 0
                        if individuo2[cont] not in individuo_filho and q_filho < len(individuo_filho):
                            individuo_filho[q_filho] = individuo2[cont]
                            k += 1
                            if q_filho == len(individuo_filho):
                                q_filho = 0
                            else:
                                q_filho += 1
                cont += 1

    print('Individuo Filho', individuo_filho)


class Genetico(object):

    def __init__(self, nos, cluster, chaves):
        self.__entrada = grafo.Grafos(nos, cluster, chaves)
        self.__cromossomo_cluster = []
        self.__cromossomo_nos = []
        self.__individuos_fitness = {}
        self.__individuos_clusters = {}
        self.__individuos_nos = {}
        self.frequencia = frequencia.Frequencia()

    def Populacao_Inicial(self, tamanho_inicial):
        keys_cluster = self.__entrada.Cluster().keys()
        keys_cluster = list(keys_cluster)

        # Definindo os possiveis cromossomos dada a uma sequência de clusters
        aux = []

        for i in range(5):
            random.shuffle(keys_cluster)

            for i in keys_cluster:
                aux.append(i)

            if aux not in self.__cromossomo_cluster:
                self.__cromossomo_cluster.append(aux)

            aux = []

    def Possiveis_Cromossomos_Inciais(self):
        aux2 = []
        prossiveis_cromossomos_nos = []

        # Gerando os possiveis soluções de nos de modo aleatorio
        for cromossomo in self.__cromossomo_cluster:
            for i in cromossomo:
                aux = self.__entrada.Cluster()[i]
                a = random.choice(aux)
                if a in aux2:
                    a = random.choice(aux)
                    aux2.append(a)  # escolhendo aleatoriamente um no de acordo com a chave
                else:
                    aux2.append(a)

            prossiveis_cromossomos_nos.append(aux2)
            aux2 = []

        print('\n')

        return prossiveis_cromossomos_nos

    def Possiveis_Cromossomos_Entre_Geracoes(self):
        aux2 = []
        prossiveis_cromossomos_nos = []

        # Gerando os possiveis soluções de nos de modo aleatorio
        for individuo in self.__individuos_clusters:
            for i in self.__individuos_clusters[individuo]:
                aux = self.__entrada.Cluster()[i]
                a = random.choice(aux)
                if a in aux2:
                    a = random.choice(aux)
                    aux2.append(a)  # escolhendo aleatoriamente um no de acordo com a chave
                else:
                    aux2.append(a)

            prossiveis_cromossomos_nos.append(aux2)
            aux2 = []

        return prossiveis_cromossomos_nos

    def Tratando_os_Cromossomos(self, prossiveis_cromossomos_nos):

        # 1)Como existe interseccções entre os clusters devemos verificar os nos que participam mais de um cluster e eliminar
        # os outros que pertencem a unico cluster, na qual este no pode representar este nos na distribuição de clusters.
        # Outro modo é permitir uma unica interessecção se o nó representa unicamente um cluster que os demais nos não
        # fazem interessecção

        # 1.1)Primeiro eliminar nos que pertencem as mesmas intersecções, se houver
        #   1.1.1 Determinando os indices na qual este nos pertencendes se localizam:

        indice = []
        aux = []
        indice_intersseccao = []
        cromossomos_interseccoes_sem_repeticoes = []
        for i in prossiveis_cromossomos_nos:
            aux2 = i

            for j in range(len(i)):
                aux.append(self.__entrada.Inteseccao()[i[j]])
                for k in range(len(i)):
                    if k != j:
                        if self.__entrada.Inteseccao()[i[j]] == self.__entrada.Inteseccao()[i[k]]:
                            if indice == []:
                                indice.append(i[k])
                                indice_intersseccao.append(self.__entrada.Inteseccao()[i[k]])
                            else:
                                if self.__entrada.Inteseccao()[i[k]] not in indice_intersseccao:
                                    indice.append(i[k])
                                    indice_intersseccao.append(self.__entrada.Inteseccao()[i[k]])

            #   1.1.2 - Eliminando estes nos

            if indice != []:
                for v in indice:
                    aux2.remove(v)

                cromossomos_interseccoes_sem_repeticoes.append(aux2)
            else:
                cromossomos_interseccoes_sem_repeticoes.append(aux2)

            indice = []
            aux = []
            indice_intersseccao = []
            aux2 = []

        # 1.2 - Retirar nos que fazem referencia a mais de um cluster para um mesmo individuo de cluster:
        indice = []
        aux = []
        aux3 = []
        cromossomo_de_nos_final = []
        indice_intersseccao = []
        keys_cluster = list(self.__entrada.Cluster().keys())

        c = set()
        aux4 = []

        for i in cromossomos_interseccoes_sem_repeticoes:
            aux2 = i

            for j in range(len(i)):
                aux.append(len(self.__entrada.Inteseccao()[i[j]]))

            a = max(aux)

            for j in range(len(i)):
                if a == len(self.__entrada.Inteseccao()[i[j]]):
                    indice.append(i[j])
                    indice_intersseccao.append(self.__entrada.Inteseccao()[i[j]])

            for b in indice_intersseccao:
                if aux3 == []:
                    c = set(keys_cluster) - set(b)
                    aux3.append(list(c))

                else:
                    c = c - set(b)
                    aux3.append(list(c))

            c = set(aux3[len(aux3) - 1])
            tamanho_de_c = len(c)
            for j in range(len(i)):
                if i[j] not in indice:
                    if c != {}:
                        c = c - set(self.__entrada.Inteseccao()[i[j]])
                        if len(c) != tamanho_de_c:
                            indice.append(i[j])
                            indice_intersseccao.append(self.__entrada.Inteseccao()[i[j]])
                            tamanho_de_c = len(c)

            for j in i:
                if j in indice:
                    aux4.append(j)

            cromossomo_de_nos_final.append(aux4)

            aux = []
            indice = []
            indice_intersseccao = []
            aux2 = []
            aux3 = []
            aux4 = []

        # 2) Como existe nos que são representados pela mesma chave, então, existe a possibilidade de um
        # cromossomo de clusters seja representado por mais de uma sequência de cromossomos de nos.Tenho que definir um
        # no unico para a chave

        aux = []
        aux2 = []
        cromossomo_nos = []
        self.__cromossomo_nos = []
        for p in range(len(cromossomo_de_nos_final)):

            for c in cromossomo_de_nos_final[p]:
                aux = self.__entrada.Chaves()[c]
                if len(aux) == 1:
                    aux2.append(aux[0])

                else:
                    aux2.append(random.choice(aux))

            self.__cromossomo_nos.append(aux2)
            aux = []
            aux2 = []

    # Calculando o fitness da função, porém primeiro eu separo os individuos em chaves:

    def Individuos_Cluster(self):
        # Individuo de clusters :
        self.__individuos_clusters = Individuos(self.__cromossomo_cluster)

    def Individuos_Nos(self):
        # Individuos nos
        self.__individuos_nos = Individuos(self.__cromossomo_nos)

    def Fitness(self):
        matriz_adjacencia = self.__entrada.Matriz_Adjacencia()
        p = 0

        for k in self.__individuos_nos:
            fitness = 0
            aux = self.__individuos_nos[k]
            aux2 = []

            for i in range(len(aux) - 1):
                aux2.append(matriz_adjacencia[aux[i]][aux[i + 1]])
                fitness = fitness + matriz_adjacencia[aux[i]][aux[i + 1]]

            self.__individuos_fitness[p] = fitness
            p += 1

        self.frequencia.Piores_Fitness(individuos_fitness=self.__individuos_fitness,
                                       individuos_nos=self.__individuos_nos,
                                       individuos_clusters=self.__individuos_clusters)

        melhor_fitness = self.__individuos_fitness[0]

        for i in self.__individuos_fitness:
            if self.__individuos_fitness[i] < melhor_fitness:
                melhor_fitness = self.__individuos_fitness[i]

    def Selecao_Torneio(self):
        selecionados = []

        tamanho_individuos = len(list(self.__individuos_clusters.keys()))

        j = 0
        for i in range(tamanho_individuos):
            pai = 0
            individuo1 = int(random.uniform(0, 1) * (tamanho_individuos - 1))
            individuo2 = int(random.uniform(0, 1) * (tamanho_individuos - 1))
            sorteio = random.uniform(0, 1)
            k = 0.8

            if sorteio < k:

                if self.__individuos_fitness[individuo1] < self.__individuos_fitness[individuo2]:
                    pai = individuo1
                else:
                    pai = individuo2

            else:
                if self.__individuos_fitness[individuo1] < self.__individuos_fitness[individuo2]:
                    pai = individuo1

                else:
                    pai = individuo2

            selecionados.append(pai)
            j += 1

        nao_selecionados = list(set(self.__individuos_clusters.keys()) - set(selecionados))
        self.frequencia.Nao_selecionados(nao_selecionados, self.__individuos_nos, self.__individuos_fitness)
        self.frequencia.Selecionados_Geracoes(set(selecionados), self.__individuos_nos, self.__individuos_fitness)

        return selecionados

    def CrossOver(self, selecionados, probabilidade_crossover):

        print('Selecionados',selecionados)
        individuos_filho_cluster = {}

        for o in range(len(selecionados)):
            # Determinando o primeiro pai de forma aleatória dos individuos selecionados
            individuo1 = random.choice(selecionados)
            pai1 = individuo1
            # Determinando o segundo pai de forma aleatoria dos individuos selecionados
            individuo2 = random.choice(selecionados)
            # Garantindo que os pais não serão os mesmos para que garanta um cruzamento entre individuo
            # com cromossomos diferentes.
            while individuo2 == individuo1:
                individuo2 = random.choice(selecionados)

            pai2 = individuo2

            cromossomo1 = self.__individuos_clusters[pai1]
            cromossomo2 = self.__individuos_clusters[pai2]

            sorteio = random.uniform(0, 1)

            if sorteio < probabilidade_crossover:
                # # Determinandos as fronteiras existentes entre uma 'cidade' a outra
                # cidades_com_todas_as_fronteiras = {}
                #
                # for i in range(len(cromossomo1)):
                #     cidades_com_todas_as_fronteiras[cromossomo1[i]] = []
                #
                #     if i == 0:
                #         cidades_com_todas_as_fronteiras[cromossomo1[i]].append(cromossomo1[i + 1])
                #     elif i == len(cromossomo1) - 1:
                #         cidades_com_todas_as_fronteiras[cromossomo1[i]].append(cromossomo1[i - 1])
                #     else:
                #         cidades_com_todas_as_fronteiras[cromossomo1[i]].append(cromossomo1[i + 1])
                #         cidades_com_todas_as_fronteiras[cromossomo1[i]].append(cromossomo1[i - 1])
                #
                #     k = -1
                #     for j in range(len(cromossomo2)):
                #         if cromossomo1[i] == cromossomo2[j]:
                #             k = j
                #
                #     if k == 0:
                #         if cromossomo2[k + 1] not in cidades_com_todas_as_fronteiras[cromossomo1[i]]:
                #             cidades_com_todas_as_fronteiras[cromossomo1[i]].append(cromossomo2[k + 1])
                #     elif k == len(cromossomo1) - 1:
                #         if cromossomo2[k - 1] not in cidades_com_todas_as_fronteiras[cromossomo1[i]]:
                #             cidades_com_todas_as_fronteiras[cromossomo1[i]].append(cromossomo2[k - 1])
                #     else:
                #         if cromossomo2[k + 1] not in cidades_com_todas_as_fronteiras[cromossomo1[i]]:
                #             cidades_com_todas_as_fronteiras[cromossomo1[i]].append(cromossomo2[k + 1])
                #         if cromossomo2[k - 1] not in cidades_com_todas_as_fronteiras[cromossomo1[i]]:
                #             cidades_com_todas_as_fronteiras[cromossomo1[i]].append(cromossomo2[k - 1])
                #
                # filho1 = Filho_CrossOver(Copia(cidades_com_todas_as_fronteiras))
                # # filho2=Filho_CrossOver(Copia(cidades_com_todas_as_fronteiras))
                #
                # individuos_filho_cluster[o] = filho1

                Substring(cromossomo1, cromossomo2)

            else:
                escolha = [pai1, pai2]
                individuos_filho_cluster[o] = self.__individuos_clusters[random.choice(escolha)]

        return individuos_filho_cluster

    def Mutation_Swap(self, probabilidade_mutação, individuo_filho_cluster):
        individuos = list(individuo_filho_cluster.keys())
        for i in individuos:
            sorteio = random.uniform(0, 1)
            if sorteio < probabilidade_mutação:
                cromossomo = individuo_filho_cluster[i]
                posicao1 = int(random.uniform(0, 1) * (len(cromossomo) - 1))

                posicao2 = int(random.uniform(0, 1) * (len(cromossomo) - 1))

                while posicao2 == posicao1:
                    posicao2 = int(random.uniform(0, 1) * len(cromossomo) - 1)

                aux = cromossomo[posicao1]
                cromossomo[posicao1] = cromossomo[posicao2]
                cromossomo[posicao2] = aux

                individuo_filho_cluster[i] = cromossomo

        self.__individuos_clusters = individuo_filho_cluster

    def Get_Individuos_Clusters(self):

        for i in self.__individuos_clusters:
            print(self.__individuos_clusters[i])

    def GetFrequencia(self):
        return self.frequencia

    def GetInterseccao(self):
        print(self.__entrada.Inteseccao())
