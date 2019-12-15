def opcode_compile(opcode):
    operations = {1: '+', 2: '*', 7: '<', 8: '=='}
    relative_base = 0
    codes_1 = {0: 'opcode[opcode[i+1]]', 1: 'opcode[i+1]', 2: 'opcode[opcode[i+1] + relative_base]'}
    codes_2 = {0: 'opcode[opcode[i+2]]', 1: 'opcode[i+2]', 2: 'opcode[opcode[i+2] + relative_base]'}
    codes_3 = {0: 'opcode[opcode[i+3]]', 1: 'opcode[i+3]', 2: 'opcode[opcode[i+3] + relative_base]'}
    bools = {True: 1, False: 0}

    i = 0
    while i < len(opcode):
        instruct = opcode[i]
        mode_1 = 0
        mode_2 = 0
        mode_3 = 0
        if len(str(instruct)) > 3:
            mode_3 = (instruct // 10000) % 10

        if len(str(instruct)) > 2:
            mode_1 = (instruct // 100) % 10
            mode_2 = (instruct // 1000) % 10
            instruct %= 10

        if instruct == 1 or instruct == 2:
            exec(codes_3[mode_3] + '=' + codes_1[mode_1] + operations[instruct] + codes_2[mode_2])
            i += 4

        elif instruct == 3:
            exec(codes_1[mode_1] + '=' + input("Digit please: "))
            i += 2

        elif instruct == 4:
            print(eval(codes_1[mode_1]))
            i += 2

        elif instruct == 5:
            if eval(codes_1[mode_1]):
                i = eval(codes_2[mode_2])
            else:
                i += 3

        elif instruct == 6:
            if not eval(codes_1[mode_1]):
                i = eval(codes_2[mode_2])
            else:
                i += 3

        elif instruct == 7 or instruct == 8:
            exec(codes_3[mode_3] + '=' + str(bools[eval(codes_1[mode_1] + operations[instruct] + codes_2[mode_2])]))
            i += 4

        elif instruct == 9:
            relative_base += int(eval(codes_1[mode_1]))
            i += 2

        elif instruct == 99:
            return


if __name__ == '__main__':
    with open("input", "r") as file:
        opcode = file.read()

    opcode = [int(n) for n in opcode.split(',')] + [0]*100000
    # Part 1 and 2 use the same code
    # For Part 1 run the intcode computer and input: 1
    # For Part 2 run the intcode computer and input: 2
    opcode_compile(opcode)
