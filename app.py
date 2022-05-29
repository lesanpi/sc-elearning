from flask import Flask, render_template, request
import json
import random
from models.question import Question

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

with open('./data.json', 'r') as file:
    data = json.load(file)

def getRandomContent(type="lesson", num=12):
    contentFiltered = []
    for course in data["courses"]:
        # print(course["title"])
        for content in course["content"]:
            # print(content["title"])
            if content["type"] == type:
                # print("added")
                contentFiltered.append(content)

    contentFiltered = list(contentFiltered)
    random.shuffle(contentFiltered)
    
    return contentFiltered[:num]

def getClassById(id):
    for course in data["courses"]:
        for content in course["content"]:
            if content["id"] == id:
                return (content, course)
    
    return None

def getQuizById(id):
    for course in data["quizes"]:
        for quiz in course["quizes"]:
            if quiz["id"] == id:
                return (quiz, course)

    return None

@app.route('/')
@app.route('/home')
def home():
    # Home
    return render_template('index.html')

@app.route('/aprende')
def aprende():
    # E-Learning
    lessonsRecommended = getRandomContent()
    guidesRecommended = getRandomContent(type="guide", num=4)
    return render_template('aprende.html', lessonsRecommended=lessonsRecommended, guidesRecommended=guidesRecommended)

@app.route('/curso/<course_num>')
def course(course_num=None):
    if (int(course_num) > 5 or int(course_num) < 1):
        return render_template('404.html'), 404
    
    lessonRecommended = getRandomContent(num=1)[0]

    course = data["courses"][int(course_num) - 1]
    return render_template('course.html', course_num=course_num, course=course, lessonRecommended=lessonRecommended)



@app.route('/clase/<class_id>')
def video_class(class_id=None):
    if (class_id is None):
        return render_template('404.html'), 404
    
    course_class = getClassById(class_id)
    if course_class is None:
        return render_template('404.html'), 404
    
    video_class, course = course_class
    return render_template('video_player.html', course=course, video_class=video_class)


@app.route('/play')
def play_page():
    # Home
    return render_template('play.html', all_quizes = data["quizes"])



@app.route("/play/<quiz_id>")
def quiz(quiz_id = None):
    if quiz_id == None:
        return render_template('404.html'), 404
    
    quiz_course = getQuizById(quiz_id)
    if quiz_course == None:
        return render_template('404.html'), 404

    quiz, course = quiz_course

    question_list = []
    for i, question in enumerate(quiz["questions"], 1):
        try:
            newQuestion = Question(i, question["question"], question["option_1"], question["option_2"], 
                question["option_3"], question["option_4"], question["correct_option"], question["img"]) 
            # print(question["img"]);
        except:
            newQuestion = Question(i, question["question"], question["option_1"], question["option_2"], 
                question["option_3"], question["option_4"], question["correct_option"], "") 
        question_list.append(newQuestion)

    return render_template("quiz.html", quiz = quiz, questions_list = question_list)

@app.route("/play/<quiz_id>/submit", methods=['POST', 'GET'])
def submit(quiz_id = None):

    if request.method == 'GET':
        return render_template('404.html'), 404
        
    if quiz_id == None:
        return render_template('404.html'), 404
    
    quiz_course = getQuizById(quiz_id)
    if quiz_course == None:
        return render_template('404.html'), 404

    quiz, course = quiz_course
    question_list = [
            Question(i, question["question"], question["option_1"], question["option_2"], 
                question["option_3"], question["option_4"], question["correct_option"]) 
            for i, question in enumerate(quiz["questions"], 1)
            ]
    correct_count = 0
    answers_selected = []
    for question in question_list:
        question_id = str(question.q_id)
        selected_option = request.form[question_id]
        answers_selected.append(selected_option)
        correct_option = question.get_correct_option()
        if selected_option == correct_option:
            correct_count = correct_count +1

    correct_count = str(correct_count)
    return render_template("quiz_result.html", quiz = quiz, questions_list = question_list, course = course, answers_selected = answers_selected, correct_count=correct_count)

    

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('404.html'), 500

if __name__ == '__main__':
    app.run(debug=True)

    