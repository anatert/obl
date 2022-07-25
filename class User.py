class User():

    def __init__(self, fname, sname, lname, nickname):
        self.fname = fname.title()
        self.sname = sname.title()
        self.lname = lname.title()
        self.nicname = nickname.title()
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print(f'First Name: {self.fname}\n'
              f'Second Name: {self.sname}\n'
              f'Last Name: {self.lname}\n'
              f'Nickname: {self.nicname}\n')

    def greet_user(self):
        print(f'Hello, {self.fname} {self.lname}\n')


u1 = User('FIRSTNAME1', 'SECONDNAME1', 'LASTNAME1', 'NICKNAME1')
u2 = User('FIRSTNAME2', 'SECONDNAME2', 'LASTNAME2', 'NICKNAME2')
u3 = User('FIRSTNAME3', 'SECONDNAME3', 'LASTNAME3', 'NICKNAME3')

u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.reset_login_attempts()
print(u1.login_attempts)