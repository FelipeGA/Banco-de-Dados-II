import pandas as pd


#Q1 = pd.read_csv("Resultado_Query1.csv")
#Q2 = pd.read_csv("Resultado_Query2.csv")
#Q3 = pd.read_csv("Resultado_Query3.csv")
#Q4 = pd.read_csv("Resultado_Query4.csv")
Q5 = pd.read_csv("Resultado_Query5.csv")


def ReputationMean():
    locais = []
    Occur = []
    for i in Q5.iloc[:,1:2].values:
        locais.append(str(i))
    
    for i in Q5.iloc[:,:1].values:
        Occur.append(int(i))
    
    
    
    BeforeComma = []
    AfterComma = []
    #preprocessamento   
    tmp = "[]'"
    for i in range(len(locais)):
        for j in range(len(tmp)):
            locais[i] = locais[i].replace(tmp[j], "")
        BeforeComma.append(locais[i])
        AfterComma.append("")
    
    #Separando Antes e Depois da virgula
    tmp = []
    for i in range(len(BeforeComma)):
        if ',' in BeforeComma[i]:
            for k in range(len(BeforeComma[i])-3):
                if BeforeComma[i][k] == ',':
                    tmp.append(BeforeComma[i][:k])
                    AfterComma[i] = BeforeComma[i][k+2:]
                    break
        else:
            tmp.append(BeforeComma[i])
    
    BeforeComma = tmp
    del(tmp)
    del(locais)
    
    #Segunda Separação de virgulas
    
    for i in range(len(AfterComma)):
        if ',' in AfterComma[i]:
            for j in range(len(AfterComma[i])):
                if AfterComma[i][j] == ',':
                    AfterComma[i] = AfterComma[i][j+2:]
                    break
    
    medias = []
    for i in Q5.iloc[:,2:].values:
        medias.append(str(i))
    
    for i in range(len(medias)):
        tmp="[]"
        for j in tmp:
            medias[i] = medias[i].replace(j, "")
        medias[i] = float(medias[i])
    
    
    #Fim Preprocessamento
    
    BeforeComma.append("EOF")
    medias.append(-1)
    AfterComma.append("EOF")
    Occur.append(-1)
    Final = []
    for i in range(len(BeforeComma)):
        tmp = []    
        for j in range(1):
            tmp.append(BeforeComma[i])
            tmp.append(medias[i])
            tmp.append(Occur[i])
        Final.append(tmp)
    
            
    
    
    Final2 = []
    for i in range(133):
        tmp = []    
        for j in range(1):
            tmp.append(i)
            tmp.append('')
            tmp.append('cont')
            tmp.append('Occur')
        Final2.append(tmp)
    
    for i in range(len(Final)):
        Final2[i][1] = Final[i][1]
        Final2[i][3] = Final[i][2]
    #####################################
    
    i=0
    while Final[i][0] != 'EOF':
        cont = 0
        for j in range(len(AfterComma)):
            if Final[i][0] == AfterComma[j]:
                Final2[i][0] = AfterComma[j]
                #Final2[i][1] = Final[i][1]
                print("{}, @{} Achei".format(Final[i][0], j))
                cont += 1
                Final2[i][1] += Final[j][1]
                Final2[i][3] += Final[j][2]
                
    #                del(Final[j])
                continue
        Final2[i][2] = cont
        i+=1
    #####################################
    
    ReputationByLocal = []
    for i in range(len(Final2)):
        if type(Final2[i][0]) == str:
            Final2[i][1] = round(Final2[i][1]/Final2[i][2],2)
            ReputationByLocal.append(Final2[i])
    
    
    for i in ReputationByLocal:
        del(i[2])
        if type(i[0]) == str:
            del(i)


    return ReputationByLocal


x = ReputationMean()


































