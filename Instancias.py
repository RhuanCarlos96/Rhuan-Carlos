import os
import shutil
import random


# Abrindo arquivos para teste:

def Lendo_Instancias():
    folder_path = \
        ["C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instances\\Catanzaro",
         "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instances\\Yanasse",
         "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instances\\Crama",
         "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instances\\Mecler",
         ]

    arquivos_para_instâncias = []
    for folder in folder_path:
        for root, dirs, files in os.walk(folder):
            for name in files:
                arquivos_para_instâncias.append(os.path.join(root, name))

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
