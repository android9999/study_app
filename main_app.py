import tkinter as tk
import StudyApp


def main():
    root = tk.Tk()
    app = StudyApp.StudyApp(root, "questions.txt")  # Replace "questions.txt" with your questions file
    root.mainloop()

if __name__ == "__main__":
    main()

