import pdb


class coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_distance_on_wire(self, x):
        self.length = x

    def __repr__(self):
        return '({},{})'.format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.__repr__())

    def distance(self):
        return abs(self.x) + abs(self.y)


def parse_file():
    with open('input.txt') as f:
        file_string = f.read().strip('\n')
        directions_list = file_string.split('\n')

    return directions_list


def better_range(a, b):
    if a < b:
        return range(a, b)
    else:
        return reversed(range(b + 1, a + 1))


def get_end_coord(start, movement):
    direction = movement[0]
    magnitude = int(movement[1:])
    end = coordinate(start.x, start.y)

    if direction == 'R':
        end.x += magnitude

    elif direction == 'L':
        end.x -= magnitude

    elif direction == 'U':
        end.y += magnitude

    elif direction == 'D':
        end.y -= magnitude

    return end


def points_on_line(start, end):
    points = []

    if end.x != start.x:
        for x in better_range(start.x, end.x):
            points.append(coordinate(x, start.y))

    elif end.y != start.y:

        for y in better_range(start.y, end.y):
            points.append(coordinate(start.x, y))

    else:
        print('error in points_on_line')

    return points


def part1(directions):
    origin = coordinate(0, 0)
    path1_directions = directions[0].split(',')
    path2_directions = directions[1].split(',')
    path1_coords = [origin]
    path2_coords = [origin]
    path1_points = []
    path2_points = []
    intersections = []
    first_intersection = None
    distance = None

    last = path1_coords[-1]

    for move in path1_directions:
        path1_coords.append(get_end_coord(last, move))
        last = get_end_coord(last, move)

    last = path2_coords[-1]

    for move in path2_directions:
        path2_coords.append(get_end_coord(last, move))
        last = get_end_coord(last, move)

    pdb.set_trace()

    for i, point in enumerate(path1_coords[1:]):
        path1_points += points_on_line(path1_coords[i], point)

    for i, point in enumerate(path2_coords[1:]):
        path2_points += points_on_line(path2_coords[i], point)

    p1_points_set = set(path1_points)
    p2_points_set = set(path2_points)
    intersections = list(p1_points_set.intersection(p2_points_set))

    for intersection in intersections[1:]:
        int_dist = intersection.distance()

        if distance is None:
            distance = int_dist
            first_intersection = intersection

        elif distance > int_dist:
            distance = int_dist
            first_intersection = intersection
        else:
            pass

    return distance, first_intersection, path1_points, path2_points, intersections


def add_distance_to_coords(wire):
    for i, coord in enumerate(wire):
        coord.set_distance_on_wire(i)


arbitrarily_large_number = 9999999999999999999999
def zip_wires(wire1, wire2, intersections):
    result = arbitrarily_large_number

    for intersection in intersections:
        wire1_point_index = wire1.index(intersection)
        wire2_point_index = wire2.index(intersection)
        total = wire1[wire1_point_index].length + wire2[wire2_point_index].length

        if total < result:
            result = total

    return result


def foo():
    return 1


def part2(intersections, path1_points, path2_points):
    origin = coordinate(0, 0)

    try:
        originIndex = intersections.index(origin)
        intersections.pop(originIndex)
    except:
        pass

    add_distance_to_coords(path1_points)
    add_distance_to_coords(path2_points)

    zipped_elements = zip_wires(path1_points, path2_points, intersections)
    minimun_length = min([x[0].length + x[1].length for x in zipped_elements])

    return minimun_length


directions1 = ['R75,D30,R83,U83,L12,D49,R71,U7,L72',
               'U62,R66,U55,R34,D71,R55,D58,R83']
directions2 = ['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
               'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']

## TODO: delete this.
file = parse_file()
dis, integer, p1p, p2p, ints = part1(file)
add_distance_to_coords(p1p)
add_distance_to_coords(p2p)
print(zip_wires(p1p, p2p, ints))
