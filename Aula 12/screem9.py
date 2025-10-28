from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

def botao_clique():
    print("Saudades")
    
app = QApplication([])
window = QWidget ()
button = QPushButton("Clique aqui", window)
button.clicked.connect(botao_clique)
window.show()
app.exec()