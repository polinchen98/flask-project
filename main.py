from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/thanks/')
def thanks():
    return render_template('thanks.html')


if __name__ == "__main__":
    app.run(debug=True)
