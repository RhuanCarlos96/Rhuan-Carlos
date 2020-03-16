import FuncaoLeitura as opter
import numpy as np
import Reducao_de_Dominio_Reversa as reducao
import Executando_Genetico


def main():
    print('entrou')
    # arquivo.Lendo_Arquivos()

    with open(
            "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Teste_No_PC\\Teste_No_PC\\ChavesEtAl_2012\\ChavesEtAl_2012\\GrupoE\\L8-10.txt",
            "r") as archive:
        tarefas, ferramentas, capacidade, matrix = opter.instancias(
            archive)  # optendo todos os valores de instâncias recolhidas em um determinado arquivo

        print('A maquina possui:\n*tarefas:', tarefas, '\n*ferramentas:', ferramentas, '\n*capacidade:', capacidade)

    jobs = np.arange(0, tarefas)  # conjunto de tarefas
    t = np.arange(0, ferramentas)  # conjunto de ferramentas
    print('Conjunto de tarefas ', jobs)
    print('Conjunto de ferramentas: ', t)
    #
    nos, chaves, cluster = reducao.Reducao_de_Dominio(matrix, tarefas, capacidade, ferramentas,
                                                      jobs, t)

    print('Executando...')
    Executando_Genetico.Running_Genetic(nos, cluster, chaves)
    print('Finalizado!')

    # cluster, nos, chaves = completando.CompletandoNos([4], cluster, matrix, capacidade, t, ferramentas, nos, chaves)
    #
    # print('Tamanho dos Nos', len(nos))
    # print('Tamanho das chaves', len(chaves))


if __name__ == '__main__':
    main()
