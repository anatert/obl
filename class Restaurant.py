class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 4

    def set_number_served(self, number):
        self.number_served = number


    def describe_restaurant(self):
        print(f'Restaurant name: {self.restaurant_name}\nCuisine type: {self.cuisine_type}')

    def open_restaurant(self):
        print('Restaurant is open')

    def increment_number_served(self, number):
        self.number_served += number

'''r1 = Restaurant('resto', 'france')
r2 = Restaurant('resto2', 'france2')
r3 = Restaurant('resto3', 'france3')

r1.set_number_served(13)

r1.increment_number_served(13)
print(r1.number_served)'''

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors.title()

    def print_flavors(self):
        print(f'Flavors: {self.flavors}')


icecream = IceCreamStand('reasfgh', 'wesfdgh', 'esrdhfjh')

icecream.print_flavors()