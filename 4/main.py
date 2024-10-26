from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/html_route')
def html_route():
    return "<h1>Tekst</h1>"

@app.route('/multihtml_route')
def multihtml_route():
    return """
        <html>
            <head>
                <title>Title</title>
            </head>
            <body>
                <ul>
                    <li>1</li>
                    <li>2</li>
                    <li>3</li>
                </ul>
            </body>
        </html>
    """

@app.route('/render')
def render():
    return render_template("index.html")

@app.route('/render_param')
def render_param():

    num = 10

    return render_template('render_param.html', broj = num)

@app.route('/more_param_route')
def more_param_route():

    num1 = 10
    num2 = 20

    return render_template("/more_param.html", num1 = num1, num2 = num2)

app.run(debug=True)