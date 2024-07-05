from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'your_secret_key'

client = MongoClient("mongodb+srv://admin123:admin123@obs.jv4itlw.mongodb.net/?retryWrites=true&w=majority&appName=OBS")
db = client['book']
sample = db.VALUES
books_collection = db.addbooks

@app.route('/', methods=['GET', 'POST'])
def index():
    if "email" in session:
        return redirect(url_for("home"))
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if email == 'admin@gmail.com' and password == 'admin123':
            # Redirect to admin home page or perform actions here
            return render_template('admin_home.html')
        user = sample.find_one({"email": email})
        if user and user["password"] == password:
            session["email"] = email
            return redirect(url_for("home"))

        else:
            flash("Invalid login credentials")
            return render_template('login.html')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        user_found = sample.find_one({'username': username})
        email_found = sample.find_one({'email': email})

        if user_found:
            flash('There is already a user by that name')
            return render_template('register.html')

        if email_found:
            flash('The email already exists in the database')
            return render_template('register.html')

        user_input = {'username': username, 'email': email, 'password': password}
        sample.insert_one(user_input)
        return redirect(url_for('index'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))

@app.route('/admin_home')
def admin():
    return render_template('admin_home.html')

@app.route('/genre')
def genre():
    return render_template('genre.html')

@app.route('/favourites')
def wishlist():
    return render_template('favourites.html')

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

@app.route('/folklore')
def folklore():
    return render_template('folklore.html')

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

@app.route('/addbook', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_book = {
            'name': request.form['name'],
            'author': request.form['author'],
            'genre': request.form['genre'],
            'image_url': request.form['image_url']
        }
        books_collection.insert_one(new_book)
        return redirect(url_for('viewbook'))
    return render_template('addbook.html')

@app.route('/viewbook', methods=['GET'])
def viewbook():
    books = list(books_collection.find())
    return render_template('viewbook.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
