'''

The function is not returning the correct values. Can you figure out why?

get_planet_name(3) # should return 'Earth'

'''

def get_planet_name(id):
    return {1: 'Mercury',
            2: 'Venus',
            3: 'Earth',
            4: 'Mars',
            5: 'Jupiter',
            6: 'Saturn',
            7: 'Uranus',
            8: 'Neptune'}.get(id, None)


if __name__ == '__main__':
    print(get_planet_name(3))
    print(get_planet_name(8))
    print(get_planet_name(10))