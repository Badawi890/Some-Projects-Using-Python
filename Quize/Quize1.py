
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.current_question_index = 0

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            print(f"Question {self.current_question_index + 1}: {question.text}")
            for idx, choice in enumerate(question.choices, 1):
                print(f"{idx}. {choice}")
            answer = input("Your answer (type the choice): ")
            self.guess(answer)
            self.loadQuestions()
        else:
            print(f"Quiz finished! Your score is {self.score}/{len(self.questions) * 25}")

    def guess(self, answer):
        question = self.questions[self.current_question_index]
        if question.checkAnswer(answer):
            print("Correct!")
            self.score += 25
        else:
            print(f"Wrong! The correct answer was: {question.answer}")
        self.current_question_index += 1
        self.display_question()
    def loadQuestions(self):
        if len(self.questions) == self.current_question_index:
            self.Showscore()
        else:
            self.displayPogress()
            self.display_question()
    def Showscore(self):
        pass
    def displayPogress(self):
        total_questions = len(self.questions)
        current_question = self.current_question_index + 1
        print(f"Question {current_question} of {total_questions}".center(170,"*"))
        

# Define questions
Q1 = Question("Which is the best programming language?", ["Python", "Java", "C++", "JavaScript"], "Python")
Q2 = Question("What is 2 + 2?", ["3", "4", "5", "6"], "4")
Q3 = Question("What happens if you put water in the freezer?", ["it is ice", "it is hot"], "it is ice")

questions = [Q1, Q2, Q3]
quiz = Quiz(questions)
quiz.loadQuestions()






    


