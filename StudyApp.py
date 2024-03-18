import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from convert_latex_to_png import convert_latex_to_png

class StudyApp:
    def __init__(self, root, questions_file, if_all_correct_answers):
        self.root = root
        self.root.title("Study App")

        self.questions = self.load_questions(questions_file)
        self.current_question_index = -1
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.if_all_correct_answers = if_all_correct_answers
        self.show_answer_button = tk.Button(root, text="Show Answer", command=self.show_answer)
        self.show_answer_button.pack()
        self.show_answer_button["state"] = "disabled"

        self.correct_button = tk.Button(root, text="Correct", command=self.correct_answer)
        self.correct_button.pack()

        self.incorrect_button = tk.Button(root, text="Incorrect", command=self.incorrect_answer)
        self.incorrect_button.pack()

        self.image_label = tk.Label(root)
        self.image_label.pack(padx=20, pady=20)

        self.load_next_question()

    def load_questions(self, questions_file):
        questions = []
        with open(questions_file, 'r') as file:
            for line in file:
                question, answer = line.strip().split(';')
                questions.append((question, answer))
        return questions

    def switch(self):
        if self.show_answer_button["state"] == "normal":
            self.show_answer_button["state"] = "disabled"
            self.incorrect_button["state"] = "normal"
            self.correct_button["state"] = "normal"      
        else:
            self.show_answer_button["state"] = "normal"
            self.incorrect_button["state"] = "disabled"
            self.correct_button["state"] = "disabled"

    def show_answer(self):
        if self.current_question_index != -1:
            _, answer = self.questions[self.current_question_index]
            self.open_image(answer)
            self.switch()

    def correct_answer(self):
        if self.current_question_index != -1:
            self.correct_answers += 1
            self.load_next_question()

    def incorrect_answer(self):
        if self.current_question_index != -1:
            self.incorrect_answers += 1
            self.load_next_question()

    def load_next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            question, _ = self.questions[self.current_question_index]
            self.open_image(question)
            self.switch()
        else:
            self.study_complete()

    def study_complete(self):
        messagebox.showinfo("Study Complete", f"Congratulations! You have completed all the questions.\nCorrect Answers: {self.correct_answers}\nIncorrect Answers: {self.incorrect_answers}")
        if self.incorrect_answers == 0:
            self.if_all_correct_answers()
        exit(0)

    def open_image(self, latex_str):
        file_path =  convert_latex_to_png(latex_str)
        if file_path:
            self.display_image(file_path)

    def display_image(self, file_path):
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.photo = photo

# Example usage
#root = tk.Tk()
#app = StudyApp(root, "questions.txt")
#root.mainloop()
