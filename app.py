from flask import Flask, render_template, redirect, url_for, session, request
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL connection details
db_host = 'localhost'
db_user = 'root'
db_password = 'root'
db_name = 'book'

# Connect to MySQL
db = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Insert user data into MySQL
        cursor = db.cursor()
        sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        values = (name, email, password)
        cursor.execute(sql, values)
        db.commit()

        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form['email']
    password = request.form['password']

    # Check if user exists in MySQL
    cursor = db.cursor()
    sql = "SELECT * FROM users WHERE email = %s AND password = %s"
    values = (email, password)
    cursor.execute(sql, values)
    user = cursor.fetchone()

    if user:
        session['user_id'] = user[0]
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/genre')
def genre():
    return render_template('genre.html')

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

if __name__ == "__main__":
    app.run()