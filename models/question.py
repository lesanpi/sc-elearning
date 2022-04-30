class Question:
    q_id = -1
    question = ""
    option1 = ""
    option2 = ""
    option3 = ""
    correctOption = -1

    def __init__(self, q_id, question, option1, option2, option3, option4, correctOption):
        self.q_id = q_id
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.correctOption = correctOption

    def get_correct_option(self):
        if self.correctOption == 1:
            return self.option1
        elif self.correctOption == 2:
            return self.option2
        elif self.correctOption == 3:
            return self.option3
        elif self.correctOption == 4:
            return self.option4

