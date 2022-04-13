from flask import Flask, redirect, render_template, request, url_for
import os

app = Flask(__name__)

picFolder = os.path.join('static','pics')

app.config['UPLOAD_FOLDER'] = picFolder



class Question:
    q_id = -1
    question = ""
    option1 = ""
    option2 = ""
    option3 = ""
    option4 = ""
    correctOption = -1

    def __init__(self,q_id,question,option1,option2,option3,option4,correctOption):
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

qa1 = Question(1, "¿Cuál es el nombre de tu universidad?","UCAB","UET","UCV","MIT",1)
qa2 = Question(2, "¿Donde esta la universidad ubicada?","Bolivia","Mexico","Caracas","Boston",3)
qa3 = Question(3, "¿Cuál es el nombre de tu carrera?","Comunicación","Ingeniería","Psicología","Medicina",2)
qa4 = Question(4, "¿Quien fue el profesor de Simon Bolivar?","Andrés Bello","George Washington","Lincoln","Ana Maria",1)
questions_list1 = [qa1,qa2,qa3,qa4]
qb1 = Question(1,"¿Quien fue el primer presidente de Estados Unidos?","Lincoln","Washington","Jefferson","Roosevelt",2)
qb2 = Question(2,"¿Cuantos estados tiene Estados Unidos?","48","52","46","50",4)
qb3 = Question(3,"¿Cual de las siguientes comidas NO es un producto lacteo?","Leche","Hamburguesa","Yogur","Queso",2)
qb4 = Question(4,"¿Cuál es un pais Sudamericano?","Rusia","Argentina","Mexico","Japón",2)
questions_list2 = [qb1,qb2,qb3,qb4]

questions_list = questions_list1

@app.route("/main", methods=["POST","GET"])
def main():
        pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'castellano.svg')
        pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'matematica.svg')
        pic3 = os.path.join(app.config['UPLOAD_FOLDER'],'fisica.svg')
        pic4 = os.path.join(app.config['UPLOAD_FOLDER'],'quimica.svg')
        pic5 = os.path.join(app.config['UPLOAD_FOLDER'],'biologia.svg')
        pic6 = os.path.join(app.config['UPLOAD_FOLDER'],'historia.svg')
        pic7 = os.path.join(app.config['UPLOAD_FOLDER'],'banner2.jpg')
        if request.method == "POST":
            if request.form['submit_button'] == 'castellano':
                return redirect(url_for('quiz', questions_list = questions_list1)) #Chequear pagina de las pestañas para solucionar error de paso de lista (redirect list)
            
            elif request.form['submit_button'] == 'matematica':
                return redirect(url_for('quiz', questions_list = questions_list2))
            
            else:
                return redirect(url_for(main)),404

        else:
            return render_template("index.html", 
                                user_image1 = pic1, 
                                user_image2 = pic2,
                                user_image3 = pic3,
                                user_image4 = pic4,
                                user_image5 = pic5,
                                user_image6 = pic6,
                                user_image7 = pic7)
        

@app.route("/quiz", methods = ['POST','GET'])
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

        correct_count = str(correctCount)

        msg = "Respuestas Correctas: "+correct_count
        if correctCount == 0:
            msg = "No obtuviste ninguna respuesta correcta"
    return render_template("submit.html", msg = msg)

if __name__ == "__main__":
    app.run(debug=True)