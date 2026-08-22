import json
import sys
import os
from core.questions import Quiz
from ui.main_window import MainWindow
from PyQt6.QtWidgets import QApplication

def fetch_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

json_path = fetch_path(os.path.join("json", "vocab.json"))

with open(json_path, "r", encoding="utf-8") as file:
    master_list = json.load(file)

quiz = Quiz(master_list)
app = QApplication(sys.argv)
window = MainWindow(quiz)
window.show()
sys.exit(app.exec())