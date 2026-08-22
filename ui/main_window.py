from PyQt6.QtCore import QSize, Qt, QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, QVBoxLayout
from core.questions import Quiz
import sys, time

class MainWindow(QMainWindow):
    def __init__(self, quiz):
        super().__init__()

        self.quiz = quiz
        self.correctCount = 0
        self.incorrectCount = 0

        self.setWindowTitle("asdf")
        self.resize(800, 800)

        central = QWidget()
        self.setCentralWidget(central)
        mainLayout = QVBoxLayout(central)
        div = QWidget()
        div.setMaximumWidth(600)
        divLayout = QVBoxLayout(div)

        self.questionLabel = QLabel()
        self.choice1 = QPushButton()
        self.choice2 = QPushButton()
        self.choice3 = QPushButton()
        self.choice4 = QPushButton()
        self.answerLabel = QLabel()

        divLayout.addWidget(self.questionLabel)
        divLayout.addWidget(self.choice1)
        divLayout.addWidget(self.choice2)
        divLayout.addWidget(self.choice3)
        divLayout.addWidget(self.choice4)
        divLayout.addWidget(self.answerLabel)

        mainLayout.addStretch()
        mainLayout.addWidget(div, alignment=Qt.AlignmentFlag.AlignHCenter)
        mainLayout.addStretch()

        self.new_question()

        self.choice1.clicked.connect(lambda: self.check_answer(1))
        self.choice2.clicked.connect(lambda: self.check_answer(2))
        self.choice3.clicked.connect(lambda: self.check_answer(3))
        self.choice4.clicked.connect(lambda: self.check_answer(4))
    def new_question(self):
        self.choice1.setEnabled(True)
        self.choice2.setEnabled(True)
        self.choice3.setEnabled(True)
        self.choice4.setEnabled(True)
        self.answerLabel.setText("")
        question = self.quiz.get_question()
        self.questionLabel.setText(f'What does {question["word"]} mean?')
        self.choice1.setText(question["answers"][0])
        self.choice2.setText(question["answers"][1])
        self.choice3.setText(question["answers"][2])
        self.choice4.setText(question["answers"][3])
        self.correct_answer = question["correct_answer"]
    def check_answer(self, choice):
        if choice == self.correct_answer:
            self.correctCount += 1
            self.answerLabel.setText(f'Correct! Correct: {self.correctCount} Incorrect: {self.incorrectCount}')
        else:
            self.incorrectCount += 1
            print("no")
            self.answerLabel.setText(f'Incorrect! Correct: {self.correctCount} Incorrect: {self.incorrectCount}')

        self.choice1.setEnabled(False)
        self.choice2.setEnabled(False)
        self.choice3.setEnabled(False)
        self.choice4.setEnabled(False)
        
        QTimer.singleShot(2250, self.new_question)