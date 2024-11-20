import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="", # ako niste nista menjali u phpmyadminu ovo su standardni
    # username i password
	database="priprema1" # iz phpmyadmin
)

class Student:

	__name_surname: str
	__inex: str
	__study_year: int
	__average_grade: float

	def __init__(self, name_surname: str, index: str, study_year: int, average_grade: float):
		self.__name_surname = name_surname
		self.__inex = index
		self.__study_year = study_year
		self.__average_grade = average_grade



	def get_name_surname(self):
		return self.__name_surname

	def get_index(self):
		return self.__index

	def get_study_year(self):
		return self.__study_year

	def get_average_grade(self):
		return self.__average_grade


	@staticmethod
	def check_index():
		sql = 'SELECT * FROM student WHERE index = ?'
		params = (index, )
		cursor = mydb.cursor(buffered=True)
		cursor.execute(sql, params)

		result = cursor.fetchone()

		if result:
			return True

		return False

	@staticmethod
	def showAll():

		sql = 'SELECT * FROM student'
		cursor = mydb.cursor()
		cursor.execute(sql)

		tupple_array = cursor.fetchall()

		decoded_tupple_array = Student.decode_tupple(tupple_array)

		return decoded_tupple_array

	@staticmethod
	def add_student(name_surname: str, index: str, study_year: int, average_grade: float):

		err = ''

		if Student.check_index(index):
			err = 'Index already exists. You cannot add a student.'
			return err

		if ' ' not in name_surname:
			err = 'Name and surname is required.'
			return err

		if study_year < 1:
			err = 'Student must be studying for more than one year.'
			return err

		sql = 'INSERT INTO student VALUES (null, ?, ?, ?, ?)'
		cursor = mydb.cursor()
		cursor.execute(sql, (name_surname, index, study_year, average_grade))
		mydb.commit()
		return err

	@staticmethod
	def delete_student(index: str):

		err = ''

		if index == '' or index is None:
			err = 'Index is required.'
			return err

		if not Student.check_index(index):
			err = 'Index does not exist.'
			return err

		sql = 'DELETE FROM student WHERE index = ?'
		cursor = mydb.cursor()
		cursor.execute(sql, (index,))

		mydb.commit()
		return err

	@staticmethod
	def search_student_by_name():
		sql = 'SELECT * FROM student WHERE name = ?'
		cursor = mydb.cursor()
		cursor.execute(sql)

		tupple_array = cursor.fetchall()
		decoded_tupple_array = Student.decode_tupple(tupple_array)
		return decoded_tupple_array

	@staticmethod
	def decode_tupple(tupple_bytearray):

		tupple_bytearray = list(tupple_bytearray)

		for i in range(len(tupple_bytearray)):
			tupple_bytearray[i] = tupple_bytearray[i].decode()

		return tupple_bytearray

	@staticmethod
	def decode_tupple_array(tupple_bytearray):
		for i in range(len(tupple_bytearray)):
			tupple_bytearray[i] = Student.decode_tupple(tupple_bytearray[i])
		return tupple_bytearray
