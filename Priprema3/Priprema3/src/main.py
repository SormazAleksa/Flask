
from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector
app = Flask(__name__)
app.config['SECRET_KEY'] = "RAF2021-2022"
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="", # ako niste nista menjali u phpmyadminu ovo su standardni
    # username i password
	database="naziv_baze" # iz phpmyadmin 
)

@app.route('/')
def index():
    return 'Hello world'


app.run(debug=True)
