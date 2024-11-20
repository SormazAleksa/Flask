from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = "RAF2021-2022"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':
        username = request.form['username']
        name_surname = request.form['name_surname']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        err = Admin.register(username, name_surname, password, confirm_password)

        if err != '':
            return render_template('register.html', err=err)

        return redirect(url_for('show_all'))


@app.route('/login')
def login():

    if request.method == "GET":
        return render_template('login.html')

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        err = admin.login(username, password)
        if err != '':
            return render_template('login.html', err = err)

        session['username'] = username
        return redirect(url_for('show_all'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))



@app.route('/show_all/<student_id>')
def show_all():
    students = Student.showAll()
    return render_template('show_all.html', students=students)




if __name__ == '__main__':
    app.run(debug=True)
