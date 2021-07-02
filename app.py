from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

videos = {
    "5": {
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
    "4": [],
    "3": [],
    "2": [],
    "1": []
}

@app.route('/')
@app.route('/home')
def home():
    # Home
    return render_template('index.html')

@app.route('/course/<course>')
def course(course=None):
    classes_list = videos[course]['classes']
    course_title = videos[course]['title']
    return render_template('course.html', course=course, classes_list=classes_list, course_title=course_title)

if __name__ == '__main__':
    app.run(debug=True)