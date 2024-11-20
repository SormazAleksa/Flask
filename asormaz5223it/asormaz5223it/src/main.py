from flask import Flask, render_template, request, session, redirect, url_for
from user import User
from zaposleni import Zaposleni


app = Flask(__name__)
app.config['SECRET_KEY'] = "RAF2021-2022"


@app.route('/')
def index():
	return 'Hello world'

@app.route('/register', methods=['GET', 'POST'])
def register():

	if request.method == 'GET':
		return render_template('register.html')

	elif request.method == 'POST':
		ime_prezime = request.form['ime_prezime']
		email = request.form['email']
		password = request.form['password']
		repeat_password = request.form['repeat_password']

		greska = User.registracija(ime_prezime, email, password, repeat_password)

		if greska != '':
			return render_template('register.html', greska = greska)

		return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():

	if request.method == 'GET':
		return render_template('login.html')

	elif request.method == 'POST':
		email = request.form['email']
		password = request.form['password']

		greska = User.login(email, password)
		if greska != '':
			return render_template('login.html', greska = greska)

		session['email'] = email
		return redirect(url_for('show_all'))


@app.route('/logout')
def logout():
	if 'email' not in session:
		return redirect(url_for('login'))
	session.clear()
	return redirect(url_for('show_all'))


@app.route('/show_all')
def show_all():
	zaposleni = Zaposleni.showAll()
	return render_template('show_all.html', zaposleni = zaposleni)


@app.route('/dodaj_zaposlenog', methods=['GET', 'POST'])
def dodaj_zaposlenog():
	if 'email' not in session:
		return redirect(url_for('login'))

	if request.method == 'GET':
		return render_template('dodaj_zaposlenog.html')

	elif request.method == 'POST':
		jmbg = request.form['jmbg']
		ime_prezime = request.form['ime_prezime']
		broj_radnih_sati = request.form['broj_radnih_sati']
		pozicija = request.form['pozicija']

		greska = Zaposleni.dodaj(jmbg, ime_prezime, broj_radnih_sati, pozicija)

		if greska != '':
			return render_template('dodaj_zaposlenog.html', greska = greska)

		return redirect(url_for('show_all'))

@app.route('/obrisi_zaposlenog', methods=['POST'])
def obrisi_zaposlenog():
	if 'email' not in session:
		return redirect(url_for('login'))

	jmbg_zaposleni = request.form['jmbg']

	Zaposleni.obrisi(jmbg_zaposleni)
	return redirect(url_for('show_all'))

@app.route('/pretraga_po_jmbg', methods=['POST'])
def pretraga_po_jmbg():
	if 'email' not in session:
		return redirect(url_for('login'))

	jmbg = request.form['jmbg']

	rez = Zaposleni.pretraga_po_jmbg(jmbg)

	return render_template('show_all.html', zaposleni = rez)

@app.route('/pretraga_po_broju_radnih_sati', methods=['POST'])
def pretraga_po_broju_radnih_sati():
	if 'email' not in session:
		return redirect(url_for('login'))

	broj_radnih_sati = request.form['broj_radnih_sati']
	rez = Zaposleni.pretraga_po_broju_radnih_sati(broj_radnih_sati)
	return render_template('show_all.html', zaposleni = rez)

@app.route('/pretraga_po_poziciji', methods=['POST'])
def pretraga_po_poziciji():
	if 'email' not in session:
		return redirect(url_for('login'))

	pozicija = request.form['pozicija']
	rez = Zaposleni.pretraga_po_poziciji(pozicija)
	return render_template('show_all.html', zaposleni = rez)

app.run(debug=True)

