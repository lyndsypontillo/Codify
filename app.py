from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Secret key for session management
app.config['SECRET_KEY'] = 'your_secret_key'

# SQLite Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# User model (representing the users table in the database)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Route for the home page
@app.route('/')
def home():
    return render_template('login.html')

# Route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Check if username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists", "danger")
            return redirect(url_for('register'))

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please log in.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists in the database
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash("Login successful!", "success")
            return redirect(url_for('welcome'))  # Redirect to welcome page after successful login

        flash("Login failed. Check your username and/or password.", "danger")

    return render_template('login.html')


# Route for the welcome page
@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Get the selected language from the form
        language = request.form['language']
        # Redirect to the learning page with the selected language
        return redirect(url_for('learning', language=language))

    return render_template('welcome.html', username=session['username'])

# Route for learning page based on language selection
@app.route('/learning/<language>')
def learning(language):
    if language == 'python':
        return render_template('learning_python.html')
    elif language == 'javascript':
        return render_template('learning_javascript.html')
    elif language == 'java':
        return render_template('learning_java.html')
    elif language == 'ruby':
        return render_template('learning_ruby.html')
    else:
        flash("Language not available.", "danger")
        return redirect(url_for('welcome'))

# Route to logout the user
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))

# Initialize the database inside the app context
if __name__ == '__main__':
    with app.app_context():  # Ensure the app context is available
        db.create_all()  # Create tables if they do not exist
    app.run(debug=True)
