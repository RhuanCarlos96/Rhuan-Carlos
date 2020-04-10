import pandas as pd
import glob
import FuncaoLeitura as opter
import Execucao as executar
import os
import Verifcar


def GrupoE(folder):
    print('GrupoE')
    arquivo = "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\instancias_lidas_GrupoE.txt"
    grupo = "\\GrupoE\\"
    if os.stat(arquivo).st_size == 0:
        print('entrei')
        df1 = pd.DataFrame()

        df2 = pd.DataFrame()

        df3 = pd.DataFrame()

        df4 = pd.DataFrame()

        df5 = pd.DataFrame()

        df6 = pd.DataFrame()

        df7 = pd.DataFrame()

        df8 = pd.DataFrame()

        df1 = df1.append(
            {' |J| ': ' ', ' |T| ': ' ', ' |C| ': ' ', ' TP': ' ',
             ' NT ': ' ', ' Tempo ': ' ', ' Media ': ' ',
             'Media de Tempo': ' ',
             ' Desvio Padrao ': ' '}, ignore_index=True)

        df2 = df2.append(
            {' |J| ': ' ', ' |T| ': ' ', ' |C| ': ' ', ' TP': ' ',
             ' NT ': ' ', ' Tempo ': ' ', ' Media ': ' ',
             'Media de Tempo': ' ',
             ' Desvio Padrao ': ' '}, ignore_index=True)

        df3 = df3.append(
            {' |J| ': ' ', ' |T| ': ' ', ' |C| ': ' ', ' TP': ' ',
             ' NT ': ' ', ' Tempo ': ' ', ' Media ': ' ',
             'Media de Tempo': ' ',
             ' Desvio Padrao ': ' '}, ignore_index=True)

        df4 = df4.append(
            {' |J| ': ' ', ' |T| ': ' ', ' |C| ': ' ', ' TP': ' ',
             ' NT ': ' ', ' Tempo ': ' ', ' Media ': ' ',
             'Media de Tempo': ' ',
             ' Desvio Padrao ': ' '}, ignore_index=True)

        df5 = df5.append(
            {' |J| ': ' ', ' |T| ': ' ', ' |C| ': ' ', ' TP': ' ',
             ' NT ': ' ', ' Tempo ': ' ', ' Media ': ' ',
             'Media de Tempo': ' ',
             ' Desvio Padrao ': ' '}, ignore_index=True)

        df6 = df6.append(
            {' |J| ': ' ', ' |T| ': ' ', ' |C| ': ' ', ' TP': ' ',
             ' NT ': ' ', ' Tempo ': ' ', ' Media ': ' ',
             'Media de Tempo': ' ',
             ' Desvio Padrao ': ' '}, ignore_index=True)

        df7 = df7.append(
            {' |J| ': ' ', ' |T| ': ' ', ' |C| ': ' ', ' TP': ' ',
             ' NT ': ' ', ' Tempo ': ' ', ' Media ': ' ',
             'Media de Tempo': ' ',
             ' Desvio Padrao ': ' '}, ignore_index=True)

        df8 = df8.append(
            {' |J| ': ' ', ' |T| ': ' ', ' |C| ': ' ', ' TP': ' ',
             ' NT ': ' ', ' Tempo ': ' ', ' Media ': ' ',
             'Media de Tempo': ' ',
             ' Desvio Padrao ': ' '}, ignore_index=True)

        df1.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste1_E.csv", index=None,
                   header=True)

        df2.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste2_E.csv", index=None,
                   header=True)

        df3.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste3_E.csv", index=None,
                   header=True)

        df4.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste4_E.csv", index=None,
                   header=True)

        df5.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste5_E.csv", index=None,
                   header=True)

        df6.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste6_E.csv", index=None,
                   header=True)

        df7.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste7_E.csv", index=None,
                   header=True)

        df8.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste8_E.csv", index=None,
                   header=True)



    else:
        print('entrei2')
        df1 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste1_E.csv")
        df2 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste2_E.csv")
        df3 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste3_E.csv")
        df4 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste4_E.csv")
        df5 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste5_E.csv")
        df6 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste6_E.csv")
        df7 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste7_E.csv")
        df8 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste8_E.csv")

    for filename in glob.glob(os.path.join(folder, '*.txt')):
        if Verifcar.Veficar_Grupo(filename,arquivo,grupo):
            with open(filename, 'r') as f:
                tarefas, ferramentas, capacidade, matrix = opter.instancias(
                    f)  # optendo todos os valores de instâncias recolhidas em um determinado arquivo

            tamanho, melhor_solucao, melhor_tempo, media, desvio_padrao, media_de_tempo = executar.Execucao(
                tarefas=tarefas,
                ferramentas=ferramentas,
                matrix=matrix,
                capacidade=capacidade)

            if (tarefas == 10) and (ferramentas == 10) and (capacidade == 4):
                if list(df1) != []:
                    df1 = df1.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df1.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste1_E.csv", index=None,
                               header=True)

            if tarefas == 10 and ferramentas == 10 and capacidade == 5:
                if list(df2) != []:
                    df2 = df2.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df2.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste2_E.csv", index=None,
                               header=True)
            if tarefas == 10 and ferramentas == 10 and capacidade == 6:
                if list(df3) != []:
                    df3 = df3.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df3.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste3_E.csv", index=None,
                               header=True)

            if tarefas == 10 and ferramentas == 10 and capacidade == 7:
                if list(df4) != []:
                    df4 = df4.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df4.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste4_E.csv", index=None,
                               header=True)

            if tarefas == 15 and ferramentas == 20 and capacidade == 6:
                if list(df5) != []:
                    df5 = df5.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df5.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste5_E.csv", index=None,
                               header=True)

            if tarefas == 15 and ferramentas == 20 and capacidade == 8:
                if list(df6) != []:
                    df6 = df6.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df6.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste6_E.csv", index=None,
                               header=True)

            if tarefas == 15 and ferramentas == 20 and capacidade == 10:
                if list(df7) != []:
                    df7 = df7.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df7.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste7_E.csv", index=None,
                               header=True)

            if tarefas == 15 and ferramentas == 20 and capacidade == 12:
                if list(df8) != []:
                    df8 = df8.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df8.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoE\\teste8_E.csv", index=None,
                               header=True)

            Verifcar.Atualizar(filename,arquivo)
