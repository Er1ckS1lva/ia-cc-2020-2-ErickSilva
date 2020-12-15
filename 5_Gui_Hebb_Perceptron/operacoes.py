
def percp(x1,x2,peso):
    teta = 0     
    somatorio = 0
    
    somatorio += int(peso[2])
    somatorio += int(x1) * int(peso[0]) 
    somatorio += int(x2) * int(peso[1])

    if(somatorio >= teta):
        y = 1
    elif((somatorio>=-teta)and(somatorio<=teta)):
        y = 0
    elif(somatorio < -teta):
        y = -1

    return y


def hebb(x1,x2,peso):
    
    saida = int(peso[0]/x1)/int(peso[1]/x2)
    print(saida)
    return saida
            