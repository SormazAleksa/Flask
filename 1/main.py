from flask import Flask, render_template

# Import flask and template operators

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


class Korisnik:

    __username: str
    __userType: str
    __userDescription: str
    __profilePicture: str

    def __init__(self, username, userType, profilePicture, userDescription):
        self.__username = username
        self.__userType = userType
        self.__userDescription = userDescription
        self.__profilePicture = profilePicture

    def getUsername(self):
        return self.__username

    def getUserType(self):
        return self.__userType

    def getUserDescription(self):
        return self.__userDescription

    def getProfilePicture(self):
        return self.__profilePicture

    def setUsername(self, __new_username):
        if len(__new_username) < 3:
            print("Username must be at least 3 characters long")
            return

        self.__username = __new_username

    def setUserType(self, new_userType):
        if new_userType not in ["guest", "user", "admin", "editor"]:
            print("Invalid user type")
            return

        self.__userType = new_userType

    def setUserDescription(self, new_userDescription):
        if len(new_userDescription) < 3:
            print("Description must be at least 3 characters long")
            return

        self.__userDescription = new_userDescription

    def setProfilePicture(self, new_profilePicture):
        if len(new_profilePicture) < 3:
            print("Profile picture must be at least 3 characters long")
            return

        self.__profilePicture = new_profilePicture

    def __str__(self):
        return f"Username: {self.__username}\nUser type: {self.__userType}\nDescription: {self.__userDescription}\nProfile picture: {self.__profilePicture}\n"


@app.route("/userList")
def user_table():

    u1 = Korisnik("user1", "user", "profile1.jpg", "User 1 description")
    u2 = Korisnik("user2", "user", "profile2.jpg", "User 2 description")
    u3 = Korisnik("user3", "user", "profile3.jpg", "User 3 description")
    u4 = Korisnik("user4", "user", "profile4.jpg", "User 4 description")

    userList = [u1, u2, u3, u4]

    return render_template("user.html", userList=userList)


@app.route("/class_route")
def class_route():
    a1 = Korisnik("asormaz", "admin", "profile1.jpg", "Admin description")
    return render_template("class.html", user=a1)


@app.route("/profiles/<username>")
def profiles(username):
    return render_template("profile.html", username=username)


@app.route("/list_in_list")
def list_in_list():

    student_list = []

    student1 = ["Mika", "Mikic", "RAF", "3220it"]
    student2 = ["Pera", "Peric", "RAF", "3520it"]
    student3 = ["Zika", "Zikic", "RAF", "3820it"]
    student4 = ["Laza", "Lazic", "RAF", "5820it"]

    student_list.append(student1, student2, student3, student4)

    print(student_list)

    return render_template("list_in_list.html", student_list=student_list)


app.run(debug=True)
