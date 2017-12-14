from werkzeug.security import generate_password_hash, check_password_hash

class User(object):
    def __init__(self, username, password):
        self.__username = username
        self.__hash_pw = generate_password_hash(password)

    def get_username(self):
        return self.__username

    def get_hashed_pw(self):
        return self.__hashed_pw

Kent = User("khu1998", "default")

print(check_password_hash(Kent.get_hashed_pw(), "defaul"))
