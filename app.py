from flask import Flask, render_template, url_for
import json
import random
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

    # print(contentFiltered)
    contentFiltered = list(contentFiltered)
    # print(contentFiltered[0])
    random.shuffle(contentFiltered)
    # print(contentFiltered[0])
    # print(list(contentFiltered))
    
    return contentFiltered[:num]

def getClassById(id):
    for course in data["courses"]:
        for content in course["content"]:
            if content["id"] == id:
                return (content, course)
    
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

@app.route('/aprende/curso/<course>')
def course(course=None):
    if (int(course) > 5 or int(course) < 1):
        return render_template('404.html'), 404
    
    lessonRecommended = getRandomContent(num=1)[0]

    course = data["courses"][int(course) - 1]
    return render_template('course.html', course=course, lessonRecommended=lessonRecommended)



@app.route('/aprende/clase/<class_id>')
def video_class(class_id=None):
    if (class_id is None):
        return render_template('404.html'), 404
    
    course_class = getClassById(class_id)
    if course_class is None:
        return render_template('404.html'), 404
    
    video_class, course = course_class
    return render_template('video_player.html', course=course, video_class=video_class)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('404.html'), 500



if __name__ == '__main__':
    app.run(debug=True)

    