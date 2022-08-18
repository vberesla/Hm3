import colorama
from colorama import Fore, Style
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def context():
    title_txt = 'Hello ' +  input(Fore.RED + "\nplease insert your title txt\n")
    body_txt = input(Fore.CYAN + "\nplease inset your test\n")
    return render_template('news.html', title=title_txt, body=body_txt)

@app.route("/register")
def register():
    return render_template('register.html')


@app.route("/gallery")
def gallery():
    return render_template('picture.html')

if __name__ == "__main__":
    app.run(debug=True)