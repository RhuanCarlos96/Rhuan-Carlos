import os
import shutil
import random
import FuncaoLeitura
import pandas as pd

# Abrindo arquivos para teste:

def Lendo_Instancias():
    folder_path = ["C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instances\\Crama"]

    arquivos_para_instâncias = []
    for folder in folder_path:
        for root, dirs, files in os.walk(folder):
            for name in files:
                arquivos_para_instâncias.append(os.path.join(root, name))

    print(len(arquivos_para_instâncias))
    print(len(arquivos_para_instâncias) * 0.05)

    faixa = list(range(0, len(arquivos_para_instâncias)))
    escolhidos = []
    while len(escolhidos) < int(len(arquivos_para_instâncias) * 0.05):
        aux = random.choice(faixa)

        while aux in escolhidos:
            aux = random.choice(faixa)

        escolhidos.append(aux)

        for i in escolhidos:
            shutil.copy(arquivos_para_instâncias[i],
                        "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instancias_para_ajustes")


def Separando_Instancias():
    folder_path = ["C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instances\\Crama"]

    # "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instances\\Yanasse",
    # "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instances\\Mecler",
    # "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instances\\Catanzaro"

    arquivos_para_instâncias = []
    for folder in folder_path:
        for root, dirs, files in os.walk(folder):
            for name in files:
                arquivos_para_instâncias.append(os.path.join(root, name))

    caminhos = []
    for i in arquivos_para_instâncias:
        with open(i, 'r') as f:
            tarefas, ferramentas, capacidade, matrix = FuncaoLeitura.instancias(
                f)  # optendo todos os valores de instâncias recolhidas em um determinado arquivo

        path = "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instâncias_divididas\\Crama" + "\\tarefa" + str(
            tarefas) + "\\ferramentas" + str(ferramentas) + "\\capacidade" + str(capacidade)

        if path not in caminhos:
            os.makedirs(path)
            caminhos.append(path)

    for i in arquivos_para_instâncias:
        with open(i, 'r') as f:
            tarefas, ferramentas, capacidade, matrix = FuncaoLeitura.instancias(
                f)  # optendo todos os valores de instâncias recolhidas em um determinado arquivo

        path = "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instâncias_divididas\\Crama" + "\\tarefa" + str(
            tarefas) + "\\ferramentas" + str(ferramentas) + "\\capacidade" + str(capacidade)

        shutil.copy(i, path)


def geradndo_arquivo_de_resultados():
    folder_path = ["C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instances\\Yanasse\\Tabela5"]

    # "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instances\\Yanasse",
    # "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instances\\Mecler",
    # "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instances\\Catanzaro"

    arquivos_para_instâncias = []
    for folder in folder_path:
        for root, dirs, files in os.walk(folder):
            for name in files:
                arquivos_para_instâncias.append(os.path.join(root, name))

    caminhos = []
    for i in arquivos_para_instâncias:
        with open(i, 'r') as f:
            tarefas, ferramentas, capacidade, matrix = FuncaoLeitura.instancias(
                f)  # optendo todos os valores de instâncias recolhidas em um determinado arquivo

        path = "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Resultados\\Yanasse\\Tabela5" + "\\tarefa" + str(
            tarefas) + "\\ferramentas" + str(ferramentas) + "\\capacidade" + str(capacidade)

        if path not in caminhos:
            os.makedirs(path)
            caminhos.append(path)

    d = [' |J|' , ' |T| ', ' |C| ', ' Melhor Troca ', 'Media da Melhor Troca' , ' Tempo' , 'Media de Tempo' ,' Desvio Padrao' ]
    df = pd.DataFrame(columns=d)

    for i in caminhos:
        df.to_csv(i +"\\resultado.csv" , index=None,
                 header=True)





