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

@app.route('/')
@app.route('/home')
def home():
    # Home
    return render_template('index.html')

@app.route('/juego')
def quiz():
    # Home
    return render_template('game.html')

@app.route('/año/<course>/')
def course(course=None):
    classes_list = videos[course]['classes']
    course_title = videos[course]['title']
    return render_template('course.html', course=course, classes_list=classes_list, course_title=course_title)


@app.route('/año/<course>/<class_num>')
def video_class(course=None, class_num=None):
    print(course, class_num)
    class_title = videos[course]['classes'][int(class_num)]['title']
    classes_list = videos[course]['classes']
    course_class_link = videos[course]['classes'][int(class_num)]['video_link']
    return render_template('video_player.html', course=course, classes_list=classes_list,
        class_title=class_title, 
        class_num=class_num, class_link=course_class_link)



if __name__ == '__main__':
    app.run(debug=True)