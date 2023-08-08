from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def Home():
    return render_template("Homepage.html")

app.run(debug=True)