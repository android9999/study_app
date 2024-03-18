class QuestionSelector:
    def __init__(self, all_questions_file, index_file):
        self.all_questions_file = all_questions_file
        self.index_file = index_file
        self.current_index = self.load_index()

    def load_index(self):
        try:
            with open(self.index_file, 'r') as f:
                return int(f.read())
        except FileNotFoundError:
            return 0

    def save_index(self):
        with open(self.index_file, 'w') as f:
            f.write(str(self.current_index))

    def select_questions(self, n, questions_file):
        with open(self.all_questions_file, 'r') as all_questions:
            all_lines = all_questions.readlines()

        selected_questions = []
        for i in range(n):
            selected_questions.append(all_lines[self.current_index % len(all_lines)].strip())
            self.current_index += 1

        with open(questions_file, 'w') as selected_file:
            selected_file.write('\n'.join(selected_questions))

    def change_questions(self):
        self.save_index()

# Example usage:
#selector = QuestionSelector("all_questions.txt", "index.txt")
#selector.select_questions(5, "questions.txt")
#selector.change_questions(5)

