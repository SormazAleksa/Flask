import mysql.connector
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="", # ako niste nista menjali u phpmyadminu ovo su standardni
    # username i password
	database="priprema2" # iz phpmyadmin
)

class Projects:

	__sifra_projekta: int
	__naziv: str
	__budzet: float
	__trajanje: int
	__opis: str

	def __init__(self, sifra_projekta: int, naziv: str, budzet: float, trajanje: int, opis: str):
		self.__sifra_projekta = sifra_projekta
		self.naziv = naziv
		self.budzet = budzet
		self.trajanje = trajanje
		self.opis = opis

	def get_sifra_projekta(self):
		return self.__sifra_projekta

	def get_naziv(self):
		return self.naziv

	def get_budzet(self):
		return self.budzet

	def get_trajanje(self):
		return self.trajanje

	def get_opis(self):
		return self.opis

	@staticmethod
	def proveri_sifru_projekta(sifra_projekta):
		sql = 'SELECT * FROM projects WHERE sifra_projekta=?'
		cursor = mydb.cursor(prepared=True)
		cursor.execute(sql, (sifra_projekta,))

		rez = cursor.fetchone()

		if rez:
			return True
		return False

	@staticmethod
	def add_project(sifra_projekta, naziv, budzet, trajanje, opis):
		err = ''

		if sifra_projekta == '' or naziv == '' or budzet == '' or trajanje == '' or opis == '':
			err = 'Morate uneti sve podatke!'
			return err

		if Projects.proveri_sifru_projekta(sifra_projekta):
			err = 'Sifra projekta je vec u upotrebi! Probajte drugu sifru!'
			return err

		sql = 'INSERT INTO projects VALUES (null, ?, ?, ?, ?, ?)'

		cursor = mydb.cursor(prepared=True)
		cursor.execute(sql, (sifra_projekta, naziv, budzet, trajanje, opis))
		mydb.commit()
		return err

	@classmethod
	def napravi_objekat_od_reda(cls, lista):
		return cls(lista[1], lista[2], lista[3], lista[4], lista[5])

	@staticmethod
	def napravi_objekat_od_liste(lista):
		for i in range(len(lista)):
			lista[i] = Projects.napravi_objekat_od_reda(lista[i])
		return lista

	@staticmethod
	def fetch_all_projects():
		sql = 'SELECT * FROM projects'
		cursor = mydb.cursor(prepared=True)
		cursor.execute(sql)
		rez = cursor.fetchall()
		list_of_lists = Projects.decode_tupple_list(rez)
		objekti = Projects.napravi_objekat_od_liste(list_of_lists)
		return objekti

	@staticmethod
	def decode_tupple_list(lista):
		for i in range(len(lista)):
			lista[i] = Projects.decode_tupple(lista[i])
		return lista

	@staticmethod
	def decode_tupple(tapl):
		tapl = list(tapl)
		for i in range(len(tapl)):
			if isinstance(tapl[i], bytearray):
				tapl[i] = tapl[i].decode()
		return tapl

	@staticmethod
	def delete_project(sifra_projekta):
		sql = 'DELETE FROM projects WHERE sifra_projekta=?'
		cursor = mydb.cursor(prepared=True)
		cursor.execute(sql, (sifra_projekta,))
		mydb.commit()

	@staticmethod
	def search_project_by_name(naziv):
		sql = 'SELECT * FROM projects WHERE naziv LIKE ?'
		cursor = mydb.cursor(prepared=True)
		param = (f"%{naziv}%", )
		cursor.execute(sql, param)
		rez = cursor.fetchall()

		dekodirani = Projects.decode_tupple_list(rez)
		objekti = Projects.napravi_objekat_od_liste(dekodirani)
		return objekti



