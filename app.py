from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/genre')
def genre():
    return render_template('genre.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/fiction')
def fiction():
    return render_template('fiction.html')

@app.route('/novel')
def novel():
    return render_template('novel.html')

@app.route('/biography')
def biography():
    return render_template('biography.html')

@app.route('/mystery')
def mystery():
    return render_template('mystery.html')

@app.route('/floklore')
def floklore():
    return render_template('floklore.html')

@app.route('/comedy')
def comedy():
    return render_template('comedy.html')

@app.route('/horror')
def horror():
    return render_template('horror.html')

@app.route('/poetry')
def poetry():
    return render_template('poetry.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
