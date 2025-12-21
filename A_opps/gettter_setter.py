


class User:
    def __init__(self, name, password, email):
        #setter Methods to set the values
        self._name = name   # protected attribute 
        self.__password = password # private attribute
        self._email = email

        # getter Methods to get the values
        def get_name(self):
            return self._name

        def get_password(self):
            return self.__password

        def get_email(self):
            return self._email
     


user1 = User("vaibhav", "mypassword123", "vaibhav@example.com")

print(user1.__password) # accessing private attribute via getter method
print(user1._email) # accessing protected attribute via getter method