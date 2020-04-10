import pandas as pd
import glob
import FuncaoLeitura as opter
import Execucao as executar
import os
import Verifcar


def GrupoB(folder):
    print('Grupo B')
    arquivo = "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoA\\instancias_lidas_GrupoB.txt"
    grupo = "\\GrupoB\\"
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

        df9 = pd.DataFrame()

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

        df9 = df9.append(
            {' |J| ': ' ', ' |T| ': ' ', ' |C| ': ' ', ' TP': ' ',
             ' NT ': ' ', ' Tempo ': ' ', ' Media ': ' ',
             'Media de Tempo': ' ',
             ' Desvio Padrao ': ' '}, ignore_index=True)

        df1.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoB\\teste1_B.csv", index=None,
                   header=True)

        df2.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoB\\teste2_B.csv", index=None,
                   header=True)

        df3.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoB\\teste3_B.csv", index=None,
                   header=True)

        df4.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoB\\teste4_B.csv", index=None,
                   header=True)

        df5.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoB\\teste5_B.csv", index=None,
                   header=True)

        df6.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoB\\teste6_B.csv", index=None,
                   header=True)

        df7.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoB\\teste7_B.csv", index=None,
                   header=True)

        df8.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoB\\teste8_B.csv", index=None,
                   header=True)

        df9.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoB\\teste9_B.csv", index=None,
                   header=True)


    else:
        print('entrei2')
        df1 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoB\\teste1_B.csv")
        df2 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoB\\teste2_B.csv")
        df3 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoB\\teste3_B.csv")
        df4 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoB\\teste4_B.csv")
        df5 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoB\\teste5_B.csv")
        df6 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoB\\teste6_B.csv")
        df7 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoB\\teste7_B.csv")
        df8 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoB\\teste8_B.csv")
        df9 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoB\\teste9_B.csv")

    for filename in glob.glob(os.path.join(folder, '*.txt')):
        if Verifcar.Veficar_Grupo(filename, arquivo=arquivo, grupo=grupo):
            with open(filename, 'r') as f:
                tarefas, ferramentas, capacidade, matrix = opter.instancias(
                    f)  # optendo todos os valores de instâncias recolhidas em um determinado arquivo

            tamanho, melhor_solucao, melhor_tempo, media, desvio_padrao, media_de_tempo = executar.Execucao(
                tarefas=tarefas,
                ferramentas=ferramentas,
                matrix=matrix,
                capacidade=capacidade)
            if (tarefas == 9) and (ferramentas == 15) and (capacidade == 5):
                if list(df1) != []:
                    df1 = df1.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df1.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoA\\teste1_B.csv", index=None,
                               header=True)

            if tarefas == 9 and ferramentas == 15 and capacidade == 10:
                if list(df2) != []:
                    df2 = df2.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df2.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoA\\teste2_B.csv", index=None,
                               header=True)

            if tarefas == 9 and ferramentas == 20 and capacidade == 5:
                if list(df3) != []:
                    df3 = df3.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df3.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoA\\teste3_B.csv", index=None,
                               header=True)
            if tarefas == 9 and ferramentas == 20 and capacidade == 10:
                if list(df4) != []:
                    df4 = df4.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df4.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoA\\teste4_B.csv", index=None,
                               header=True)

            if tarefas == 9 and ferramentas == 20 and capacidade == 15:
                if list(df5) != []:
                    df5 = df5.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df5.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoA\\teste5_B.csv", index=None,
                               header=True)

            if tarefas == 9 and ferramentas == 25 and capacidade == 5:
                if list(df6) != []:
                    df6 = df6.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df6.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoA\\teste6_B.csv", index=None,
                               header=True)

            if tarefas == 9 and ferramentas == 25 and capacidade == 10:
                if list(df7) != []:
                    df7 = df7.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df7.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoA\\teste7_B.csv", index=None,
                               header=True)

            if tarefas == 9 and ferramentas == 25 and capacidade == 15:
                if list(df8) != []:
                    df8 = df8.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df8.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoA\\teste8_B.csv", index=None,
                               header=True)
            if tarefas == 9 and ferramentas == 25 and capacidade == 20:
                if list(df9) != []:
                    df9 = df9.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df9.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoA\\teste9_B.csv", index=None,
                               header=True)

            Verifcar.Atualizar(filename,arquivo=arquivo)
