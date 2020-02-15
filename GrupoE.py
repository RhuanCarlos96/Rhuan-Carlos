from pandas import DataFrame
import glob
import FuncaoLeitura as opter
import Execucao as executar
import os

def GrupoE(folder):

    df1 = DataFrame()
    df2 = DataFrame()
    df3 = DataFrame()
    df4 = DataFrame()
    df5 = DataFrame()
    df6 = DataFrame()
    df7 = DataFrame()
    df8 = DataFrame()


    for filename in glob.glob(os.path.join(folder, '*.txt')):
        with open(filename, 'r') as f:
            tarefas, ferramentas, capacidade, matrix = opter.instancias(
                f)  # optendo todos os valores de instâncias recolhidas em um determinado arquivo

        if (tarefas == 10) and (ferramentas == 10) and (capacidade == 4):
            if list(df1) == []:
                df1 = df1.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                             capacidade=capacidade)},
                               ignore_index=True)

            else:
                df1 = df1.append({'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                             capacidade=capacidade)}, ignore_index=True)

        if tarefas == 10 and ferramentas == 10 and capacidade == 5:
            if list(df2) == []:

                df2 = df2.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                  'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                               capacidade=capacidade)},
                                 ignore_index=True)

            else:
                df2 = df2.append({'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                               capacidade=capacidade)}, ignore_index=True)

        if tarefas == 10 and ferramentas == 10 and capacidade == 6:
            if list(df3) == []:

                df3 = df3.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                  'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                               capacidade=capacidade)},
                                 ignore_index=True)

            else:
                df3 = df3.append({'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                               capacidade=capacidade)}, ignore_index=True)

        if tarefas == 10 and ferramentas == 10 and capacidade == 7:
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

        if tarefas == 15 and ferramentas == 20 and capacidade == 6:
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

        if tarefas == 15 and ferramentas == 20 and capacidade == 8:
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

        if tarefas == 15 and ferramentas == 20 and capacidade == 10:
            if list(df7) == []:

                df7 = df7.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                  'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas,
                                                               matrix=matrix,
                                                               capacidade=capacidade)}, ignore_index=True)

            else:
                df7 = df7.append(
                    {'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                  capacidade=capacidade)}, ignore_index=True)

        if tarefas == 15 and ferramentas == 20 and capacidade == 12:
            if list(df8) == []:

                df8 = df8.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                  'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas,
                                                               matrix=matrix,
                                                               capacidade=capacidade)}, ignore_index=True)

            else:
                df8 = df8.append(
                    {'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                  capacidade=capacidade)}, ignore_index=True)


    if list(df1) != []:
        df1.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoE//teste1_E.csv', index=None,
                  header=True)
        print(df1)

    if list(df2) != []:
        df2.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoE//teste2_E.csv', index=None,
                   header=True)
        print(df2)

    if list(df3) != []:
        df3.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoE//teste3_E.csv', index=None,
                  header=True)

    if list(df4) != []:
        df4.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoE//teste4_E.csv', index=None,
                  header=True)

    if list(df5) != []:
        df5.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoE//teste5_E.csv', index=None,
                  header=True)

    if list(df6) != []:
        df6.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoE//teste6_E.csv', index=None,
                  header=True)

    if list(df7) != []:
        df7.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoE//teste7_E.csv', index=None,
                  header=True)

    if list(df8) != []:
        df8.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoE//teste8_E.csv', index=None,
                  header=True)

