def Veficar_Grupo(filename, arquivo_de_instancias_lidas):
    instancias = open(arquivo_de_instancias_lidas, 'r')

    arquivo = []

    for i in instancias:
        arquivo.append(str(i))

    for i in range(len(arquivo)):
        if len(arquivo[i]) > 1:
            arquivo[i] = arquivo[i].split(
                "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instâncias_divididas\\")
            # arquivo[i] = arquivo[i][1].split(name)
            arquivo[i] = arquivo[i][1].rsplit('\n')
            arquivo[i] = arquivo[i][0]

    filename = str(filename).split(
        "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instâncias_divididas\\")

    if filename[1] in arquivo:
        return False
    else:
        return True


def Atualizar(filename, arquivo):
    instancias_lidas_A = open(
        arquivo, 'a+')
    instancias_lidas_A.write(filename + '\n')
    instancias_lidas_A.close()

def arquivo_de_resultado(filename,name):
    filename = str(filename).split(
        "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Instâncias_divididas\\")

    filename = filename[1].rsplit(name)
    filename = filename[0]

    path = "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\Resultados\\" + filename + "resultado.csv"

    return path