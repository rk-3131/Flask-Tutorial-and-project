from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///rk.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"
    
@app.cli.command("initdb")
def init_db():
    db.create_all()
    print("Database tables created")

# @app.route('/')
# def hello_world():
#     return "Hello Rk this side"
# above line of codes made above text as the homepage of the site
# we will be making the new webpage as homepage

@app.route('/')
def to_do():
    todo = Todo(title = "my title", desc = "my description")
    db.session.add(todo)
    db.session.commit()
    allTodo = Todo.query.all()
    return render_template('todo.html', allTodo = allTodo)

# Here we have created the instance of the query of the database provided in such way that we have got queries database. This is now sent to the index page using jinja2 extension

@app.route('/htmlPage')
def html_pages():
    return render_template('index.html')


@app.route('/products')
def products():
    return "This is the page for products"


@app.route('/myPage')
def my_info():
    return "This is my own page"


@app.route('/newHtml')
def another_page():
    allTodo = Todo.query.all()
    print(allTodo)
    return ""
# Above fumnction is used in the flask
# Whenever we go to newhtml page of the site at that point we will have our all the queries printed in the terminal


if __name__ == '__main__':
    app.run(debug=True)
    # debug = True returns any of the error in the browser itself
    # app.run(port = 8000) This line of code will run the app on port number 8000
    # Flask has to be used only in the development mode and not in the production mode
    # If we want to use flask in the prodction mode then other sources should be used