from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton

app = QApplication ([])
window = QWidget()
layout = QHBoxLayout()
layout.addWidget(QPushButton("Botão 1"))
layout.addWidget(QPushButton("Botão 2"))
window.setLayout(layout)
window.show()
app.exec()