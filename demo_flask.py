from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def welcome():
    return "<h2>Welcome, to Web World!!</h2>"

@app.route("/about")
def about():
    return "<h2>Hey, This is about me.</h2>"

if __name__ == '__main__':
    app.run(debug=True)

