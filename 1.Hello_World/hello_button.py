from PyQt5.QtWidgets import QApplication, QPushButton

def say_hello():
    print("Button clicked, Hello!")

if __name__ == "__main__":

    app = QApplication([])

    button = QPushButton("Click me")
    button.clicked.connect(say_hello)
    button.show()

    app.exec_()
    
