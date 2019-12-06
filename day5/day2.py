def op1(input_list, position):
    sum = input_list[input_list[position + 1]] + input_list[input_list[position + 2]]
    input_list[input_list[position + 3]] = sum

    return input_list


def op2(input_list, position):
    product = input_list[input_list[position + 1]] * input_list[input_list[position + 2]]
    input_list[input_list[position + 3]] = product

    return input_list


def parse_file(file):
    with open(file) as f:
        string = f.read().replace('\n', '')
    input_list = string.split(',')
    input_list = [int(x) for x in input_list]

    return input_list


def move(p1):
    return p1 + 4


def run_intcode(input_list):
    position = 0

    while True:
        if input_list[position] == 1:
            input_list = op1(input_list, position)
            position = move(position)
        elif input_list[position] == 2:
            input_list = op2(input_list, position)
            position = move(position)
        elif input_list[position] == 99:

            return input_list
        else:
            print(input_list)

            return


def part1():
    input_list = parse_file('input.txt')
    input_list[1] = 12
    input_list[2] = 2

    input_list = run_intcode(input_list)

    return input_list[0]


def part2():
    for n in range(0, 99):
        for i in range(0, 99):
            input_list = parse_file('input2.txt')
            input_list[2] = i
            input_list[1] = n
            input_list = run_intcode(input_list)

            if input_list[0] == 19690720:
                print(n)
                print(i)
                print(100 * n + i)

            else:
                pass
