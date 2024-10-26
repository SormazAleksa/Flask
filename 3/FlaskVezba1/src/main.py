from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/italian')
def italian():
    return render_template("italian.html")

@app.route('/serbian')
def serbian():
    return render_template("serbian.html")



app.run(debug=True)
