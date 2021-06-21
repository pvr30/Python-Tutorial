from abc import ABCMeta, abstractmethod           
class Database:
    content = {'users': []}

    @classmethod
    def insert(cls, data):
        cls.content['users'].append(data)
    
    @classmethod
    def remove(cls, finder):
        cls.content['users'] = [user for user in cls.content['users'] if not finder(user)]
    
    @classmethod
    def find(cls, finder):
        return [user for user in cls.content['users'] if finder(user)]

class Saveable(metaclass=ABCMeta):
    def save(self):
        Database.insert(self.to_dict())
    
    # @classmethod (or @staticmethod, or @property)
    @abstractmethod  # @abstractmethod must always be the innermost decorator if used in conjunction with other decorators.
    def to_dict():
        pass

class User(Saveable):
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
        return 'Logged in!'
    
    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password
        }


class Admin(User):
    def __init__(self, username, password, access):
        super(Admin, self).__init__(username, password)
        self.access = access
    
    def __repr__(self):
        return f'<Admin {self.username}, access {self.access}>'

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'access': self.access
        }

a = Admin('paco', 'perez', 2)
b = Admin('rolf', 'smith', 1)

a.save()
b.save()

user = Database.find(lambda x: x['username'] == 'paco')[0]
user_obj = Admin(**user)
print(user_obj.username)

print(isinstance(user_obj, Saveable))  # This is True because it's a subclass

# You can do things like these without worry:

users_to_save = [a, b, User('jose', '1234')]
for u in users_to_save:
    u.save()  # This is fine, because all users (Admin and User) implement the Saveable interface so we know they have a .save() method