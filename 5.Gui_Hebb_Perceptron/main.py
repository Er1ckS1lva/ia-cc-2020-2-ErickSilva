from PyQt5 import QtCore, uic, QtWidgets
from PyQt5.QtWidgets import QAction, QApplication, QLabel,QPushButton,QRadioButton, QSpinBox
import operacoes

#(x1,x2,baias)
treino_inicial = [(1,1,1),(1,-1,1),(-1,1,1),(-1,-1,1)]
epocas = 0
saida_esperada = [1,-1,-1,-1]
pesos = [0,0,0]
hebb_bol = True

def treino():
    global hebb_bol
    if hebb_bol:
        hebb()
    else:
        perceptroon()


def hebb_check():
    global hebb_bol
    hebb_bol = True

def percep_check():
    global hebb_bol
    hebb_bol = False

def hebb():
    epoca.setVisible(False)
    global treino_inicial,saida_esperada,pesos
    pesos = [0,0,0]
    for i in range(len(treino_inicial)):
        for j in range(len(treino_inicial[i])-1):      
            pesos[j] = pesos[j] + (int(treino_inicial[i][j])*int(saida_esperada[i]))
        pesos[2] = pesos[2] + int(saida_esperada[i])
    
    pesos_values_1.setText('w1 = '+str(pesos[0]))
    pesos_values_2.setText('w2 = '+str(pesos[1]))
    pesos_values_baias.setText('wb = '+str(pesos[2]))

def perceptroon():
    global treino_inicial,saida_esperada,pesos,epocas
    epoca.setVisible(True)
    epoca.setText('Epocas = '+str(epocas))
    epocas = 0
    pesos = [0,0,0]
    alfa = 1
    
    aprendendo = True
    while(aprendendo):
        epocas+=1
        for i in range(len(treino_inicial)):
            somatorio = 0
            y=-1     
            for j in range(len(treino_inicial[i])-1):
                somatorio += int(treino_inicial[i][j]) * int(pesos[j])                              
            somatorio += int(treino_inicial[i][2])
            
            if(somatorio > alfa):
                y = 1
            elif((somatorio>=-alfa)and(somatorio<=alfa)):
                y = 0
            elif(somatorio < -alfa):
                y = -1
            
            if(int(saida_esperada[i]) == y):
                aprendendo = False
            else:
                tamanho = len(pesos)
                for j in range(tamanho):
                    pesos[j] = int(pesos[j]) + (alfa*int(saida_esperada[j])*somatorio)
                    if j == tamanho-1:
                        pesos[j] = int(pesos[j])+(alfa*int(saida_esperada[j]))

    
    pesos_values_1.setText('w1 = '+str(pesos[0]))
    pesos_values_2.setText('w2 = '+str(pesos[1]))
    pesos_values_baias.setText('wb = '+str(pesos[2]))
    epoca.setText('Epocas = '+str(epocas))


def operar():

    global pesos
    x1 = entrada1.value()
    x2 = entrada2.value()
  
    if hebb_.isChecked():
        operacoes.opr(1,x1,x2,pesos)
    elif percep.isChecked():
        operacoes.opr(2,x1,x2,pesos)




if __name__ == "__main__":

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication([])

    Pyqt = uic.loadUi(r"5.Gui_Hebb_Perceptron\Ui\layout.ui")
    
    #Labels
    epoca = Pyqt.findChild(QLabel, 'epoca')
    epoca.setVisible(False)
    aprendizado = Pyqt.findChild(QLabel, 'aprendizado')
    treinamento = Pyqt.findChild(QLabel, 'treinamento')
    treinamento_text = Pyqt.findChild(QLabel, 'inputs_t')
    treinamento_text2 = Pyqt.findChild(QLabel, 'outputs')
    input_treinamento = Pyqt.findChild(QLabel, 'Input_value')
    input_treinamento.setText(str(treino_inicial))
    output_treinamento = Pyqt.findChild(QLabel, 'outpu_values')
    output_treinamento.setText(str(saida_esperada))
    peso_text = Pyqt.findChild(QLabel, 'pesos_label')
    pesos_values_1 = Pyqt.findChild(QLabel, 'peso1')
    pesos_values_2 = Pyqt.findChild(QLabel, 'peso2')
    pesos_values_baias = Pyqt.findChild(QLabel, 'pesobaias')
    rodando = Pyqt.findChild(QLabel, 'rodando')
    resultado = Pyqt.findChild(QLabel, 'resultado')
    dados = Pyqt.findChild(QLabel, 'dado')

    #Butões
    treinar = Pyqt.findChild(QPushButton,'treinar_but')
    treinar.clicked.connect(treino)

    testar = Pyqt.findChild(QPushButton,'testar')
    testar.clicked.connect(operar)

    hebb_ = Pyqt.findChild(QRadioButton,'hebb')
    hebb_.setChecked(1)
    hebb_.toggled.connect(hebb_check)
    percep = Pyqt.findChild(QRadioButton,'percep')
    percep.toggled.connect(percep_check)

    entrada1 = Pyqt.findChild(QSpinBox,'dado1')
    entrada2 = Pyqt.findChild(QSpinBox,'dado2')

    Pyqt.show()
    app.exec_()