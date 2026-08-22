import random

#def ask_question(question_type):
#    if question_type == "meaning":
#        word_choice = random.randrange(length)
#        print(f'Which selection best represents the meaning of the word {master_list[word_choice]["word"]}?\n')
#        correct_answer = random.randint(1, 4)
#        for i in range(4):
#            if i + 1 != correct_answer:
#                temp_randnum = random.randrange(length)
#                while temp_randnum == word_choice:
#                    temp_randnum = random.randrange(length)
#                print(f'\t{i + 1}. {master_list[temp_randnum]["meaning"]}')
#            else:
#                print(f'\t{i + 1}. {master_list[word_choice]["meaning"]}')
#        choice = int(input(""))
#        if choice == correct_answer:
#            print("Correct")
#        else:
#            print("Incorrect")

class Quiz:
    def __init__(self, master_list):
        self.master_list = master_list
        self.length = len(master_list)

    def get_question(self):
        word_choice = random.randrange(self.length)
        correct_answer = random.randint(1,4)
        answers = []
        for i in range(4):
            if i+1 == correct_answer:
                answers.append(self.master_list[word_choice]["meaning"])
            else:
                temp_randnum = random.randrange(self.length)
                while temp_randnum==word_choice:
                    temp_randnum=random.randrange(self.length)
                answers.append(self.master_list[temp_randnum]["meaning"])
        return{
            "word": self.master_list[word_choice]["word"],
            "answers": answers,
            "correct_answer": correct_answer
        }

