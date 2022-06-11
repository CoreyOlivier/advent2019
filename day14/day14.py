import re
import math
import pdb
from collections import Counter
from copy import deepcopy


class Converter:
    """
    Something to reverse this structure.
    10 ORE => 10 A
    1 ORE => 1 B
    7 A, 1 B => 1 C
    7 A, 1 C => 1 D
    7 A, 1 D => 1 E
    7 A, 1 E => 1 FUEL
    """

    def __init__(self, world_constraints):
        self.equations = get_equations(world_constraints)
        self.lookup = self.generate_lookup()

    def get_ore_req(self, chemical):
        name = chemical.name
        self.lookup[name]

    def do_name_lookup(self, name):
        # chems = self.lookup[name]
        pass

    def generate_lookup(self):
        result = {}

        for eq in self.equations:
            result[eq[-1]] = eq[:-1]

        return result


class Chemical:
    def __init__(self, equation):
        self.equation = equation
        self.name = equation[-1][0]
        self.reagents = []
        self.qty_made = int(equation[-1][1])
        self.made = 0
        self.used = 0

    def __repr__(self):
        return self.name

    def set_reagents(self, reagents):
        self.reagents = reagents

    def make(self):

        for reagent in self.reagents:
            reagent[0].use(int(reagent[1]))
        self.made += self.qty_made

    def make_many_old(self, n):

        for reagent in self.reagents:
            reagent[0].use_many(int(reagent[1]), n)

        self.made += self.qty_made * n

    def use(self, qty):
        while True:
            if self.made - qty < 0:
                self.make()
            else:
                self.made -= qty

                break

    def use_many_old(self, amount, cycles):
        while True:

            if self.made - (cycles * amount) < 0:
                needed = (cycles * amount) - self.made
                print(needed)
                self.make_many(needed)
            else:
                self.made -= (cycles * amount)

                break

    def use_many(self, amount):

        while True:
            if amount <= self.made:
                self.made -= amount
                self.used += amount

                break
            elif self.made < amount:
                needed_exact = amount - self.made
                need_make = math.ceil(
                    needed_exact / self.qty_made) * self.qty_made

                for reagent in self.reagents:
                    if reagent[0] == ore:
                        ore.used += int((int(reagent[1])
                                         * need_make / self.qty_made))
                        ore.available -= int((int(reagent[1])
                                              * need_make / self.qty_made))
                    else:
                        reagent[0].use_many(int(reagent[1]) * need_make)
                self.made += need_make

    def get_reagent_dict(self):
        dct = {}

        for reagent in self.reagents:
            dct[reagent[0]] = int(reagent[1])

        return dct


def resolve(chemical, first=True):
    ore = 0
    non_ore = {}

    for key in chemical.get_reagent_dict().keys():
        value = chemical.get_reagent_dict()[key]

        if key == ore:
            ore += value
        elif key in non_ore.keys():
            non_ore[key] += value
        else:
            non_ore[key] = value

    return ore, non_ore


def resolve_dct(dct):
    pass


def combine_dict(d1, d2):
    return dict(Counter(d1) + Counter(d2))


class Ore(Chemical):
    def __init__(self):
        self.ore_req = 1
        self.name = 'ORE'
        self.qty_made = 1
        self.used = 0
        self.available = 1000000000000
        self.made = 0

    def resolve(self, x):
        pass

    def use(self, qty):
        self.used += qty
        self.available -= qty

        if ore.available == 0:
            return

    def use_many(self, n):
        self.used += n
        self.available -= n


def get_equations(string):
    pattern = r'\d+ \w+'
    eq_lst = [re.findall(pattern, x) for x in string.split('\n')]
    final_eq_lst = []

    for eq in eq_lst:
        final_eq_lst.append([tuple(reversed(x.split(' '))) for x in eq])

    return final_eq_lst


def get_chems(eqs):
    chems = {}

    for eq in eqs:
        chems[eq[-1][0]] = Chemical(eq)

    return chems


def add_reagents(chemicals):
    for c in list(chemicals.values()):
        if c == ore:
            pass
        else:
            reagents_str = c.equation[:-1]
            reagents_obj = []

            for reagent in reagents_str:
                reagents_obj.append((chemicals[reagent[0]], reagent[1]))

            c.set_reagents(reagents_obj)


def parse_file(file):
    with open(file) as f:
        file = f.read()

    return file


def find_all_used(chems):
    fuel.make()

    while True:
        zeros = []

        for chem in chems.values():
            if chem.made == 0:
                zeros.append(True)
            else:
                zeros.append(False)

        if all(zeros) is True:
            break
        fuel.make()


def binary_search(agents):
    start = 0
    end = 1000000000000

    while start < end:

        mid = (start + end) // 2
        comps = deepcopy(agents)
        comps['FUEL'].use_many(mid)
        print(mid)
        print(comps['ORE'].available)

        if comps['ORE'].available == 0:
            return mid
        elif comps['ORE'].available > 0:
            start = mid + 1
        elif comps['ORE'].available < 0:
            end = mid - 1

        else:
            print('broke')

    return comps


sample1 = """10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL
"""

sample2 = """157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT
"""


if __name__ == '__main__':
    file = parse_file('input.txt')
    eqs = get_equations(sample2)[:-1]
    chems = get_chems(eqs)
    ore = Ore()
    chems['ORE'] = ore
    add_reagents(chems)
    fuel = chems['FUEL']
    # chema = chems['A']
    # chemb = chems['B']
    # chemc = chems['C']
    # chemd = chems['D']
    # cheme = chems['E']
    a = binary_search(chems)
