from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QLabel, \
    QPushButton, QAction, QSpinBox


def dinheiro_pessoa_risco():

    money = Quantidade_Dinheiro.value()

    if money == 0:
        pouco = 0
        razoavel = 0
        adequado = 0

    elif (0<money)and(money<=30):
        pouco = 1
        razoavel = 0
        adequado = 0

    elif (money > 30)and(money<50):
        pouco = (50-money)/(50-30)
        razoavel = (money-30)/(50-30)
        adequado = 0
        
    elif money >= 70:
        pouco = 0
        razoavel = 0
        adequado = 1

    elif money == 50:
        pouco = 0
        adequado = 0
        razoavel = 1
        
    elif (money > 50)and(money < 70):
        razoavel = (70-money)/(70-50)
        adequado = (money-50)/(70-50)
        pouco = 0

    people = Quantidade_Pessoa.value()

    if people == 0:
        insuficiente = 0
        satisfatorio = 0
    
    elif people >= 70:
        insuficiente = 0
        satisfatorio = 1

    elif (people > 0)and(people <= 30):
        insuficiente = 1
        satisfatorio = 0

    elif (people > 30)and(people < 70):
        insuficiente = (70-people)/(70-30)
        satisfatorio = (people - 30)/(70-30)

    risco_total(pouco, razoavel, adequado, insuficiente, satisfatorio)


def risco_total(pouco, razoavel, adequado, insuficiente, satisfatorio):
    
    if (pouco >= insuficiente) and (pouco >= satisfatorio):
        alto = pouco
  
    else:
        if (insuficiente <= satisfatorio):
            alto = insuficiente

        else:
            alto = satisfatorio
 
    if razoavel <= satisfatorio:
        medio = razoavel
    else:
        medio = satisfatorio

    if adequado <= satisfatorio:
        baixo = adequado
    else: 
        baixo = satisfatorio

    soma = 0
    divisor = 0

    if baixo > 0:
        soma += 60 * baixo
        divisor += 3*baixo
    
    if medio > 0:
        soma += 150 * medio
        divisor += 3*medio
    
    if alto > 0:
        soma += 240 * alto
        divisor += 3*alto

    risco_final = soma/divisor
    show(risco_final)


def show(risco_final):
    if (risco_final <= 35):
        Resultado.setText('Baixo : ' + str(risco_final))
        Resultado.setVisible(True)
    elif(risco_final > 35)and(risco_final <= 65):
        Resultado.setText('Mediano : ' + str(risco_final))
        Resultado.setVisible(True)
    elif(risco_final > 65):
        Resultado.setText('Alto : ' + str(risco_final))
        Resultado.setVisible(True)


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication([])

    window = uic.loadUi(r"ia-cc-2020-2-ErickSilva\2.Logica_Fuzzy\Trab_Saulo.ui")

    Dinheiro = window.findChild(QLabel, 'Dinheiro')
    Quantidade_Dinheiro = window.findChild(QSpinBox, 'QuantDinheiro')

    Pessoa = window.findChild(QLabel, 'Pessoa')
    Quantidade_Pessoa = window.findChild(QSpinBox, 'QuantPesssoa')

    Risco = window.findChild(QLabel, 'Risco')
    Resultado = window.findChild(QLabel, 'Resultado')
    Resultado.setVisible(False)

    Calcular = window.findChild(QPushButton, 'Calcular')
    Calcular.clicked.connect(dinheiro_pessoa_risco)
    

    window.show()

    app.exec_()