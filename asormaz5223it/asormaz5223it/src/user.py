import mysql.connector
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="", # ako niste nista menjali u phpmyadminu ovo su standardni
	# username i password
	database="kolokvijum" # iz phpmyadmin 
)

class User:

	__ime_prezime: str
	__email: str
	__password: str
	
	def __init__(self, ime_prezime: str, email: str, password: str):
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
	def proveri_postojanje_email(email):
		sql = 'SELECT * FROM users WHERE email = ?'
		cursor = mydb.cursor(prepared=True)
		cursor.execute(sql, (email,))
		rez = cursor.fetchone()

		if rez:
			return True
		return False

	@classmethod
	def napravi_objekat_od_niza(cls, lista):
		return cls(lista[1], lista[2], lista[3])
	
	@staticmethod
	def dekodiraj_listu_taplova(tapl):
		tapl = list(tapl)
		n = len(tapl)
		for i in range(n):
			if isinstance(tapl[i], bytearray):
				tapl[i] = tapl[i].decode()
		return tapl

	@staticmethod
	def registracija(ime_prezime, email, password, repeat_password):
		greska = ''
	
		if ime_prezime == '' or email == '' or password == '' or repeat_password == '':
			greska = 'Morate uneti sve podatke'
			return greska

		if User.proveri_postojanje_email(email):
			greska = 'Email je vec u upotrebi'
			return greska
		
		if ' ' not in ime_prezime:
			greska = 'Morate uneti i ime i prezime'
			return greska
		
		if password != repeat_password:
			greska = 'Sifre se ne poklapaju'
			return greska
		
		if '@' not in email:
			greska = 'Email mora sadrzati @'
			return greska
		
		sql = 'INSERT INTO users values(null, ?, ?, ?)'
		cursor = mydb.cursor(prepared=True)
		cursor.execute(sql, (ime_prezime, email, password))
		mydb.commit()

		return greska

	@staticmethod
	def dohvati_korisnika_po_email(email):
		sql = 'SELECT * FROM users WHERE email = ?'
		cursor = mydb.cursor(prepared=True)
		cursor.execute(sql, (email,))
		rez = cursor.fetchone()
		dekodirani = User.dekodiraj_listu_taplova(rez)
		objekat = User.napravi_objekat_od_niza(dekodirani)

		return objekat

	@staticmethod
	def login(email, password):

		greska = ''

		if email == '' or password == '':
			greska = 'Morate uneti sve podatke'
			return greska

		if not User.proveri_postojanje_email(email):
			greska = 'Uneli ste ne postojeci email'
			return greska

		trenutni = User.dohvati_korisnika_po_email(email)
		if trenutni.get_password() != password:
			greska = 'Sifre se ne poklapaju'
			return greska

		return greska
		