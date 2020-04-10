def Veficar_Grupo(filename, arquivo, grupo):
    instancias = open(arquivo, 'r')

    arquivo = []

    for i in instancias:
        arquivo.append(i)

    for i in range(len(arquivo)):
        if len(arquivo[i]) > 1:
            arquivo[i] = arquivo[i].split(
                "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\ChavesEtAl_2012\\ChavesEtAl_2012" + grupo)
            arquivo[i] = arquivo[i][1]
            arquivo[i] = arquivo[i].rstrip('\n')

    filename = str(filename).split(
        "C:\\Users\\Rhuan\\Desktop\\Teste_No_PC\\Teste_No_PC\\ChavesEtAl_2012\\ChavesEtAl_2012" + grupo)
    filename = filename[1]

    if filename in arquivo:
        return False
    else:
        return True


def Atualizar(filename, arquivo):
    instancias_lidas_A = open(
        arquivo, 'a+')
    instancias_lidas_A.write(filename + '\n')
    instancias_lidas_A.close()
