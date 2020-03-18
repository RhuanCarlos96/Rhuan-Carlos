from pandas import DataFrame
import glob
import FuncaoLeitura as opter
import Execucao as executar
import os


def GrupoA(folder):
    print('Grupo A')
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

        tamanho, melhor_solucao, melhor_tempo, media, desvio_padrao = executar.Execucao(tarefas=tarefas,
                                                                                        ferramentas=ferramentas,
                                                                                        matrix=matrix,
                                                                                        capacidade=capacidade)
        if (tarefas == 8) and (ferramentas == 15) and (capacidade == 5):
            if list(df1) == []:
                df1 = df1.append({'J': tarefas, 'T': ferramentas, 'C': capacidade, 'Tamanho da população': tamanho,
                                  'NT': melhor_solucao, 'Tempo': melhor_tempo, 'Media': media,
                                  'Desvio Padrao': desvio_padrao}, ignore_index=True)

            else:
                df1 = df1.append({'Tamanho da população': tamanho,
                                  'NT': melhor_solucao, 'Tempo': melhor_tempo, 'Media': media,
                                  'Desvio Padrao': desvio_padrao}, ignore_index=True)

        if tarefas == 8 and ferramentas == 15 and capacidade == 10:
            if list(df2) == []:

                df2 = df2.append({'J': tarefas, 'T': ferramentas, 'C': capacidade, 'Tamanho da população': tamanho,
                                  'NT': melhor_solucao, 'Tempo': melhor_tempo, 'Media': media,
                                  'Desvio Padrao': desvio_padrao}, ignore_index=True)

            else:
                df2 = df2.append({'Tamanho da população': tamanho,
                                  'NT': melhor_solucao, 'Tempo': melhor_tempo, 'Media': media,
                                  'Desvio Padrao': desvio_padrao}, ignore_index=True)

        if tarefas == 8 and ferramentas == 20 and capacidade == 5:
            if list(df3) == []:

                df3 = df3.append({'J': tarefas, 'T': ferramentas, 'C': capacidade, 'Tamanho da população': tamanho,
                                  'NT': melhor_solucao, 'Tempo': melhor_tempo, 'Media': media,
                                  'Desvio Padrao': desvio_padrao}, ignore_index=True)

            else:
                df3 = df3.append({'Tamanho da população': tamanho,
                                  'NT': melhor_solucao, 'Tempo': melhor_tempo, 'Media': media,
                                  'Desvio Padrao': desvio_padrao}, ignore_index=True)

        if tarefas == 8 and ferramentas == 20 and capacidade == 10:
            if list(df4) == []:

                df4 = df4.append({'J': tarefas, 'T': ferramentas, 'C': capacidade, 'Tamanho da população': tamanho,
                                  'NT': melhor_solucao, 'Tempo': melhor_tempo, 'Media': media,
                                  'Desvio Padrao': desvio_padrao}, ignore_index=True)
            else:
                df4 = df4.append({'Tamanho da população': tamanho,
                                  'NT': melhor_solucao, 'Tempo': melhor_tempo, 'Media': media,
                                  'Desvio Padrao': desvio_padrao}, ignore_index=True)

        if tarefas == 8 and ferramentas == 20 and capacidade == 15:
            if list(df5) == []:

                df5 = df5.append({'J': tarefas, 'T': ferramentas, 'C': capacidade, 'Tamanho da população': tamanho,
                                  'NT': melhor_solucao, 'Tempo': melhor_tempo, 'Media': media,
                                  'Desvio Padrao': desvio_padrao}, ignore_index=True)

            else:
                df5 = df5.append({'Tamanho da população': tamanho,
                                  'NT': melhor_solucao, 'Tempo': melhor_tempo, 'Media': media,
                                  'Desvio Padrao': desvio_padrao}, ignore_index=True)

        if tarefas == 8 and ferramentas == 25 and capacidade == 5:
            if list(df6) == []:

                df6 = df6.append({'J': tarefas, 'T': ferramentas, 'C': capacidade, 'Tamanho da população': tamanho,
                                  'NT': melhor_solucao, 'Tempo': melhor_tempo, 'Media': media,
                                  'Desvio Padrao': desvio_padrao}, ignore_index=True)

            else:
                df6 = df6.append({'Tamanho da população': tamanho,
                                  'NT': melhor_solucao, 'Tempo': melhor_tempo, 'Media': media,
                                  'Desvio Padrao': desvio_padrao}, ignore_index=True)

        if tarefas == 8 and ferramentas == 25 and capacidade == 10:
            if list(df7) == []:

                df7 = df7.append({'J': tarefas, 'T': ferramentas, 'C': capacidade, 'Tamanho da população': tamanho,
                                  'NT': melhor_solucao, 'Tempo': melhor_tempo, 'Media': media,
                                  'Desvio Padrao': desvio_padrao}, ignore_index=True)
            else:
                df7 = df7.append({'Tamanho da população': tamanho,
                                  'NT': melhor_solucao, 'Tempo': melhor_tempo, 'Media': media,
                                  'Desvio Padrao': desvio_padrao}, ignore_index=True)

        if tarefas == 8 and ferramentas == 25 and capacidade == 15:
            if list(df8) == []:

                df8 = df8.append({'J': tarefas, 'T': ferramentas, 'C': capacidade, 'Tamanho da população': tamanho,
                                  'NT': melhor_solucao, 'Tempo': melhor_tempo, 'Media': media,
                                  'Desvio Padrao': desvio_padrao}, ignore_index=True)

            else:
                df8 = df8.append({'Tamanho da população': tamanho,
                                  'NT': melhor_solucao, 'Tempo': melhor_tempo, 'Media': media,
                                  'Desvio Padrao': desvio_padrao}, ignore_index=True)

        if tarefas == 8 and ferramentas == 25 and capacidade == 20:
            if list(df9) == []:

                df9 = df9.append({'J': tarefas, 'T': ferramentas, 'C': capacidade, 'Tamanho da população': tamanho,
                                  'NT': melhor_solucao, 'Tempo': melhor_tempo, 'Media': media,
                                  'Desvio Padrao': desvio_padrao}, ignore_index=True)
            else:
                df9 = df9.append({'Tamanho da população': tamanho,
                                  'NT': melhor_solucao, 'Tempo': melhor_tempo, 'Media': media,
                                  'Desvio Padrao': desvio_padrao}, ignore_index=True)

    if list(df1) != []:
        df1.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//Grupo A//teste1_A.csv', index=None,
                   header=True)
        print('Grupo 1 finalizado!!')

    if list(df2) != []:
        df2.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//Grupo A//teste2_A.csv', index=None,
                   header=True)
        print('Grupo 2 finalizado!!')

    if list(df3) != []:
        df3.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//Grupo A//teste3_A.csv', index=None,
                   header=True)
        print('Grupo 3 finalizado!!')

    if list(df4) != []:
        df4.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//Grupo A//teste4_A.csv', index=None,
                   header=True)
        print('Grupo 4 finalizado!!')

    if list(df5) != []:
        df5.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//Grupo A//teste5_A.csv', index=None,
                   header=True)
        print('Grupo 5 finalizado!!')

    if list(df6) != []:
        df6.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//Grupo A//teste6_A.csv', index=None,
                   header=True)
        print('Grupo 6 finalizado!!')

    if list(df7) != []:
        df7.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//Grupo A//teste7_A.csv', index=None,
                   header=True)
        print('Grupo 7 finalizado!!')

    if list(df8) != []:
        df8.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//Grupo A//teste8_A.csv', index=None,
                   header=True)
        print('Grupo 8 finalizado!!')

    if list(df9) != []:
        df9.to_csv('//home//loop//Desktop//Teste_No_PC//Resultados//Grupo A//teste9_A.csv', index=None,
                   header=True)
        print('Grupo 9 finalizado!!')

        print(df9)
