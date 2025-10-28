from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit

app = QApplication ([])
window = QWidget()
line = QLineEdit(window)
window.show()
app.exec()