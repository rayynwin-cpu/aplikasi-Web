from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout, 
    QLabel, QPushButton, QRadioButton
)
from PyQt6.QtCore import Qt

app = QApplication([])

try: 
    with open("style3.css", "r") as f:
        app.setStyleSheet(f.read())
except FileNotFoundError:
    print("Warning: whatever your typing is not being registered by us.")

window = QWidget()
window.setObjectName("mainWindow")
main_layout = QVBoxLayout(window)
main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

container = QWidget()
container.setObjectName("container")
container_layout = QVBoxLayout(container)
container_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

h2 = QLabel("Quiz Title")
h2.setObjectName("title")
h2.setAlignment(Qt.AlignmentFlag.AlignCenter)

h3 = QLabel("Select an answer below:")
h3.setObjectName("subtitle")
h3.setAlignment(Qt.AlignmentFlag.AlignCenter)

radio_grid = QGridLayout()
radio_grid.setHorizontalSpacing(20)
radio_grid.setVerticalSpacing(20)

opt1 = QRadioButton("Option A")
opt2 = QRadioButton("Option B")
opt3 = QRadioButton("Option C")
opt4 = QRadioButton("Option D")

radio_grid.addWidget(opt1, 0, 0)
radio_grid.addWidget(opt2, 0, 1)
radio_grid.addWidget(opt3, 1, 0)
radio_grid.addWidget(opt4, 1, 1)

btn = QPushButton("Submit")
btn.setProperty("class", "btn")

result = QLabel("Result text goes here")
result.setObjectName("restext")
result.setAlignment(Qt.AlignmentFlag.AlignCenter)

def check_answer():
    selected_button = button_group.checkedButton()

    if selected_button is None:
        result.setText("Please select an answer first!")
        return

    correct_id = 1

    if button_group.checkedId() == correct_id:
        result.setText("Correct! Great job.")
    else:
        result.setText(f"Incorrect. You picked {selected_button.text()}.")

btn.clicked.connect(check_answer)

container_layout.addWidget(h2)
container_layout.addWidget(h3)
container_layout.addLayout(radio_grid)
container_layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)
container_layout.addWidget(result)
main_layout.addWidget(container)
window.resize(500, 400)
window.show()

app.exec()
