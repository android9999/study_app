



class ImageConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Image Viewer")
        self.text_widget = tk.Text(root, wrap=tk.WORD, height=15, width=35)
        self.open_button = tk.Button(root, text="Open Image", command=self.open_image)
        self.open_button.pack(padx=20, pady=10)
        self.image_label = tk.Label(root)
        self.image_label.pack(padx=20, pady=20)
        self.status_label = tk.Label(root, text="", padx=20, pady=10)
        self.status_label.pack()

    def open_image(self):
        file_path = self.latex_to_png(r"\theta")
        if file_path:
            self.display_image(file_path)

    def latex_to_png(self, latex_str):
        fig = plt.figure()
        plt.axis("off")
        plt.text(0.5, 0.5, f"${latex_str}$", size=50, ha="center", va="center")

        pdf_path = "result.pdf"
        png_path = "result.png"

        plt.savefig(pdf_path, format="pdf", bbox_inches="tight", pad_inches=0.4)
        plt.close(fig)

        images = convert_from_path(pdf_path)
        images[0].save(png_path, "PNG")

        return png_path

    def display_image(self, file_path):
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.photo = photo
        self.status_label.config(text=f"Image loaded: {file_path}")



























class StudyApp:
    def __init__(self, root, questions_file):
        self.root = root
        self.root.title("Study App")

        self.questions = self.load_questions(questions_file)
        self.current_question_index = -1
        self.correct_answers = 0
        self.incorrect_answers = 0

        #self.question_label = tk.Label(root, text="")
        #self.question_label.pack()

        self.show_answer_button = tk.Button(root, text="Show Answer", command=self.show_answer)
        self.show_answer_button.pack()

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

    def show_answer(self):
        if self.current_question_index != -1:
            _, answer = self.questions[self.current_question_index]
            self.open_image(answer)

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
            #self.question_label.config(text=question)
            self.open_image(question)










            
        else:
            self.study_complete()

    def study_complete(self):
        messagebox.showinfo("Study Complete", f"Congratulations! You have completed all the questions.\nCorrect Answers: {self.correct_answers}\nIncorrect Answers: {self.incorrect_answers}")

    def open_image(self, latex_str):
        file_path = self.latex_to_png( repr(latex_str)[1:-1]   )
        if file_path:
            self.display_image(file_path)

    def latex_to_png(self, latex_str):
        fig = plt.figure()
        plt.axis("off")
        plt.text(0.5, 0.5, latex_str, size=20, ha="center", va="center")

        pdf_path = "result.pdf"
        png_path = "result.png"

        plt.savefig(pdf_path, format="pdf", bbox_inches="tight", pad_inches=0.4)
        plt.close(fig)

        images = convert_from_path(pdf_path)
        images[0].save(png_path, "PNG")

        return png_path

    def display_image(self, file_path):
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.photo = photo
 



if __name__ == "__main__":
    root = tk.Tk()
    app = StudyApp(root, "questions.txt")  # Replace "questions.txt" with your questions file
    root.mainloop()
