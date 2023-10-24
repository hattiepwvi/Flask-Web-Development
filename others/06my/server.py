from flask import Flask
import random

app = Flask(__name__)
num2 = random.choice(range(10))

@app.route("/")
def hello_world():
    return ("<h1 style='text-align: center'>Guess a number between 0 and 9</h1>"
            "<div style='width:100%;height:0;padding-bottom:100%;position:relative;'><iframe src='https://giphy.com/embed/3o7aCSPqXE5C6T8tBC' width='100%' height='100%' style='position:absolute' frameBorder='0' class='giphy-embed' allowFullScreen></iframe></div>")

@app.route("/<num1>")
def greet(num1):
    if int(num1) == num2:
        return ("<h1 style='text-align: center; color: green'>You found me!</h1>"
                "<div style='width:100%;height:0;padding-bottom:105%;position:relative;'><iframe src='https://giphy.com/embed/4T7e4DmcrP9du' width='100%' height='100%' style='position:absolute' frameBorder='0 class='giphy-embed' allowFullScreen></iframe></div>")
    elif int(num1) > num2:
        return ('<h1 style="text-align: center; color: pink">Too high,try again!</h1>'
                '<div style="width:100%;height:0;padding-bottom:94%;position:relative;"><iframe src="https://giphy.com/embed/3o6ZtaO9BZHcOjmErm" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div>')
    elif int(num1) < num2:
        return ('<h1 style="text-align: center; color: red">Too low,try again!</h1>'
                '<div style="width:100%;height:0;padding-bottom:125%;position:relative;"><iframe src="https://giphy.com/embed/jD4DwBtqPXRXa" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div>')


app.run(debug=True)

