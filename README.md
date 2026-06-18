# Codify

Codify is a simple Flask web application for learning to code. Users can register an account, log in securely, and choose a programming language to view a dedicated learning page for it.

## Features

- User registration with hashed passwords (via Flask-Bcrypt)
- Login and session management
- SQLite database for storing user accounts (via Flask-SQLAlchemy)
- Language selection page after login (Python, JavaScript, Java, Ruby)
- Flash messages for registration, login, and logout feedback

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite (via Flask-SQLAlchemy)
- **Security:** Flask-Bcrypt for password hashing
- **Frontend:** HTML templates (Jinja2)

## Getting Started

### Prerequisites

- Python 3.x installed
- pip (Python's package installer)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/lyndsypontillo/Codify.git
   cd Codify
   ```

2. (Recommended) Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install Flask Flask-Bcrypt Flask-SQLAlchemy
   ```

### Running the App

```
python app.py
```

The app will start in debug mode and create the SQLite database (`users.db`) automatically on first run. Open your browser and go to:

```
http://127.0.0.1:5000
```

## Project Structure

```
Codify/
├── app.py              # Main application file (routes, models, app setup)
├── templates/           # HTML templates (login, register, welcome, learning pages)
└── users.db             # SQLite database (created automatically on first run)
```

## How It Works

1. New users register an account on the **Register** page. Passwords are hashed before being stored.
2. Returning users log in on the **Login** page; credentials are checked against the hashed password in the database.
3. After logging in, users land on the **Welcome** page and select a language to learn.
4. Users are redirected to a language-specific learning page (Python, JavaScript, Java, or Ruby).
5. Users can log out at any time, which clears their session.

## Notes

- The app currently uses a hardcoded `SECRET_KEY` for session management. For any real deployment, replace this with a securely generated key kept outside of source control (e.g., via an environment variable).
- The database is SQLite by default, which is convenient for development but not recommended for production use at scale.

## License

No license specified yet. Add one (e.g., MIT) if you plan to share or open this project up for contributions.
