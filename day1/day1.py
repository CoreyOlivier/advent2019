def get_required_fuel(mass):
    result = int(mass)/3
    result = int(result)
    result = result-2
    return result


def parse_file(file):
    with open(file) as fp:
        content = fp.readlines()
    content = [x.strip() for x in content]
    
    return content

def calc_fuel_list(mass_list):
    fuel_list = []
    for mass in mass_list:
        fuel_list.append(get_required_fuel(mass))

    return fuel_list

def part1():
    mass_list = parse_file('input.txt')
    fuel_list = calc_fuel_list(mass_list)
    print(sum(fuel_list))

def recursive_fuel(mass):
    masses = [get_required_fuel(mass)]
    calculating = True
    while calculating is True:
        if get_required_fuel(masses[-1]) > 0:
            masses.append(get_required_fuel(masses[-1]))
        else:
            calculating = False
    return sum(masses)

def part2():
    mass_list = parse_file('input.txt')
    fuel_list = map(recursive_fuel, mass_list)
    print(sum(fuel_list))
