entradas = []
arquivo = open('entradas.txt', 'r')
for linhas in arquivo:
    vetor_entradas = linhas.split(',')
    entradas.append(vetor_entradas)

pesos = []


for i in range(len(entradas[0])-1):
    pesos.append(0)


saidas = []

for i in range(len(entradas)):
    saidas.append(entradas[i][len(entradas[i])-1])

for i in range(len(entradas)):
    x = []
    for j in range(len(entradas[i])-1):
        x.append(entradas[i][j])
        y = saidas[i]
        pesos[j] = pesos[j] + (int(x[j])*int(y))
        
    print('\nEntradas=',x,'Saida=',saidas[i],'Pesos=',pesos)
    
