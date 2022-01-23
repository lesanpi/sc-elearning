from flask import Flask, render_template, request

app = Flask(__name__)

class Question:
    q_id = -1
    question = ""
    option1 = ""
    option2 = ""
    option3 = ""
    correctOption = -1

    def __init__(self,q_id,question,option1,option2,option3,correctOption):
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

q1 = Question(1, "¿Cuál es el nombre de tu universidad?","UCAB","UET","UCV",1)
q2 = Question(2, "¿Donde esta la universidad ubicada?","Bolivia","Mexico","Caracas",3)
q3 = Question(3, "¿Cuál es el nombre de tu carrera?","Comunicación","Ingeniería","Psicología",2)
questions_list = [q1,q2,q3]



@app.route("/quiz")
def quiz():
        return render_template("quiz.html", questions_list = questions_list)

@app.route("/submitquiz", methods=['POST','GET'])
def submit():
    correctCount = 0
    for question in questions_list:
        qid = str(question.q_id)
        selected_option = request.form[qid]
        correct_option = question.get_correct_option()
        if selected_option == correct_option:
            correctCount = correctCount + 1

        correctCount = str(correctCount)

        msg = "Correct Options is"+correctCount
    return msg

if __name__ == "__main__":
    app.run(debug=True)