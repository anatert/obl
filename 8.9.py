magicians = [
    'magician_1', 'magician_2', 'magician_3', 'magician_4', 'magician_5', 'magician_6'
]
great_magicians = []
def show_magicians(spis):
    for magician in spis:
        print(magician)


def make_great(spis):
    while spis:
        gm = spis.pop()
        great_magicians.append('great' + gm)



make_great(magicians[:])
show_magicians(great_magicians)
print(magicians)

