treino_inicial = []
arquivo = open(r'4_Perceptron\entradas.txt', 'r')

for linhas in arquivo:
    vetor_entradas = linhas.split(',')
    treino_inicial.append(vetor_entradas)

pesos = []

for i in range(len(treino_inicial[0])-1):
    pesos.append(0)


saida_esperada = []

for i in range(len(treino_inicial)):
    saida_esperada.append(treino_inicial[i][len(treino_inicial[i])-1])

pesos = [0,0,0]
alfa = 1
teta = 0
teste =0
epocas = 0

aprendendo = True

while(aprendendo):
        epocas+=1
        teste = 0
        for i in range(len(treino_inicial)):
            somatorio = 0
            somatorio += int(pesos[2])
            for j in range(len(treino_inicial[i])-1):
                somatorio += int(treino_inicial[i][j]) * int(pesos[j])                              

            if(somatorio > teta):
                y = 1
            elif((somatorio>=-teta)and(somatorio<=teta)):
                y = 0
            elif(somatorio < -teta):
                y = -1

            if(int(saida_esperada[i]) == y):
                teste += 1
                if teste == 1:
                    aprendendo = False
            else:
                tamanho = len(pesos)
                for j in range(tamanho):
                    if j == 2:
                        pesos[j] = int(pesos[j])+(alfa*int(saida_esperada[i]))
                    else:
                        pesos[j] = int(pesos[j]) + (alfa*int(saida_esperada[i])*int(treino_inicial[i][j]))
            print('\nEntradas=',treino_inicial[i],'Saida=',saida_esperada[i],'Pesos=',pesos)
        epocas += 1
        print('Epocas = '+str(epocas))