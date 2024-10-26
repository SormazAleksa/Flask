from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="GazdaSogun0701*",
    db="crud_wsit",
)

if mydb:
    print(True)

@app.route('/')
def index():
    
    ime = "Mika"

    # Library
    student = {
        'ime' : "Aleksa",
        'prezime' : "Sormaz"
    }

    #List
    predmeti = [

        'Informacioni sistemi',
        'Web sistemi i tehnologije',
        'Dizajn i razvoj web strana',
    ]

    return render_template(
        'index.html',
        ime = ime,
        student = student,
        lista_predmeta = predmeti
    )

@app.route('profile/<username>')
def form_route():

    print(request.method)

    if request.method == 'GET':
        return render_template('form.html')
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == '' or password == '':
            return render_template('form.html', error = 'Morate popuniti sva polja')
        
    return f'{request.method} username={username} password={password}'

@app.route('/new_product', methods=['GET', 'POST'])
def new_product():
    if request.method == 'GET':
        return render_template('new_product.html')
    
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']

        if name == '' or price == '' or description == '':
            return render_template('new_product.html', error='Morate popuniti sva polja')
        
        if len(name) < 3:
            return render_template('new_product.html', error='Ime proizvoda mora imati bar 3 karaktera')
        
        if price < 100:
            return render_template('new_product.html', error='Cena mora biti veca od 100')
        
        cursor = mydb.cursor()
        sql_crud = f'INSERT INTO products (name, price, description) VALUES ("{name}", "{price}", "{description}")'

        cursor.execute(sql_crud)
        mydb.commit()
        return redirect('/')
    
@app.route('/products')
def products():

    cursor = mydb.cursor()
    sql_crud = 'SELECT * FROM products'
    cursor.execute(sql_crud)
    products = cursor.fetchall()


    return render_template('products.html', products=products)

@app.route('/change/<id>')
def change(id):
    cursor = mydb.cursor()
    sql_crud = f'SELECT * FROM products WHERE id = {id}'
    cursor.execute(sql_crud)
    products = cursor.fetchone()
    return render_template('change.html', product=products)

app.run(debug=True)