import pdb
import re
from copy import deepcopy


class Moon:
    def __init__(self, x, y, z):
        self.position = {
            'x': x,
            'y': y,
            'z': z
        }
        self.velocity = {
            'x': 0,
            'y': 0,
            'z': 0
        }
        self.original_position = {
            'x': x,
            'y': y,
            'z': z
        }

    def update_velocity(self, moons):
        for moon in moons:

            if moon == self:
                pass
            else:
                if moon.position['x'] - self.position['x'] > 0:
                    self.velocity['x'] += 1
                elif moon.position['x'] - self.position['x'] < 0:
                    self.velocity['x'] -= 1
                else:
                    pass

                if moon.position['y'] - self.position['y'] > 0:
                    self.velocity['y'] += 1
                elif moon.position['y'] - self.position['y'] < 0:
                    self.velocity['y'] -= 1
                else:
                    pass

                if moon.position['z'] - self.position['z'] > 0:
                    self.velocity['z'] += 1
                elif moon.position['z'] - self.position['z'] < 0:
                    self.velocity['z'] -= 1
                else:
                    pass

    def update_position(self):
        self.position['x'] += self.velocity['x']
        self.position['y'] += self.velocity['y']
        self.position['z'] += self.velocity['z']

    def get_e_type(self, dict):
        sum = 0

        for value in dict.values():
            sum += abs(value)

        return sum

    def get_total_e(self):
        return self.get_e_type(self.position) * self.get_e_type(self.velocity)

    def is_original(self):
        return self.position == self.original_position

    def is_original_p_v(self, p):
        return self.position[p] == self.original_position[p] and self.velocity[p] == 0


def all_original_p_v(p, system):
    return system[0].is_original_p_v(p) and \
        system[1].is_original_p_v(p) and \
        system[2].is_original_p_v(p) and \
        system[3].is_original_p_v(p)


def match_cycle(p, system):
    steps(1, system)
    counter = 1

    while True:
        if all_original_p_v(p, system) is True:
            return counter
        else:
            steps(1, system)
            counter += 1


def get_cycles(system):

    x_cycle = match_cycle('x', [deepcopy(x) for x in system])
    y_cycle = match_cycle('y', [deepcopy(x) for x in system])
    z_cycle = match_cycle('z', [deepcopy(x) for x in system])

    return (x_cycle, y_cycle, z_cycle)


def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)


def lcm(a, b):
    return (a * b) / gcd(a, b)


def full_cycles(system):
    cycles = get_cycles(system)
    lcm1 = lcm(cycles[0], cycles[1])
    lcm2 = lcm(lcm1, cycles[2])

    return int(lcm2)


def steps(n, set):
    for i in range(n):
        [x.update_velocity(set) for x in set]
        [x.update_position() for x in set]


def display_positions(set):
    [print(x.position) for x in set]


def display_velocity(set):
    [print(x.velocity) for x in set]


def show(set):
    display_positions(set)
    print()
    display_velocity(set)


def get_system_energy(system):
    sum = 0

    for moon in system:
        sum += moon.get_total_e()

    return sum


def all_original(system):
    return system[0].is_original() and \
        system[1].is_original() and \
        system[2].is_original() and \
        system[3].is_original()


def part_2(system):
    steps(1, system)
    counter = 1

    while True:
        if all_original(system) is True:
            print(counter)

            break
        else:
            steps(1, system)
            counter += 1


def system_from_file(file):
    with open(file) as f:
        string = f.read()
    pattern = r"=.[0-9]*"
    matches = re.findall(pattern, string)
    numbers = [int(x[1:]) for x in matches]
    chunked_lst = list(chunk(numbers, 3))
    system = []

    for set in chunked_lst:
        system.append(Moon(set[0], set[1], set[2]))

    return system


def chunk(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


m1 = Moon(-1, 0, 2)
m2 = Moon(2, -10, -7)
m3 = Moon(4, -8, 8)
m4 = Moon(3, 5, -1)
m5 = Moon(-8, -10, 0)
m6 = Moon(5, 5, 10)
m7 = Moon(2, -7, 3)
m8 = Moon(9, -8, -3)


sample1 = [m1, m2, m3, m4]
sample2 = [m5, m6, m7, m8]

if __name__ == '__main__':
    system = system_from_file('input.txt')
