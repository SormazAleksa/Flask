from unicodedata import numeric
import mysql.connector
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="", # ako niste nista menjali u phpmyadminu ovo su standardni
    # username i password
	database="kolokvijum" # iz phpmyadmin 
)

class Zaposleni:
    
	__jmbg: str
	__ime_prezime: str
	__broj_radnih_sati: int
	__pozicija: str


	def __init__(self, jmbg: str, ime_prezime: str, broj_radnih_sati: str, pozicija: str):
		self.__jmbg = jmbg
		self.__ime_prezime = ime_prezime
		self.__broj_radnih_sati = broj_radnih_sati
		self.__pozicija = pozicija

	def get_jmbg(self):
		return self.__jmbg
	
	def get_ime_prezime(self):
		return self.__ime_prezime
	
	def get_broj_radnih_sati(self):
		return self.__broj_radnih_sati
	
	def get_pozicija(self):
		return self.__pozicija
	
	@classmethod
	def napravi_objekat_od_reda(cls, lista):
		return cls(lista[1], lista[2], lista[3], lista[4])
	
	@staticmethod
	def napravi_objekat_od_liste(lista):
		n = len(lista)
		for i in range(n):
			lista[i] = Zaposleni.napravi_objekat_od_reda(lista[i])
		return lista
	
	@staticmethod
	def dekodiraj_tapl(tapl):
		tapl = list(tapl)
		for i in range(len(tapl)):
			if isinstance(tapl[i], bytearray):
				tapl[i] = tapl[i].decode()
		return tapl

	@staticmethod
	def dekodiraj_listu_taplova(lista_taplova):
		for i in range(len(lista_taplova)):
			lista_taplova[i] = Zaposleni.dekodiraj_tapl(lista_taplova[i])
		return lista_taplova

	@staticmethod
	def showAll():
		sql = 'SELECT * FROM zaposleni'
		cursor = mydb.cursor(prepared=True)
		cursor.execute(sql)
		rez = cursor.fetchall()
		lista = Zaposleni.dekodiraj_tapl(rez)
		objekat = Zaposleni.dekodiraj_listu_taplova(lista)

		return objekat

	@staticmethod
	def proveri_da_li_postoji_jmbg(jmbg):
		sql = 'SELECT * FROM zaposleni WHERE jmbg = ?'
		cursor = mydb.cursor(buffered=True)
		cursor.execute(sql, (jmbg,))
		rez = cursor.fetchone()

		if rez:
			return True
		return False

	@staticmethod
	def dodaj(jmbg, ime_prezime, broj_radnih_sati, pozicija):
		greska = ''

		if len(jmbg) != 13 or jmbg.isnumeric() != True:
			greska = ('JMBG mora sadrzati iskljucivo brojeve, ne sme sadrzati '
			          'space-ove i mora biti duzine 13araktera!')
			return greska
		
		if ' ' not in ime_prezime:
			greska = 'Morate uneti i ime i prezime'
			return greska
		
		if int(broj_radnih_sati) < 40:
			greska = 'Zaposleni mora imati minimalno 40 radnih sati'
			return greska
		
		if pozicija == '':
			greska = 'Zaposleni mora imati poziciju na kojoj radi!'
			return greska
		

		sql = 'INSERT INTO zaposleni VALUES (null, ?, ?, ?, ?)'
		cursor = mydb.cursor(prepared=True)
		cursor.execute(sql, (jmbg, ime_prezime, broj_radnih_sati, pozicija))
		mydb.commit()

		return greska

	@staticmethod
	def obrisi(jmbg):
		sql = 'DELETE FROM zaposleni WHERE jmbg = ?'
		cursor = mydb.cursor(prepared=True)
		cursor.execute(sql, (jmbg,))
		mydb.commit()

	@staticmethod
	def pretraga_po_jmbg(jmbg):
		sql = 'SELECT * FROM zaposleni WHERE jmbg LIKE ?'
		cursor = mydb.cursor(prepared=True)
		cursor.execute(sql, (jmbg,))
		mydb.commit()

	@staticmethod
	def pretraga_po_poziciji(pozicija):
		sql = 'SELECT * FROM zaposleni WHERE pozicija = ?'
		cursor = mydb.cursor(prepared=True)
		cursor.execute(sql, (pozicija,))
		mydb.commit()

	@staticmethod
	def pretraga_po_broju_radnih_sati(broj_radnih_sati):
		sql = 'SELECT * FROM zaposleni WHERE broj_radnih_sati = ?'
		cursor = mydb.cursor(prepared=True)
		cursor.execute(sql, (broj_radnih_sati,))
		mydb.commit()