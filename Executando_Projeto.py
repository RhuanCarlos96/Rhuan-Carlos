import Execucao
import FuncaoLeitura
import os
import Verifcar
import pandas as pd


def executando_projeto(arquivo, name):
    if os.stat(
            "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instâncias_divididas\\instâncias_utilizadas.txt").st_size == 0:
        with open(arquivo, 'r') as f:
            tarefas, ferramentas, capacidade, matrix = FuncaoLeitura.instancias(
                f)  # optendo todos os valores de instâncias recolhidas em um determinado arquivo

        path = Verifcar.arquivo_de_resultado(filename=arquivo, name=name)
        df = pd.read_csv(path)
        melhor_solucao, melhor_tempo, media, desvio_padrao, media_de_tempo = Execucao.Execucao(
            tarefas=tarefas,
            ferramentas=ferramentas,
            matrix=matrix,
            capacidade=capacidade)

        #df.append([tarefas, ferramentas, capacidade, melhor_solucao,
        #           media, melhor_tempo, media_de_tempo, desvio_padrao], ignore_index=True)

        df.loc[len(df)] = [tarefas, ferramentas, capacidade, melhor_solucao,media, melhor_tempo, media_de_tempo, desvio_padrao]
        df.to_csv(path, index=None, header=True)

        Verifcar.Atualizar(arquivo,
                           "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instâncias_divididas\\instâncias_utilizadas.txt")
    else:
        if Verifcar.Veficar_Grupo(filename=arquivo,
                                  arquivo_de_instancias_lidas="C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instâncias_divididas\\instâncias_utilizadas.txt"):
            with open(arquivo, 'r') as f:
                tarefas, ferramentas, capacidade, matrix = FuncaoLeitura.instancias(
                    f)  # optendo todos os valores de instâncias recolhidas em um determinado arquivo

            melhor_solucao, melhor_tempo, media, desvio_padrao, media_de_tempo = Execucao.Execucao(
                tarefas=tarefas,
                ferramentas=ferramentas,
                matrix=matrix,
                capacidade=capacidade)
            path = Verifcar.arquivo_de_resultado(filename=arquivo, name=name)
            df = pd.read_csv(path)
            #df.append([tarefas,ferramentas,  capacidade, melhor_solucao,
            #         media, melhor_tempo,media_de_tempo,desvio_padrao], ignore_index=True)

            df.loc[len(df)] = [tarefas, ferramentas, capacidade, melhor_solucao, media, melhor_tempo, media_de_tempo,
                               desvio_padrao]

            df.to_csv(path, index=None, header=True)

            print(df)
            Verifcar.Atualizar(arquivo,
                               "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instâncias_divididas\\instâncias_utilizadas.txt")