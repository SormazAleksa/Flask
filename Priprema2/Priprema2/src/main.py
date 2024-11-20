from flask import Flask, render_template, request, session, redirect, url_for

from Priprema2.src.projects import Projects
from users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = "RAF2021-2022"

@app.route('/')
def index():
    return 'Hello world'

@app.route('/register', methods=['GET','POST'])
def register():

    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        ime_prezime = request.form['ime_prezime']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        err = User.register(ime_prezime, email, password, confirm_password)

        if err != '':
            return render_template('register.html', greska = err)

        return redirect(url_for('show_all'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        err = User.login(email, password)
        if err != '':
            return render_template('login.html', greska = err)
        session['email'] = email
        return redirect(url_for('show_all'))

@app.route('/show_all')
def show_all():
    projects = Projects.fetch_all_projects()
    return render_template('show_all.html', projekti = projects)

@app.route('/dodaj_projekat', methods=['GET', 'POST'])
def dodaj_projekat():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'GET':
        return render_template('dodaj_projekat.html')
    elif request.method == 'POST':
        sifra_projekta = request.form['sifra_projekta']
        naziv = request.form['naziv']
        budzet = request.form['budzet']
        trajanje = request.form['trajanje']
        opis = request.form['opis']

        err = Projects.add_project(sifra_projekta, naziv, budzet, trajanje, opis)

        if err != '':
            return render_template('dodaj_projekat.html', greska = err)

        return redirect(url_for('show_all'))


@app.route('/logout')
def logout():
    if 'username' not in session:
        return redirect(url_for('login'))

    session.clear()
    return redirect(url_for('show_all'))

@app.route('/obrisi_projekat', methods=['POST'])
def obrisi_projekat():
    if 'username' not in session:
        return redirect(url_for('login'))

    sifra_projekta = request.form['sifra_projekta']

    Projects.delete_project(sifra_projekta)
    return redirect(url_for('show_all'))

@app.route('/pretraga_po_nazivu_projekta', methods=['POST'])
def pretraga_po_nazivu_projekta():
    naziv_projekta = request.form['naziv']
    projekti = Projects.search_project_by_name(naziv_projekta)
    return render_template('show_all.html', projects = projekti)

app.run(debug=True)
