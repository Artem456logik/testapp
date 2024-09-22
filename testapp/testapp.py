from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton)
from PyQt6.QtCore import Qt
app = QApplication([])
win = QWidget()

win.setWindowTitle('Okosho_ockoshnika')
win.resize(500,400)

question = QLabel("Як звуть третього Президента України")
answer1 = QRadioButton("Кравчук")
answer2 = QRadioButton("Кучма")
answer3 = QRadioButton("Ющенко")
answer4 = QRadioButton("Грушевський")

main_layout = QVBoxLayout()
main_layout.addWidget(question, alignment=Qt.AlignmentFlag.AlignCenter)

h_line_1 = QHBoxLayout()
h_line_1.addWidget(answer1, alignment=Qt.AlignmentFlag.AlignCenter)
h_line_1.addWidget(answer2, alignment=Qt.AlignmentFlag.AlignCenter)

main_layout.addLayout(h_line_1)

h_line_2 = QHBoxLayout()
h_line_2.addWidget(answer3, alignment=Qt.AlignmentFlag.AlignCenter)
h_line_2.addWidget(answer4, alignment=Qt.AlignmentFlag.AlignCenter)

main_layout.addLayout(h_line_2)

def show_winner():
    message_box = QMessageBox()
    message_box.setText("WIN")
    message_box.show()
def show_loser():
    message_box = QMessageBox()
    message_box.setText("DEF")
    message_box.show()

answer1.clicked.connect(show_loser)
answer2.clicked.connect(show_winner)
answer3.clicked.connect(show_loser)
answer4.clicked.connect(show_loser)

win.setLayout(main_layout)
win.show()
app.exec()

