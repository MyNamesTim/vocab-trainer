from core.questions import ask_question
import sys

continuation = ""
while continuation.lower() != 'n':
    ask_question("meaning")
    continuation = input('Would you like to continue (Y/N)?')
sys.exit()