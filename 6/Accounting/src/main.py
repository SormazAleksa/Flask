
from flask import Flask,render_template,request,session
import mysql.connector
app = Flask(__name__, template_folder='templates', static_folder='static')


app.config['SECRET_KEY'] = "RAF2021-2022"


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
	if request.method == 'GET':
		return render_template('register.html')

	if request.method == 'POST':
		name = request.form['name']
		surname = request.form['surname']
		phone = request.form['tel']
		email = request.form['email']
		company_name = request.form['company_name']
		pib = request.form['pib']
		pib = int(pib)

		print(name, surname, phone, email, company_name, pib)



app.run(debug=True)
