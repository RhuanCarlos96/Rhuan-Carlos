from pandas import DataFrame
import glob
import FuncaoLeitura as opter
import Execucao as executar
import os

def GrupoD(folder):

    df1 = DataFrame()
    df2 = DataFrame()
    df3 = DataFrame()
    df4 = DataFrame()
    df5 = DataFrame()
    df6 = DataFrame()
    df7 = DataFrame()
    df8 = DataFrame()
    df9 = DataFrame()
    df10 = DataFrame()
    df11 = DataFrame()
    df12 = DataFrame()
    df13 = DataFrame()
    df14 = DataFrame()
    df15 = DataFrame()



    for filename in glob.glob(os.path.join(folder, '*.txt')):
        with open(filename, 'r') as f:
            tarefas, ferramentas, capacidade, matrix = opter.instancias(
                f)  # optendo todos os valores de instâncias recolhidas em um determinado arquivo

        if (tarefas == 20) and (ferramentas == 15) and (capacidade == 5):
            if list(df1) == []:
                df1 = df1.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                             capacidade=capacidade)},
                               ignore_index=True)

            else:
                df1 = df1.append({'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                             capacidade=capacidade)}, ignore_index=True)

        if tarefas == 20 and ferramentas == 15 and capacidade == 10:
            if list(df2) == []:

                df2 = df2.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                  'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                               capacidade=capacidade)},
                                 ignore_index=True)

            else:
                df2 = df2.append({'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                               capacidade=capacidade)}, ignore_index=True)

        if tarefas == 20 and ferramentas == 20 and capacidade == 5:
            if list(df3) == []:

                df3 = df3.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                  'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                               capacidade=capacidade)},
                                 ignore_index=True)

            else:
                df3 = df3.append({'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                               capacidade=capacidade)}, ignore_index=True)

        if tarefas == 20 and ferramentas == 20 and capacidade == 10:
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

        if tarefas == 20 and ferramentas == 20 and capacidade == 15:
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

        if tarefas == 20 and ferramentas == 25 and capacidade == 5:
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

        if tarefas == 20 and ferramentas == 25 and capacidade == 10:
            if list(df7) == []:

                df7 = df7.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                  'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas,
                                                               matrix=matrix,
                                                               capacidade=capacidade)}, ignore_index=True)

            else:
                df7 = df7.append(
                    {'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                  capacidade=capacidade)}, ignore_index=True)

        if tarefas == 20 and ferramentas == 25 and capacidade == 15:
            if list(df8) == []:

                df8 = df8.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                  'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas,
                                                               matrix=matrix,
                                                               capacidade=capacidade)}, ignore_index=True)

            else:
                df8 = df8.append(
                    {'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                                  capacidade=capacidade)}, ignore_index=True)

        if tarefas == 20 and ferramentas == 25 and capacidade == 20:
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

        if tarefas == 25 and ferramentas == 15 and capacidade == 10:
            if list(df10) == []:

                df10 = df10.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                  'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas,
                                                               matrix=matrix,
                                                               capacidade=capacidade)},
                                 ignore_index=True)

            else:
                df10 = df10.append(
                    {'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                             capacidade=capacidade)}, ignore_index=True)

        if tarefas == 25 and ferramentas == 20 and capacidade == 10:
            if list(df11) == []:

                df11 = df11.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                  'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas,
                                                               matrix=matrix,
                                                               capacidade=capacidade)},
                                 ignore_index=True)

            else:
                df11 = df11.append(
                    {'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                             capacidade=capacidade)}, ignore_index=True)

        if tarefas == 25 and ferramentas == 20 and capacidade == 15:
            if list(df12) == []:

                df12 = df12.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                  'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas,
                                                               matrix=matrix,
                                                               capacidade=capacidade)},
                                 ignore_index=True)

            else:
                df12 = df12.append(
                    {'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                             capacidade=capacidade)}, ignore_index=True)

        if tarefas == 25 and ferramentas == 25 and capacidade == 10:
            if list(df13) == []:

                df13 = df13.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                  'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas,
                                                               matrix=matrix,
                                                               capacidade=capacidade)},
                                 ignore_index=True)

            else:
                df13 = df13.append(
                    {'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                             capacidade=capacidade)}, ignore_index=True)

        if tarefas == 25 and ferramentas == 25 and capacidade == 15:
            if list(df14) == []:

                df14 = df14.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                  'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas,
                                                               matrix=matrix,
                                                               capacidade=capacidade)},
                                 ignore_index=True)

            else:
                df14 = df14.append(
                    {'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                             capacidade=capacidade)}, ignore_index=True)

        if tarefas == 25 and ferramentas == 25 and capacidade == 20:
            if list(df15) == []:

                df15 = df15.append({'J': tarefas, 'T': ferramentas, 'C': capacidade,
                                  'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas,
                                                               matrix=matrix,
                                                               capacidade=capacidade)},
                                 ignore_index=True)

            else:
                df15 = df15.append(
                    {'Tamanho': executar.Execucao(tarefas=tarefas, ferramentas=ferramentas, matrix=matrix,
                                             capacidade=capacidade)}, ignore_index=True)



    if list(df1) != []:
        df1.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoD//teste1_D.csv', index=None,
                  header=True)
        print(df1)

    if list(df2) != []:
        df2.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoD//teste2_D.csv', index=None,
                   header=True)
        print(df2)

    if list(df3) != []:
        df3.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoD//teste3_D.csv', index=None,
                  header=True)

    if list(df4) != []:
        df4.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoD//teste4_D.csv', index=None,
                  header=True)

    if list(df5) != []:
        df5.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoD//teste5_D.csv', index=None,
                  header=True)

    if list(df6) != []:
        df6.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoD//teste6_D.csv', index=None,
                  header=True)

    if list(df7) != []:
        df7.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoD//teste7_D.csv', index=None,
                  header=True)

    if list(df8) != []:
        df8.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoD//teste8_D.csv', index=None,
                  header=True)

    if list(df9) != []:
        df9.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoD//teste9_D.csv', index=None,
                  header=True)


    if list(df10) != []:
        df10.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoD//teste10_D.csv', index=None,
                  header=True)

    if list(df11) != []:
        df11.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoD//teste11_D.csv', index=None,
                  header=True)


    if list(df12) != []:
        df12.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoD//teste12_D.csv', index=None,
                  header=True)


    if list(df13) != []:
        df13.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoD//teste13_D.csv', index=None,
                  header=True)


    if list(df14) != []:
        df14.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoD//teste14_D.csv', index=None,
                  header=True)


    if list(df15) != []:
        df15.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//GrupoD//teste15_D.csv', index=None,
                  header=True)