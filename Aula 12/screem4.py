from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPalette, QColor

app = QApplication ([])
window = QWidget()
label = QLabel("Hello World", window)
window.show()
app.exec()