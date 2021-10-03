from flask import Flask, render_template, request

app = Flask(__name__)


class Question:
    q_id = -1
    question = ""
    option1 = ""
    option2 = ""
    option3 = ""
    correctOption = -1

    def __init__(self, q_id, question, option1, option2, option3,correctOption):
        self.q_id = q_id
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.correctOption = correctOption

    def get_correct_option(self):
        if self.correctOption == 1:
            return self.option1
        elif self.correctOption == 2:
            return self.option2
        elif self.correctOption == 3:
            return self.option3

q1 = Question(1, "What is your Uni name", "UET", "UOS", "UOM", 1)
q2 = Question(2, "Where UET is located", "Miwali", "Multan", "Lahore", 3)
q3 = Question(3, "What is your degree name?","CE","CS","SE",2)

questions_list = [q1, q2, q3]

@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions_list = questions_list)

@app.route("/submitquiz", methods=['POST', 'GET'])
def submit():
    correct_count=0
    for question in questions_list:
        question_id = str(question.q_id)
        selected_option = request.form[question_id]
        correct_option = question.get_correct_option()
        if selected_option == correct_option:
            correct_count = correct_count +1

    correct_count = str(correct_count)
    return correct_count
    

if __name__ == "__main__":
    app.run(debug=True)
