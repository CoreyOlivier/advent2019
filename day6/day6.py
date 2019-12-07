class Body(object):
    def __init__(self, name):
        self.name = name 
        self.orbited_by = []
        self.path_from_com = []
    
    def __repr__(self):
        return 'body: {}'.format(self.name)

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __sub__(self, other):
        return self.n_orbits_from_com - other.n_orbits_from_com

    def set_orbits(self, body):
        self.orbits = body
        
    def set_n_orbits_from_com(self, n):
        self.n_orbits_from_com = n

    def set_orbited_by(self, body):
        self.orbited_by.append(body)

    def get_path_from_com(self):
        if self.n_orbits_from_com == 1:
            pass
        else:
            self.path_from_com.append(self.orbits)
            self.orbits.get_path_from_com()
        self.path_from_com += self.orbits.path_from_com


def create_body_from_orbit(string):
    body_strs = string.split(')')
    for b in list(bodies):
        if b.name == body_strs[0]:
            b1 = b
            break
        else:
            b1 = Body(body_strs[0])

    for b in list(bodies):
        if b.name == body_strs[1]:
            b2 = b
            break
        else:
            b2 = Body(body_strs[1])

    b2.set_orbits(b1)
    b1.set_orbited_by(b2)
    bodies.add(b1)
    bodies.add(b2)


def get_n_from_prev(body):
    prev_n = body.orbits.n_orbits_from_com
    body.set_n_orbits_from_com(prev_n + 1)

def get_n_for_orbiting(body):
    if len(body.orbited_by) < 1:
        pass
    else: 
        for orbital in body.orbited_by:
            get_n_from_prev(orbital)
            get_n_for_orbiting(orbital)

def calc_ns():
    for b in list(bodies):
        if b.name == 'COM':
            get_n_for_orbiting(b)


def count_orbits(bodies):
    counter = 0
    for body in list(bodies):
        counter += body.n_orbits_from_com

    return counter

def parse_file():
    with open('input.txt') as f:
        file = f.read()
        lst = file.split('\n')
        lst = lst[:-1]

    return lst

def get_body(body_name):
    for b in list(bodies):
        if b.name == body_name:
            return b

def calculate_transfers_required(body1, body2):
    matching_path_points = []
    branch_point = None
    for point in body1.path_from_com:
        if point in body2.path_from_com:
            matching_path_points.append(point)
    for point in matching_path_points:
        if branch_point is None:
            branch_point = point
        elif branch_point.n_orbits_from_com < point.n_orbits_from_com:
            branch_point = point
    body1_distance_bp = body1 - branch_point - 1 
    body2_distance_bp = body2 - branch_point - 1 
    return body1_distance_bp + body2_distance_bp



def part1(orbits):
    for orbit in orbits:
        create_body_from_orbit(orbit)
    calc_ns()

def part2(orbits):
    part1(orbits)
    you = get_body('YOU')
    san = get_body('SAN')
    you.get_path_from_com()
    san.get_path_from_com()
    return you, san



test_orbits = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 
                'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']
input_orbits = parse_file()
reversed_orbits = reversed(test_orbits)
small_orbits = ['B)C', 'COM)B', 'C)D', 'B)E']
com = Body('COM')
com.set_n_orbits_from_com(0)
bodies = set([com])

