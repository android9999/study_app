import tkinter as tk
from StudyApp import StudyApp
from QuestionSelector import QuestionSelector

def main():

    number_Of_questions = 30

    def if_all_correct_answers():
        selector.change_questions()

    root = tk.Tk()
    selector = QuestionSelector("all_questions.txt", "index.txt")  # Provide index file for persistent index storage

    selector.select_questions(number_Of_questions, "questions.txt")
    app = StudyApp(root, "questions.txt", if_all_correct_answers)  # Replace "questions.txt" with your questions file
        
    root.mainloop()

if __name__ == "__main__":
    main()
