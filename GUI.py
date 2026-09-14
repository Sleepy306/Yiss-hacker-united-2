#UI files

WindowTitle = "Yiss Hackers United Network"

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

app = QApplication(sys.argv)
window = QWidget()
window.setGeometry(100, 100, 800, 400)

#Define name input window
namelayout = QVBoxLayout()

window.setWindowTitle(WindowTitle)

inputTextField = QLineEdit(window)
inputTextField.setPlaceholderText("Enter name...")
namelayout.addWidget(inputTextField)

submitButton = QPushButton("Submit", window)
namelayout.addWidget(submitButton)

window.setLayout(namelayout)
window.show()

sys.exit(app.exec())