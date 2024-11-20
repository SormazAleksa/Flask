import mysql.connector
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="", # ako niste nista menjali u phpmyadminu ovo su standardni
    # username i password
	database="priprema2" # iz phpmyadmin
)

class User:

	__ime_prezime: str
	__email: str
	__password: str

	def __init__(self, ime_prezime, email, password):
		self.__ime_prezime = ime_prezime
		self.__email = email
		self.__password = password


	def get_ime_prezime(self):
		return self.__ime_prezime

	def get_email(self):
		return self.__email

	def get_password(self):
		return self.__password

	@staticmethod
	def check_email(email):
		sql = 'SELECT * FROM USERS WHERE email=?'
		cursor = mydb.cursor(prepared=True)
		cursor.execute(sql, (email,))

		rez = cursor.fetchone()
		if rez:
			return True
		return False

	@staticmethod
	def register(ime_prezime, email, password, confirm_password):
		err = ""

		if ime_prezime == '' or email == '' or password == '':
			err = 'Morate popuniti sve podatke!'
			return err

		if ' ' not in ime_prezime:
			err = 'Morate uneti i ime i prezime!'
			return err

		if '@' not in email:
			err = 'Morate uneti i email!'
			return err

		if len(password) < 4:
			err = 'Sifra mora biti minimalne duzine 4 karaktera!'
			return err

		if password != confirm_password:
			err = 'Sifre se ne poklapaju'
			return err

		if User.check_email(email):
			err = 'Email je vec u upotrebi!'
			return err

		sql = 'INSERT INTO USERS VALUES (null, ?, ?, ?)'
		cursor = mydb.cursor(prepared=True)
		cursor.execute(sql, (ime_prezime, email, password))
		mydb.commit()
		return err

	@classmethod
	def napravi_objekat_od_recnika(cls, lista):
		return cls(lista[1], lista[2], lista[3])

	@staticmethod
	def fetch_user_by_email(email):
		sql = 'SELECT * FROM users WHERE email = ?'
		cursor = mydb.cursor(prepared=True)
		cursor.execute(sql, (email, ))
		rez = cursor.fetchone()

		dekodirani = User.dekodiraj_tapl(rez)

		objekat = User.napravi_objekat_od_recnika(dekodirani)
		return objekat

	@staticmethod
	def dekodiraj_tapl(tapl):
		tapl = list(tapl)
		for i in range(len(tapl)):
			if isinstance(tapl[i], bytearray):
				tapl[i] = tapl[i].decode()
		return tapl

	@staticmethod
	def login(email, password):
		err = ''

		if email == '' or password == '':
			err = 'Morate popuniti sve podatke!'
			return err

		if not User.check_email(email):
			err = 'Uneli ste ne postojeci email!'
			return err

		current_user = User.fetch_user_by_email(email)

		if current_user.get_password() != password:
			err = 'Sifra se ne poklapa sa sifrom iz baze!'
			return err

		return err