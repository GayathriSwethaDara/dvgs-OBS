from flask import *
from pymongo import MongoClient

app = Flask(__name__)

client=MongoClient("mongodb+srv://swetha:swetha@cluster0.wagornv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db=client.get_database('total_records')
records = db.register
@app.route('/',methods=['post','get'])
def index():
    msg=""
    if "email" in session:
        return redirect(url_for("login"))
    if request.method=="POST":
        username=request.form.get("username")
        email=request.form.get("email")
        password=request.form.get("password")
        user_found=records.find_one({"username":username})
        email_found=records.find_one({"email":email})
        if user_found:
            msg="There is already user by that name"
            return render_template('register.html',msg=msg)
        if email_found:
            msg="There email already exists in database"
            return render_template('register.html',msg=msg)
        else:
            user_input={'username':username, 'email':email, 'password':password}
            records.insert_one(user_input)

            user_data=records.find_one({"email":email})
            new_email=user_data["email"]
            return render_template('login.html')
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
