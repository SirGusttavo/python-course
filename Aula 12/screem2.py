from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication ([])
Window = QWidget()
Window.setWindowTitle("Primeira Tela")

#Largura e Altura:
#width e height
Window.resize(400, 300)
Window.show()
app.exec()