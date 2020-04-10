import os
import glob
import FuncaoLeitura as opter
import Execucao as executar
from pandas import DataFrame
import GrupoA as GrupoA
import GrupoB as GrupoB
import GrupoC as GrupoC
import GrupoD as GrupoD
import GrupoE as GrupoE


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
        "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\ChavesEtAl_2012\\ChavesEtAl_2012\\GrupoA"
    ]

    for folder in folder_path:

        # if folder == '//home//loop//Desktop//Teste_No_PC//Teste_No_PC//ChavesEtAl_2012//ChavesEtAl_2012//GrupoA':
        #     GrupoA.GrupoA(folder)
        #
        # if folder == '//home//loop//Desktop//Teste_No_PC//Teste_No_PC//ChavesEtAl_2012//ChavesEtAl_2012//GrupoB':
        #     GrupoB.GrupoB(folder)
        #
        # if folder == '//home//loop//Desktop//Teste_No_PC//Teste_No_PC//ChavesEtAl_2012//ChavesEtAl_2012//GrupoC':
        #     GrupoC.GrupoC(folder)
        #
        # if folder == '//home//loop//Desktop//Teste_No_PC//Teste_No_PC//ChavesEtAl_2012//ChavesEtAl_2012//GrupoD':
        #     GrupoD.GrupoD(folder)
        #
        # if folder == '//home//loop//Desktop//Teste_No_PC//Teste_No_PC//ChavesEtAl_2012//ChavesEtAl_2012//GrupoE':
        #     GrupoE.GrupoE(folder)

        if folder == "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\ChavesEtAl_2012\\ChavesEtAl_2012\\GrupoA":
            GrupoA.GrupoA(folder)

        # if folder == "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\ChavesEtAl_2012\\ChavesEtAl_2012\\GrupoB":
        #     GrupoB.GrupoB(folder)
        #
        # if folder == "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Teste_No_PC\\ChavesEtAl_2012\\ChavesEtAl_2012\\GrupoC":
        #     GrupoC.GrupoC(folder)
        #
        # if folder == "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Teste_No_PC\\ChavesEtAl_2012\\ChavesEtAl_2012\\GrupoD":
        #     GrupoD.GrupoD(folder)
        #
        # if folder == "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Teste_No_PC\\ChavesEtAl_2012\\ChavesEtAl_2012\\GrupoE":
        #     GrupoE.GrupoE(folder)
