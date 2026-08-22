import json
import sys

from core.questions import Quiz, ask_question
from ui.main_window import MainWindow
from PyQt6.QtWidgets import QApplication

with open("json/vocab.json", "r") as file:
    master_list = json.load(file)

quiz = Quiz(master_list)
app = QApplication(sys.argv)
window = MainWindow(quiz)
window.show()
sys.exit(app.exec())