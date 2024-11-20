import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="", # ako niste nista menjali u phpmyadminu ovo su standardni
	# username i password
	database="accounting" # iz phpmyadmin
)

class Applicants():

	__name: str
	__surname: str
	__tel: str
	__mail: str
	__company_name: str
	__pib: int

	def __init__(self, name: str, surname: str, tel: str, mail: str, company_name: str, pib: int):
		self.__name = name
		self.__surname = surname
		self.__tel = tel
		self.__mail = mail
		self.__company_name = company_name
		self.__pib = pib

	def __str__(self):
		result = f"Username: {self.__name}\n"
		result += f"Surname: {self.__surname}\n"
		result += f"Tel: {self.__tel}\n"
		result += f"Mail: {self.__mail}\n"
		result += f"Company: {self.__company_name}\n"
		return result

	@property
	def check_email(email):
		sql = "SELECT * FROM applicants WHERE email = ?"
		cursor = mydb.cursor(buffered=True)
		params = (email,)

		cursor.execute(sql, params)

		result = cursor.fetchone()
		if result:
			return True
		return False
