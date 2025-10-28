import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QVBoxLayout, QDateEdit

class FormularioInscricao(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inscrição na Newsletter")

        # Criando os widgets
        self.label_titulo = QLabel("Inscreva-se em nossa Newsletter")
        self.label_nome = QLabel("Nome:")
        self.label_email = QLabel("E-mail:")
        self.label_cpf = QLabel("CPF:")
        self.label_data_nascimento = QLabel("Data de Nascimento:")

        self.lineEdit_nome = QLineEdit()
        self.lineEdit_email = QLineEdit()
        self.lineEdit_cpf = QLineEdit()
        self.dateEdit_data_nascimento = QDateEdit()

        self.button_inscrever = QPushButton("Inscrever-se")

        # Criando o layout
        layout = QGridLayout()
        layout.addWidget(self.label_titulo, 0, 0, 1, 3)

        layout.addWidget(self.label_nome, 1, 0)
        layout.addWidget(self.lineEdit_nome, 1, 1, 1, 2)

        layout.addWidget(self.label_email, 2, 0)
        layout.addWidget(self.lineEdit_email, 2, 1, 1, 2)

        layout.addWidget(self.label_cpf, 3, 0)
        layout.addWidget(self.lineEdit_cpf, 3, 1, 1, 2)

        layout.addWidget(self.label_data_nascimento, 4, 0)
        layout.addWidget(self.dateEdit_data_nascimento, 4, 1, 1, 2)

        layout.addWidget(self.button_inscrever, 5, 1, 1, 1)

        self.setLayout(layout)

# Criando a aplicação
app = QApplication(sys.argv)

# Criando e exibindo a janela
formulario = FormularioInscricao()
formulario.show()

# Executando a aplicação
sys.exit(app.exec())