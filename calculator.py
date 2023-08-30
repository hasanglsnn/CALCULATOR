import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QStyleFactory, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Beautiful Calculator")
        self.setGeometry(100, 100, 300, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.result_display = QLineEdit()
        self.result_display.setAlignment(Qt.AlignRight)
        self.result_display.setReadOnly(True)
        self.layout.addWidget(self.result_display)

        buttons_layout = QVBoxLayout()
        self.layout.addLayout(buttons_layout)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', 'C']  # Replace 'C' with 'Backspace'
        ]

        for row in buttons:
            row_layout = QHBoxLayout()
            buttons_layout.addLayout(row_layout)
            for button_text in row:
                button = QPushButton(button_text)
                button.clicked.connect(self.button_clicked)
                row_layout.addWidget(button)
                if button_text.isdigit() or button_text in ['+', '-', '*', '/']:
                    button.setShortcut(button_text)

        self.current_text = ""

        self.delete_shortcut = QShortcut(QKeySequence(Qt.Key_Delete), self)
        self.delete_shortcut.activated.connect(self.clear_display)

        self.backspace_shortcut = QShortcut(QKeySequence(Qt.Key_Backspace), self)
        self.backspace_shortcut.activated.connect(self.remove_last_character)

    def clear_display(self):
        self.current_text = ""
        self.result_display.clear()

    def remove_last_character(self):
        self.current_text = self.current_text[:-1]
        self.result_display.setText(self.current_text)

    def button_clicked(self):
        clicked_button = self.sender()
        clicked_text = clicked_button.text()

        if clicked_text == "=":
            self.calculate_result()
        elif clicked_text == "C":  # Clear current input
            self.clear_display()
        elif clicked_text == "Backspace":  # Remove the last character
            self.remove_last_character()
        else:
            self.current_text += clicked_text
            self.result_display.setText(self.current_text)

    def calculate_result(self):
        try:
            result = str(eval(self.current_text))
            self.result_display.setText(result)
        except Exception as e:
            self.result_display.setText("Error")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))  # Apply Fusion style for dark mode
    calculator = Calculator()
    calculator.show()
    
    sys.exit(app.exec_())
