import pandas as pd
import glob
import FuncaoLeitura as opter
import Execucao as executar
import os
import Verifcar


def GrupoD(folder):
    arquivo = "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\instancias_lidas_GrupoD.txt"
    grupo = "\\GrupoD\\"
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

        df10 = pd.DataFrame()

        df11 = pd.DataFrame()

        df12 = pd.DataFrame()

        df13 = pd.DataFrame()

        df14 = pd.DataFrame()

        df15 = pd.DataFrame()

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

        df10 = df10.append(
            {' |J| ': ' ', ' |T| ': ' ', ' |C| ': ' ', ' TP': ' ',
             ' NT ': ' ', ' Tempo ': ' ', ' Media ': ' ',
             'Media de Tempo': ' ',
             ' Desvio Padrao ': ' '}, ignore_index=True)

        df11 = df11.append(
            {' |J| ': ' ', ' |T| ': ' ', ' |C| ': ' ', ' TP': ' ',
             ' NT ': ' ', ' Tempo ': ' ', ' Media ': ' ',
             'Media de Tempo': ' ',
             ' Desvio Padrao ': ' '}, ignore_index=True)

        df12 = df12.append(
            {' |J| ': ' ', ' |T| ': ' ', ' |C| ': ' ', ' TP': ' ',
             ' NT ': ' ', ' Tempo ': ' ', ' Media ': ' ',
             'Media de Tempo': ' ',
             ' Desvio Padrao ': ' '}, ignore_index=True)

        df13 = df13.append(
            {' |J| ': ' ', ' |T| ': ' ', ' |C| ': ' ', ' TP': ' ',
             ' NT ': ' ', ' Tempo ': ' ', ' Media ': ' ',
             'Media de Tempo': ' ',
             ' Desvio Padrao ': ' '}, ignore_index=True)

        df14 = df14.append(
            {' |J| ': ' ', ' |T| ': ' ', ' |C| ': ' ', ' TP': ' ',
             ' NT ': ' ', ' Tempo ': ' ', ' Media ': ' ',
             'Media de Tempo': ' ',
             ' Desvio Padrao ': ' '}, ignore_index=True)

        df15 = df15.append(
            {' |J| ': ' ', ' |T| ': ' ', ' |C| ': ' ', ' TP': ' ',
             ' NT ': ' ', ' Tempo ': ' ', ' Media ': ' ',
             'Media de Tempo': ' ',
             ' Desvio Padrao ': ' '}, ignore_index=True)

        df1.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste1_D.csv", index=None,
                   header=True)

        df2.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste2_D.csv", index=None,
                   header=True)

        df3.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste3_D.csv", index=None,
                   header=True)

        df4.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste4_D.csv", index=None,
                   header=True)

        df5.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste5_D.csv", index=None,
                   header=True)

        df6.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste6_D.csv", index=None,
                   header=True)

        df7.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste7_D.csv", index=None,
                   header=True)

        df8.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste8_D.csv", index=None,
                   header=True)

        df9.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste9_D.csv", index=None,
                   header=True)

        df10.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste10_D.csv", index=None,
                    header=True)

        df11.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste11_D.csv", index=None,
                    header=True)

        df12.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste12_D.csv", index=None,
                    header=True)

        df13.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste13_D.csv", index=None,
                    header=True)

        df14.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste14_D.csv", index=None,
                    header=True)

        df15.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste15_D.csv", index=None,
                    header=True)

    else:
        print('entrei2')
        df1 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste1_D.csv")
        df2 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste2_D.csv")
        df3 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste3_D.csv")
        df4 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste4_D.csv")
        df5 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste5_D.csv")
        df6 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste6_D.csv")
        df7 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste7_D.csv")
        df8 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste8_D.csv")
        df9 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste9_D.csv")
        df10 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste10_D.csv")
        df11 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste11_D.csv")
        df12 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste12_D.csv")
        df13 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste13_D.csv")
        df14 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste14_D.csv")
        df15 = pd.read_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste15_D.csv")

    for filename in glob.glob(os.path.join(folder, '*.txt')):
        if Verifcar.Veficar_Grupo(filename, arquivo, grupo):
            with open(filename, 'r') as f:
                tarefas, ferramentas, capacidade, matrix = opter.instancias(
                    f)  # optendo todos os valores de instâncias recolhidas em um determinado arquivo

            tamanho, melhor_solucao, melhor_tempo, media, desvio_padrao, media_de_tempo = executar.Execucao(
                tarefas=tarefas,
                ferramentas=ferramentas,
                matrix=matrix,
                capacidade=capacidade)

            if (tarefas == 20) and (ferramentas == 15) and (capacidade == 5):
                if list(df1) != []:
                    df1 = df1.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df1.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste1_D.csv", index=None,
                               header=True)
            if tarefas == 20 and ferramentas == 15 and capacidade == 10:
                if list(df2) != []:
                    df2 = df2.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df2.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste2_D.csv", index=None,
                               header=True)

            if tarefas == 20 and ferramentas == 20 and capacidade == 5:
                if list(df3) != []:
                    df3 = df3.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df3.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste3_D.csv", index=None,
                               header=True)

            if tarefas == 20 and ferramentas == 20 and capacidade == 10:
                if list(df4) != []:
                    df4 = df4.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df4.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste4_D.csv", index=None,
                               header=True)

            if tarefas == 20 and ferramentas == 20 and capacidade == 15:
                if list(df5) != []:
                    df5 = df5.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df5.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste5_D.csv", index=None,
                               header=True)

            if tarefas == 20 and ferramentas == 25 and capacidade == 5:
                if list(df6) != []:
                    df6 = df6.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df6.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste6_D.csv", index=None,
                               header=True)

            if tarefas == 20 and ferramentas == 25 and capacidade == 10:
                if list(df7) != []:
                    df7 = df7.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df7.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste7_D.csv", index=None,
                               header=True)

            if tarefas == 20 and ferramentas == 25 and capacidade == 15:
                if list(df8) != []:
                    df8 = df8.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df8.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste8_D.csv", index=None,
                               header=True)
            if tarefas == 20 and ferramentas == 25 and capacidade == 20:
                if list(df9) != []:
                    df9 = df9.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df9.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste9_D.csv", index=None,
                               header=True)

            if tarefas == 25 and ferramentas == 15 and capacidade == 10:
                if list(df10) != []:
                    df10 = df10.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df10.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste10_D.csv", index=None,
                                header=True)
            if tarefas == 25 and ferramentas == 20 and capacidade == 10:
                if list(df11) != []:
                    df11 = df11.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df11.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste11_D.csv", index=None,
                                header=True)

            if tarefas == 25 and ferramentas == 20 and capacidade == 15:
                if list(df12) != []:
                    df12 = df12.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df12.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste12_D.csv", index=None,
                                header=True)

            if tarefas == 25 and ferramentas == 25 and capacidade == 10:
                if list(df13) != []:
                    df13 = df13.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df13.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste13_D.csv", index=None,
                                header=True)

            if tarefas == 25 and ferramentas == 25 and capacidade == 15:
                if list(df14) != []:
                    df14 = df14.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df14.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste14_D.csv", index=None,
                                header=True)

            if tarefas == 25 and ferramentas == 25 and capacidade == 20:
                if list(df15) != []:
                    df15 = df15.append(
                        {' |J| ': tarefas, ' |T| ': ferramentas, ' |C| ': capacidade, ' TP': tamanho,
                         ' NT ': melhor_solucao, ' Tempo ': melhor_tempo, ' Media ': media,
                         'Media de Tempo': media_de_tempo,
                         ' Desvio Padrao ': desvio_padrao}, ignore_index=True)

                    df15.to_csv("C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Resultados\\GrupoD\\teste15_D.csv", index=None,
                                header=True)

            Verifcar.Atualizar(filename, arquivo)
