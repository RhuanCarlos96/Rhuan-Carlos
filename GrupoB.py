from pandas import DataFrame
import glob
import FuncaoLeitura as opter
import Execucao as executar
import os

def GrupoB(folder):

    df1 = DataFrame()
    df2 = DataFrame()
    df3 = DataFrame()
    df4 = DataFrame()
    df5 = DataFrame()
    df6 = DataFrame()
    df7 = DataFrame()
    df8 = DataFrame()
    df9 = DataFrame()

    for filename in glob.glob(os.path.join(folder, '*.txt')):
        with open(filename, 'r') as f:
            tarefas, ferramentas, capacidade, matrix = opter.instancias(
                f)  # optendo todos os valores de instâncias recolhidas em um determinado arquivo

        if (tarefas == 9) and (ferramentas == 15) and (capacidade == 5):
            if list(df1) == []:
                df1 = df1.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                             capacidade=capacidade)},
                               ignore_index=True)

            else:
                df1 = df1.append({'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                             capacidade=capacidade)}, ignore_index=True)

        if tarefas == 9 and ferramentas == 15 and capacidade == 10:
            if list(df2) == []:

                df2 = df2.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                  'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                               capacidade=capacidade)},
                                 ignore_index=True)

            else:
                df2 = df2.append({'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                               capacidade=capacidade)}, ignore_index=True)

        if tarefas == 9 and ferramentas == 20 and capacidade == 5:
            if list(df3) == []:

                df3 = df3.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                  'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                               capacidade=capacidade)},
                                 ignore_index=True)

            else:
                df3 = df3.append({'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                               capacidade=capacidade)}, ignore_index=True)

        if tarefas == 9 and ferramentas == 20 and capacidade == 10:
            if list(df4) == []:

                df4 = df4.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                  'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas,
                                                               matrix=matrix,
                                                               capacidade=capacidade)},
                                 ignore_index=True)

            else:
                df4 = df4.append(
                    {'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                  capacidade=capacidade)}, ignore_index=True)

        if tarefas == 9 and ferramentas == 20 and capacidade == 15:
            if list(df5) == []:

                df5 = df5.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                  'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas,
                                                               matrix=matrix,
                                                               capacidade=capacidade)},
                                 ignore_index=True)

            else:
                df5 = df5.append(
                    {'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                  capacidade=capacidade)}, ignore_index=True)

        if tarefas == 9 and ferramentas == 25 and capacidade == 5:
            if list(df6) == []:

                df6 = df6.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                  'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas,
                                                               matrix=matrix,
                                                               capacidade=capacidade)},
                                 ignore_index=True)

            else:
                df6 = df6.append(
                    {'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                  capacidade=capacidade)}, ignore_index=True)

        if tarefas == 9 and ferramentas == 25 and capacidade == 10:
            if list(df7) == []:

                df7 = df7.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                  'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas,
                                                               matrix=matrix,
                                                               capacidade=capacidade)}, ignore_index=True)

            else:
                df7 = df7.append(
                    {'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                  capacidade=capacidade)}, ignore_index=True)

        if tarefas == 9 and ferramentas == 25 and capacidade == 15:
            if list(df8) == []:

                df8 = df8.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                  'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas,
                                                               matrix=matrix,
                                                               capacidade=capacidade)}, ignore_index=True)

            else:
                df8 = df8.append(
                    {'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                  capacidade=capacidade)}, ignore_index=True)

        if tarefas == 9 and ferramentas == 25 and capacidade == 20:
            if list(df9) == []:

                df9 = df9.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                  'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas,
                                                               matrix=matrix,
                                                               capacidade=capacidade)},
                                 ignore_index=True)

            else:
                df9 = df9.append(
                    {'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                  capacidade=capacidade)}, ignore_index=True)

        if list(df1) != []:
            df1.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoB//teste1_B.csv', index=None,
                  header=True)


        if list(df2) != []:
            df2.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoB//teste2_B.csv', index=None,
                   header=True)


        if list(df3) != []:
            df3.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoB//teste3_B.csv', index=None,
                  header=True)

        if list(df4) != []:
            df4.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoB//teste4_B.csv', index=None,
                  header=True)

        if list(df5) != []:
            df5.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoB//teste5_B.csv', index=None,
                  header=True)

        if list(df6) != []:
            df6.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoB//teste6_B.csv', index=None,
                  header=True)

        if list(df7) != []:
            df7.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoB//teste7_B.csv', index=None,
                  header=True)

        if list(df8) != []:
            df8.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoB//teste8_B.csv', index=None,
                  header=True)

        if list(df9) != []:
            df9.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoB//teste9_B.csv', index=None,
                  header=True)

