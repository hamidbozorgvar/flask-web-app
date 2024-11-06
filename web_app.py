from flask import Flask,render_template


web_app=Flask(__name__)
@web_app.route("/")

def hello():
    #text="Hello, World! "
    #return text
    return render_template("index.html")
if __name__ == "__main__":
    web_app.run(debug=True)