from flask import Flask, render_template, request, redirect, session
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SECRET_KEY'] = 'sweet_secret_feyza_2025'
db.init_app(app)

with app.app_context():
    db.create_all()


questions = [
    {"q": "Flask nedir?", "a": "Web framework"},
    {"q": "HTML’de bağlantı etiketi hangisidir?", "a": "a"},
    {"q": "Python’da liste sıralamak için hangi fonksiyon kullanılır?", "a": "sorted"},
    {"q": "discord bot yazmak için hangi kütüphane kullanılır?", "a": "discord.py"},
    {"q": "Doğal Dil İşleme kütüphanesi nedir?", "a": "nltk"},
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        session["username"] = username

        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(username=username)
            db.session.add(user)
            db.session.commit()
        return redirect("/quiz")
    return render_template("index.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        score = 0
        for i, q in enumerate(questions):
            answer = request.form.get(f"q{i}")
            if answer and answer.strip().lower() == q["a"].lower():
                score += 1

        user = User.query.filter_by(username=session["username"]).first()
        user.last_score = score
        if score > user.best_score:
            user.best_score = score
        db.session.commit()
        return redirect("/result")
    return render_template("quiz.html", questions=questions)

@app.route("/result")
def result():
    user = User.query.filter_by(username=session["username"]).first()
    top_score = db.session.query(db.func.max(User.best_score)).scalar()
    return render_template("result.html", user=user, top_score=top_score)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
