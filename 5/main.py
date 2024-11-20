from flask import Flask, url_for, render_template, request, redirect
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():

    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)

