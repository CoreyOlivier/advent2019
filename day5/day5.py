
def parse_file():
    with open('input.txt') as f:
        string = f.read().replace('\n', '')
        prog_list = string.split(',')

        return [int(x) for x in prog_list]


def op1(prog, position, modes):
    try:
        if modes['mode0'] == 'position':
            value0 = prog[prog[position + 1]]
        else:
            value0 = prog[position + 1]

        if modes['mode1'] == 'position':
            value1 = prog[prog[position + 2]]
        else:
            value1 = prog[position + 2]

        sum = value0 + value1

        if modes['mode2'] == 'position':
            prog[prog[position + 3]] = sum
        else:
            prog[position + 3] = sum

        return prog
    except Exception:
        print('error op1 at position: ' + str(position))


def op2(prog, position, modes):
    try:
        if modes['mode0'] == 'position':
            value0 = prog[prog[position + 1]]
        else:
            value0 = prog[position + 1]

        if modes['mode1'] == 'position':
            value1 = prog[prog[position + 2]]
        else:
            value1 = prog[position + 2]

        product = value0 * value1

        if modes['mode2'] == 'position':
            prog[prog[position + 3]] = product
        else:
            prog[position + 3] = product

        return prog
    except Exception:
        print('error op2 at position: ' + str(position))


def op3(prog, position, modes):
    value = int(input('input: '))
    try:
        if modes['mode0'] == 'position':
            prog[prog[position + 1]] = value
        else:
            prog[position + 1] = value

        return prog
    except Exception:
        print('error op3 at position: ' + str(position))
        print('value: ' + str(value))


def op4(prog, position, modes):

    try:
        if modes['mode0'] == 'position':
            output = prog[prog[position + 1]]
        else:
            output = prog[position + 1]

        return output
    except Exception:
        print('error op4 at position: ' + str(position))


def move(position, op):
    switcher = {
        '01': 4,
        '02': 4,
        '03': 2,
        '04': 2}

    return position + switcher.get(op, '')


def parse_instructions(code):
    string_code = format(code, '5').replace(' ', '0')
    op = str(string_code)[-2:]
    modes = {}
    modes_list = list(reversed(string_code[:-2]))

    for i, v in enumerate(modes_list):
        if v == '0':
            modes['mode{}'.format(i)] = 'position'
        else:
            modes['mode{}'.format(i)] = 'immediate'

    return op, modes


def part1(prog):
    position = 0

    while True:
        op, modes = parse_instructions(prog[position])

        if op == '99':
            return prog
        elif op == '01':
            prog = op1(prog, position, modes)
            position = move(position, op)
        elif op == '02':
            prog = op2(prog, position, modes)
            position = move(position, op)
        elif op == '03':
            prog = op3(prog, position, modes)
            position = move(position, op)
        elif op == '04':
            print(op4(prog, position, modes))
            position = move(position, op)
        else:
            print('err')

            return prog


def foo():
    v = input('bar?')
    print(v)

    return v


def bar():
    return foo()


prog = parse_file()
sample0 = [1002, 4, 3, 4, 33]
sample1 = [1001, 4, 98, 4, 1]
sample2 = [3, 0, 4, 0, 99]
sample3 = [1001, 4, 100, 4, -1]
