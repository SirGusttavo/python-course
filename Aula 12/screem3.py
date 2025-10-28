from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPalette, QColor

app = QApplication ([])
window = QWidget()
window.setWindowTitle("Color Screem")
palette = window.palette()
palette.setColor(QPalette.ColorRole.Window, QColor("black"))
window.setPalette(palette)
window.show()
app.exec()