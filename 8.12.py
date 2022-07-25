def st(*toppings):
    for topping in toppings:
        print(topping)

def build_profile(fn,ln,**ui):
    profile = {}
    profile['first_name'] = fn
    profile['last_name'] = ln
    for k, v in ui.items():
        profile[k] = v
    return profile

ui = build_profile('first_name', 'last_name', age='25', local='country')

def make_car(model, color, **car_info):
    car = {}
    car['Car'] = model.title()
    car['Color'] = color.title()
    for key, value in car_info.items():
        car[key.title()] = value.title()
    return car


auto = make_car('outback', 'blue', brand='subaru', made_in='japan')

print(auto)


