from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Ensure the path is correct and the directory exists
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'todo.db')  
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/')
def hello_world():
    todo = Todo(title="First todo", desc="Start investing in stock market")
    db.session.add(todo)
    db.session.commit()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
