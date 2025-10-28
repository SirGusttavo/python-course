from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication ([])
window = QWidget()
button = QPushButton("Click here", window)
window.show()
app.exec()