
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

        position += 4

        return prog, position
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

        position += 4

        return prog, position
    except Exception:
        print('error op2 at position: ' + str(position))


def op3(prog, position, modes):
    value = int(input('input: '))
    try:
        if modes['mode0'] == 'position':
            prog[prog[position + 1]] = value
        else:
            prog[position + 1] = value

        position += 2

        return prog, position
    except Exception:
        print('error op3 at position: ' + str(position))
        print('value: ' + str(value))


def op4(prog, position, modes):

    try:
        if modes['mode0'] == 'position':
            output = prog[prog[position + 1]]
        else:
            output = prog[position + 1]

        position += 2

        return output, position
    except Exception:
        print('error op4 at position: ' + str(position))


def op5(prog, position, modes):
    if modes['mode0'] == 'position':
        if bool(prog[prog[position +1]]) is True:
            if modes['mode1'] == 'position':
                position = prog[prog[position + 2]]
            else:
                position = prog[position + 2]
        else:
            position += 3
    else:
        if bool(prog[position +1]) is True:
            if modes['mode1'] == 'position':
                position = prog[prog[position + 2]]
            else:
                position = prog[position + 2]
        else:
            position += 3
    return prog, position


def op6(prog, position, modes):
    if modes['mode0'] == 'position':
        if bool(prog[prog[position +1]]) is False:
            if modes['mode1'] == 'position':
                position = prog[prog[position + 2]]
            else:
                position = prog[position + 2]
        else:
            position += 3
    else:
        if bool(prog[position +1]) is False:
            if modes['mode1'] == 'position':
                position = prog[prog[position + 2]]
            else:
                position = prog[position + 2]
        else:
            position += 3
    return prog, position



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


def run_prog(prog):
    position = 0

    while True:
        try:
            op, modes = parse_instructions(prog[position])
            
        except Excpetion:
            pass
        finally:
#            print('position: ' + str(position))
#            print('modes: ')
#            print(modes)
            pass
            
        if op == '99':
            return prog
        elif op == '01':
#            print(prog[position], prog[position + 1],
#                    prog[position + 2], prog[position +3])
            prog, position = op1(prog, position, modes)
        elif op == '02':
#            print(prog[position], prog[position + 1],
#                    prog[position + 2], prog[position +3])
            prog, position = op2(prog, position, modes)
        elif op == '03':
#            print(prog[position], prog[position + 1],
#                    prog[position + 2], prog[position +3])
            prog, position = op3(prog, position, modes)
        elif op == '04':
#            print(prog[position], prog[position + 1],
#                    prog[position + 2], prog[position +3])
            output, position = op4(prog, position, modes)
            print(output)
        elif op == '05':
#            print(prog[position], prog[position + 1],
#                    prog[position + 2], prog[position +3])
            prog, position = op5(prog, position, modes)
        elif op == '06':
#            print(prog[position], prog[position + 1],
#                    prog[position + 2], prog[position +3])
            prog, position = op6(prog, position, modes)
        elif op == '07':
#            print(prog[position], prog[position + 1],
#                    prog[position + 2], prog[position +3])
            prog, position = op7(prog, position, modes)
        elif op == '08':
#            print(prog[position], prog[position + 1],
#                    prog[position + 2], prog[position +3])
            prog, position = op8(prog, position, modes)

        else:
            print('err')

            return prog, position



prog = parse_file()
sample0 = [1002, 4, 3, 4, 33]
sample1 = [1001, 4, 98, 4, 1]
sample2 = [3, 0, 4, 0, 99]
sample3 = [1001, 4, 100, 4, -1]
answers = [ 3545932 ] 
sample4  = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]


def op7(prog, position, modes):
    try:
        if modes['mode0'] == 'position':
            value1 = prog[prog[position + 1]]
            if modes['mode1'] == 'position':
                value2 = prog[prog[position + 2]]
            else:
                value2 = prog[position + 2]

        else:
            value1 = prog[position + 1]
            if modes['mode1'] == 'position':
                value2 = prog[prog[position + 2]]
            else:
                value2 = prog[position + 2]
        if value1 < value2:
            prog[prog[position + 3]] = 1
        else:
            prog[prog[position + 3]] = 0
        return prog, position + 4
    except Exception:
        print('error in new op 7')
            

def op8(prog, position, modes):
    try:
        if modes['mode0'] == 'position':
            value1 = prog[prog[position + 1]]
            if modes['mode1'] == 'position':
                value2 = prog[prog[position + 2]]
            else:
                value2 = prog[position + 2]

        else:
            value1 = prog[position + 1]
            if modes['mode1'] == 'position':
                value2 = prog[prog[position + 2]]
            else:
                value2 = prog[position + 2]
        if value1 == value2:
            prog[prog[position + 3]] = 1
        else:
            prog[prog[position + 3]] = 0
        return prog, position + 4
    except Exception:
        print('error in new op 7')
