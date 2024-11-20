import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="", # ako niste nista menjali u phpmyadminu ovo su standardni
    # username i password
	database="priprema1" # iz phpmyadmin
)

class Admin:

	__name_surname: str
	__username: str
	__password: str

	def __init__(self, name_surname: str, username: str, password: str):
		self.__name_surname = name_surname
		self.__username = username
		self.__password = password

	def get_name_surname(self):
		return self.__name_surname

	def get_username(self):
		return self.__username

	def get_password(self):
		return self.__password

	@staticmethod
	def check_if_username_exists(username: str):
		sql = 'SELECT username FROM users WHERE username LIKE = ?'
		cursor = mydb.cursor(prepared=True)

		cursor.execute(sql, (username, ))

		result = cursor.fetchone()

		if result:
			return True

		return False


	@staticmethod
	def register(name_surname: str, username: str, password: str, confirm_password: str):

		err = ''

		if name_surname == '' or username == '' or password == '' or confirm_password == '':
			err = 'Please fill all fields'
			return err

		if Admin.check_if_username_exists(username):
			err = 'Username already exists'
			return err

		if len(username) < 4:
			err = 'Username must be at least 4 characters'
			return err

		if len(password) <= 4:
			err = 'Password must be at least 8 characters'
			return err

		if password != confirm_password:
			err = 'Passwords do not match'
			return err

		sql = 'INSERT INTO users (username, password) VALUES (null, ?, ?, ?)'
		params = (name_surname, username, password)

		cursor = mydb.cursor(prepared=True)
		cursor.execute(sql, params)
		mydb.commit()

	@staticmethod
	def login(username: str, password: str):
		err = ''

		if username == '' or password == '':
			err = 'Please fill all fields'
			return err

		if not Admin.check_if_username_exists(username):
			err = 'Username is not in use. Please try again.'
			return err

		current_user = Admin.get_username()
		if password != current_user[3]:
			err = 'Passwords do not match'
			return err

		return err


