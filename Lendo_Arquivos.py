import Executando_Projeto
import os

# import GrupoA as GrupoA
# import GrupoB as GrupoB
# import GrupoC as GrupoC
# import GrupoD as GrupoD
# import GrupoE as GrupoE


def Lendo_Arquivos():
    # Para teste em Linux
    # folder_path = ['//home//loop//Desktop//Teste_No_PC//Teste_No_PC//ChavesEtAl_2012//ChavesEtAl_2012//GrupoA',
    #                '//home//loop//Desktop//Teste_No_PC//Teste_No_PC//ChavesEtAl_2012//ChavesEtAl_2012//GrupoB',
    #                '//home//loop//Desktop//Teste_No_PC//Teste_No_PC//ChavesEtAl_2012//ChavesEtAl_2012//GrupoC',
    #                '//home//loop//Desktop//Teste_No_PC//Teste_No_PC//ChavesEtAl_2012//ChavesEtAl_2012//GrupoD',
    #                '//home//loop//Desktop//Teste_No_PC//Teste_No_PC//ChavesEtAl_2012//ChavesEtAl_2012//GrupoE',
    #                ]

    # Para teste em Windowns
    folder_path = [
    "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instâncias_divididas\\Yanasse\\tarefa9\\ferramentas25\\capacidade15"]


    for folder in folder_path:
        for root, dirs, files in os.walk(folder):
            for name in files:
                Executando_Projeto.executando_projeto(os.path.join(root, name),name)
