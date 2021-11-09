from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    title = "Homepage"
    programing_languages = [
        "Python",
        "JavaScript",
        "PHP",
    ]
    return render_template('index.html', title=title, programing_languages=programing_languages)




