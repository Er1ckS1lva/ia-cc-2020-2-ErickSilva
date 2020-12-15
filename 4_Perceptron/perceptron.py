entradas = []
arquivo = open(r'4_Perceptron\entradas.txt', 'r')

for linhas in arquivo:
    vetor_entradas = linhas.split(',')
    entradas.append(vetor_entradas)

pesos = []

for i in range(len(entradas[0])-1):
    pesos.append(0)


saidas = []

for i in range(len(entradas)):
    saidas.append(entradas[i][len(entradas[i])-1])

alfa = 1
aprendendo = True
epocas = 0


while(aprendendo):
    epocas += 1
    for i in range(len(entradas)):
        
        somatorio = 0
        x = []
        for j in range(len(entradas[i])-2):
            somatorio+= int(entradas[i][j]) * int(pesos[j])
            x.append(entradas[i][j])
            
        somatorio += int(entradas[i][len(entradas[i])-2])
        x.append(entradas[i][len(entradas[i])-2])

        if(somatorio > alfa):
            y = 1
        elif((somatorio>=-alfa)and(somatorio<=alfa)):
            y = 0
        elif(somatorio < -alfa):
            y = -1
        
        if(int(saidas[i]) == y):
            aprendendo = False
        else:
            tamanho = len(pesos)
            for j in range(tamanho):
                pesos[j] = int(pesos[j]) + (alfa*int(saidas[j])*somatorio)
                if j == tamanho-1:
                    pesos[j] = int(pesos[j])+(alfa*int(saidas[j]))

        print('\nEntradas=',x,'Saida=',saidas[i],'Pesos=',pesos)
epocas += 1
print('Epocas = '+str(epocas))