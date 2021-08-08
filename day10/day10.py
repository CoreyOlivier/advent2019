import pdb

class Asteroid:
    def __init__(self, ( x, y )):
        self.x = x
        self.y = y
        self.slopes_detected = set()
        self.point( self.x, self.y )

    def __str__(self):
        return self.point

    def add_slopes(self, asteroid):
        self.slopes_detected.add(get_line_slope(self.point, asteroid.point))
        self.slopes_detected.add(get_line_slope(asteroid.point, self.point))
        

def string_to_coords(asteroids_string):
    asteroid_rows = asteroids_string.split('\n')
    asteroid_coords = []
    for (y, row) in enumerate(asteroid_rows):
        for (x, j) in enumerate(str(row)):
            if j == '#':
                asteroid_coords.append((x,y))
    return asteroid_coords

def get_line_slope(p1, p2):
    if p1 == p2:
        pass
    else:
        delta_y = p2[1] - p1[1]
        delta_x = p2[0] - p1[0]
        if delta_y == 0:
            return 'undef'
        if delta_x == 0:
             return 0
        return delta_y / delta_x

def get_set_of_slopes(asteroids):
    pass

def convert_to_objects(coords):
    asteroids = []
    for asteroid in coords:
        asteroids.append(Asteroid(asteroid))
    return asteroids


def parse_file(file):
    with open(file) as f:
        file = f.readlines()
    return ''.join(file)


if __name__ == '__main__':
    file = parse_file('input.txt')
    coords = string_to_coords(file)
    asteroids = convert_to_objects(coords)
