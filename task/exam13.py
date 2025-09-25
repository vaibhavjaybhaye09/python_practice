# Create a LoggerMixin class that logs method calls. 
# Then, create Database and User classes that inherit from LoggerMixin and demonstrate logging.

class LoggerMix():
    def log(self, method):
       print( f"Calling Method : {method}")
       

class Database(LoggerMix):
    def connect(self):
        self.log("Connect")
        print("Connect to datbase")
        
class User(LoggerMix):
    def login(self):
        self.log("login")
        print("user logged in")
        
db = User()
db.login()