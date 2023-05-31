from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello Rk this side"


@app.route('/products')
def products():
    return "This is the page for products"

@app.route('/myPage')
def my_info():
    return "This is my own page"

if __name__ == '__main__':
    app.run(debug=True)
    # debug = True returns any of the error in the browser itself
    # app.run(port = 8000) This line of code will run the app on port number 8000
    # Flask has to be used only in the development mode and not in the production mode
    # If we want to use flask in the prodction mode then other sources should be used