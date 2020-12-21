import sys, random, string
from typing import ChainMap
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QComboBox, \
    QPushButton, QLineEdit, QLabel


father = []
mother = []

son_1 = []
son_2 = []


def rand(int):
    lista = []

    if int == 1:
        while len(lista) != 10:
            inserir = 0
            aux = random.choice(string.ascii_uppercase)
            for j in range(len(lista)):
                if (aux != lista[j]):
                    inserir += 1
            if inserir == len(lista):
                lista.append(str(aux))
           
    elif int == 2:
        while len(lista) != 10:
            inserir = 0
            aux = random.choice(string.ascii_lowercase)
            for j in range(len(lista)):
                if (aux != lista[j]):
                    inserir += 1
            if inserir == len(lista):
                lista.append(str(aux))
                       
    elif int == 3:
        while len(lista) != 10:
            inserir = 0
            aux = random.choice(string.digits)
            for j in range(len(lista)):
                if (aux != lista[j]):
                    inserir += 1
            if inserir == len(lista):
                lista.append(str(aux))
    
    elif int == 4:
        for i in range(10):
            lista.append(str(random.randint(0,1)))
    
    return lista

            
def random_input():
    global father, mother
    if method_combo_box.currentText() == "PMX":
        method = random.randint(1,3)
        if method == 1:
            father = rand(1)
            mother = rand(1)
        elif method == 2:
            father = rand(2)
            mother = rand(2)
        elif method == 3:
            father = rand(3)
            mother = rand(3)
    else:
        father = rand(4)
        mother = rand(4)

    m = ''.join(mother)
    f = ''.join(father)
    mother_line_edit.setText(str(m))
    father_line_edit.setText(str(f))


def on_cross_pushbutton_clicked():
    if method_combo_box.currentText() == "Corte Simples":
        offsprings = simple_cut_crossover()
        
    else:
        offsprings = pmx_crossover()
    

    son1_label_1.setText(offsprings[0])
    son1_label_2.setText(offsprings[1])
    son1_label_3.setText(offsprings[2])
    son2_label_1.setText(offsprings[3])
    son2_label_2.setText(offsprings[4])
    son2_label_3.setText(offsprings[5])


def on_method_combobox_current_text_changed():
    if method_combo_box.currentText() == "PMX":
        father_line_edit.setInputMask('NNNNNNNNNN')
        father_line_edit.setText('0123456789')
        mother_line_edit.setInputMask('NNNNNNNNNN')
        mother_line_edit.setText('9876543210')
    else:
        father_line_edit.setInputMask('BBBBBBBBBB')
        father_line_edit.setText('0000000000')
        mother_line_edit.setInputMask('BBBBBBBBBB')
        mother_line_edit.setText('1111111111')
    return '','','','','',''

def pmx_crossover():
    global son_1, son_2
    father = list(father_line_edit.text())
    mother = list(mother_line_edit.text())
    son1 = []
    son2 = []

    corte1 =random.randint(4,6)
    for i in range(corte1):
        son1.append(str(mother[i]))
        son2.append(str(father[i]))
    
    corte2 = int(corte1/2)
    for i in range(corte2):
        son1.append(str(father[corte1+i]))
        son2.append(str(mother[corte1+i]))

    corte3 = int(10 - corte1 - corte2)
    for i in range(corte3):
        son1.append(str(mother[i+corte1+corte2]))
        son2.append(str(father[i+corte1+corte2]))

    son1 = verificar_repeticao(son1,father,mother)
    son2 = verificar_repeticao(son2,father,mother)  
    son_1 = son1
    son_2 = son2

    son1 = "".join(son1)
    son2 = "".join(son2)
    
    return son1[0:corte1], son1[corte1:corte1+corte2], son1[corte1+corte2:10], son2[0:corte1], son2[corte1:corte1+corte2], son2[corte1+corte2:10]


def verificar_repeticao(son,father,mother):

    aux = []
    pos = 0

    for item in father:
        if item not in son:
            aux.append(str(item))

    for item in mother:
        if item not in son:
            aux.append(str(item))

    

    for i in range(len(son)):
        aux2 = son[i]
        for y in range(len(son)):
            if (aux2 == son[y])and(y != i):
                son[y] = aux[pos]
                pos += 1

    return son


def simple_cut_crossover():
    global son_1, son_2
    father = list(father_line_edit.text())
    mother = list(mother_line_edit.text())
    son1 = []
    son2 = []

    corte1 =random.randint(2,6)
    for i in range(corte1):
        son1.append(str(mother[i]))
        son2.append(str(father[i]))
    
    corte2 = int(corte1/2)
    for i in range(corte2):
        son1.append(str(father[corte1+i]))
        son2.append(str(mother[corte1+i]))

    corte3 = int(10 - corte1 - corte2)
    for i in range(corte3):
        son1.append(str(mother[i+corte1+corte2]))
        son2.append(str(father[i+corte1+corte2]))

    mutacao = random.randint(0,9)
    if mutacao == 5:
        pos = random.randint(0,9)
        if son1[pos] == '1':
            son1[pos] = '0'
        else:
            son1[pos] = '1'

        pos = random.randint(0,9)
        if son2[pos] == '1':
            son2[pos] = '0'
        else:
            son2[pos] = '1'

    son_1 = son1
    son_2 = son2
    

    son1 = "".join(son1)
    son2 = "".join(son2)
    
    return son1[0:corte1], son1[corte1:corte1+corte2], son1[corte1+corte2:10], son2[0:corte1], son2[corte1:corte1+corte2], son2[corte1+corte2:10]

def trocar_pais():
    global father, mother, son_1, son_2

    father = son_1
    mother = son_2

    m = ''.join(son_2)
    f = ''.join(son_1)
    mother_line_edit.setText(str(m))
    father_line_edit.setText(str(f))


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)

    # Loading widgets elements from ui file
    window = uic.loadUi("crossover_operation.ui")
    window.show()

    # Getting widgets elements
    father_line_edit = window.findChild(QLineEdit, 'fatherLineEdit')
    mother_line_edit = window.findChild(QLineEdit, 'motherLineEdit')
    son1_label_1 = window.findChild(QLabel, 'son1Label1')
    son1_label_2 = window.findChild(QLabel, 'son1Label2')
    son1_label_3 = window.findChild(QLabel, 'son1Label3')

    son2_label_1 = window.findChild(QLabel, 'son2Label1')
    son2_label_2 = window.findChild(QLabel, 'son2Label2')
    son2_label_3 = window.findChild(QLabel, 'son2Label3')
    method_combo_box = window.findChild(QComboBox, 'methodComboBox')
    cross_push_button = window.findChild(QPushButton, 'crossPushButton')
    aleatorizar = window.findChild(QPushButton, 'Aleatorizar')
    subir_filhos = window.findChild(QPushButton, 'subirF')

    # Connecting
    cross_push_button.clicked.connect(on_cross_pushbutton_clicked)
    method_combo_box.currentTextChanged.connect(on_method_combobox_current_text_changed)
    aleatorizar.clicked.connect(random_input)
    subir_filhos.clicked.connect(trocar_pais)
    
    sys.exit(app.exec_())
