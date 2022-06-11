from day14 import get_equations, parse_file
import math
import re
import pdb
PATTERN = re.compile(r'(\d+) (\w+)')
sample1 = """10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL"""
sample2 = """157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"""

ore_per_fuel = 13312
fuel_for_tril = 82892753


class Chem:
    def __init__(self, eq):
        self.qty_made = int(eq[-1][1])
        self.name = eq[-1][0]
        self.reagents_lst = eq[:-1]

    def __repr__(self):
        return self.name


class Equation:
    def __init__(self, eq):
        self.reactants_tuple = eq[:-1]
        self.product = eq[-1]
        self.amount_made = int(self.product[1])
        self.reactants = {x[0]: int(x[1])for x in self.reactants_tuple}

    def __repr__(self):
        return str(self.reactants) + ' => ' + str(self.product)

    def get_reactants(self, needed):
        cycles = math.ceil(needed / self.amount_made)
        react_needed = {k: v * cycles for k, v in self.reactants.items()}

        return react_needed


class ORE(Equation):
    def __init__(self):
        self.amount_made = 1
        self.reactants = {'ORE': 1}


def get_eq_obj(eqs_str):
    eqs = {}
    eqs['ORE'] = ORE()

    for eq in eqs_str:
        eqs[eq[-1][0]] = Equation(eq)

    return eqs


def combine_dicts(dicts):
    result_dict = {}

    for dict in dicts:
        for k, v in dict.items():
            if k in result_dict:
                result_dict[k] += v
            else:
                result_dict[k] = v

    return result_dict


def get_reacts_condition(prod, n_made):

    if prod.amount_made % n_made != 0 and n_made > prod.amount_made:
        div = math.ceil(n_made / prod.amount_made)
        n_made -= div * prod.amount_made
        reactants = prod.get_reactants(div)
    elif prod.amount_made % n_made == 0 and n_made >= prod.amount_made:
        amt_remove = n_made
        reactants = prod.get_reactants(n_made)
        n_made -= amt_remove
    else:
        pass

    return reactants


def reacts_of_dict(dict):
    reacts = {}

    for k, v in dict.items():
        prod = eqs[k]
        reacts = combine_dicts([reacts, get_reacts_condition(prod, v)])

    reactants = {k: v for k, v in reactants.items() if v != 0}

    return reacts


def parse(lines):
    rules = {}

    for line in lines:
        srcs, last = {}, None

        for match in PATTERN.finditer(line):
            if last is not None:
                key, n = last
                srcs[key] = n
            last = match.group(2), int(match.group(1))
        key, n = last
        rules[key] = n, srcs

    return rules


if __name__ == '__main__':
    eqs_strs = get_equations(sample1)
    eqs = get_eq_obj(eqs_strs)
    fuel = eqs['FUEL']
