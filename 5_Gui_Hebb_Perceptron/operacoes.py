
def percp(x1,x2,baias,peso):
    alfa = 1     
    somatorio = 0
 
    somatorio += int(x1) * int(peso[0]) 
    somatorio += int(x2) * int(peso[1])                            
    somatorio += int(baias)
            
    if(somatorio > alfa):
        y = 1
    elif((somatorio>=-alfa)and(somatorio<=alfa)):
        y = 0
    elif(somatorio < -alfa):
        y = -1
    return y


def hebb(x1,x2,baias,peso):
    
    saida = int(peso[0]/x1)/int(peso[1]/x2)
    print(saida)
    return saida
            