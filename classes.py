'''class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()

    def describe_restaurant(self):
        print(f'Restaurant name: {self.restaurant_name}\nCuisine type: {self.cuisine_type}')

    def open_restaurant(self):
        print('Restaurant is open')

r1 = Restaurant('resto', 'france')
r2 = Restaurant('resto2', 'france2')
r3 = Restaurant('resto3', 'france3')

print(r1.describe_restaurant())
print(r2.describe_restaurant())
print(r3.describe_restaurant())'''

class User():

    def __init__(self, fname, sname, lname, nickname):
        self.fname = fname.title()
        self.sname = sname.title()
        self.lname = lname.title()
        self.nicname = nickname.title()

    def describe_user(self):
        print(f'First Name: {self.fname}\n'
              f'Second Name: {self.sname}\n'
              f'Last Name: {self.lname}\n'
              f'Nickname: {self.nicname}')

    def greet_user(self):
        print(f'Hello, {self.fname} {self.lname}')


u1 = User('FIRSTNAME1', 'SECONDNAME1', 'LASTNAME1', 'NICKNAME1')
u2 = User('FIRSTNAME2', 'SECONDNAME2', 'LASTNAME2', 'NICKNAME2')
u3 = User('FIRSTNAME3', 'SECONDNAME3', 'LASTNAME3', 'NICKNAME3')

print(u1.describe_user())
print(u2.describe_user())
print(u3.describe_user())
print(u1.greet_user())
print(u2.greet_user())
print(u3.greet_user())
