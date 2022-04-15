from flask import Flask, render_template, url_for
import json
import random
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
with open('./data.json', 'r') as file:
    data = json.load(file)

videos = {
    "5": {
        "title": "5to Año",
        "classes": [
            {
                "title": "Ecuacion de segundo grado",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png",
                "video_link": "https://www.youtube.com/watch?v=6c79IBiss1o",
                "paper": "Guia de Ecuaciones y Polinomios.",
                "paper_link": "www.google.com"
            },
            {
                "title": "Ecuacion de segundo grado",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png",
                "video_link": "https://www.youtube.com/watch?v=6c79IBiss1o"
            },
            {
                "title": "Escalares, Vectores y Matrices",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png",
                "video_link": "https://www.youtube.com/watch?v=6c79IBiss1o"
            },
            {
                "title": "Ecuacion de segundo grado",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png",
                "video_link": "https://www.youtube.com/watch?v=6c79IBiss1o",
                "paper": "Guia de Ecuaciones y Polinomios.",
                "paper_link": "www.google.com"
            },
            {
                "title": "Derivas e Integrales",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png",
            },
            {
                "title": "Area sobre una curva",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png",
            },
            {
                "title": "Producto escalar y producto vecotorial",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png",
            },
        ]
    },
    "4": {
        "title": "5to Año",
        "classes": [
            {
                "title": "Ecuacion de segundo grado",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png"
            },
            {
                "title": "Escalares, Vectores y Matrices",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png"
            },
            {
                "title": "Derivas e Integrales",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png"
            },
            {
                "title": "Area sobre una curva",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png"
            },
            {
                "title": "Producto escalar y producto vecotorial",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png"
            },
        ]
    },
    "3": {
        "title": "5to Año",
        "classes": [
            {
                "title": "Ecuacion de segundo grado",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png"
            },
            {
                "title": "Escalares, Vectores y Matrices",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png"
            },
            {
                "title": "Derivas e Integrales",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png"
            },
            {
                "title": "Area sobre una curva",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png"
            },
            {
                "title": "Producto escalar y producto vecotorial",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png"
            },
        ]
    },
    "2": {
        "title": "5to Año",
        "classes": [
            {
                "title": "Ecuacion de segundo grado",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png"
            },
            {
                "title": "Escalares, Vectores y Matrices",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png"
            },
            {
                "title": "Derivas e Integrales",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png"
            },
            {
                "title": "Area sobre una curva",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png"
            },
            {
                "title": "Producto escalar y producto vecotorial",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png"
            },
        ]
    },
    "1": {
        "title": "5to Año",
        "classes": [
            {
                "title": "Ecuacion de segundo grado",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png"
            },
            {
                "title": "Escalares, Vectores y Matrices",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png"
            },
            {
                "title": "Derivas e Integrales",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png"
            },
            {
                "title": "Area sobre una curva",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png"
            },
            {
                "title": "Producto escalar y producto vecotorial",
                "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis autem consequatur veritatis ratione?",
                "img_link": "https://static.platzi.com/media/blog/que-son-y-como-se-conjugan-las-preposiciones-en-ingles_2-fb910d15-8415-42ea-8049-7164191d179a.png"
            },
        ]
    }
}


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
    print(type(data))
    lessonsRecommended = getRandomContent()
    guidesRecommended = getRandomContent(type="guide", num=4)
    return render_template('aprende.html', lessonsRecommended=lessonsRecommended, guidesRecommended=guidesRecommended)

@app.route('/aprende/curso/<course>')
def course(course=None):
    if (int(course) > 5 or int(course) < 1):
        return render_template('404.html'), 404
    
    course = data["courses"][int(course) - 1]
    return render_template('course.html', course=course)


@app.route('/clase/<class_id>')
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

    