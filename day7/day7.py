from day5 import parse_file, op1, op2, op4, op5,\
        op6, op7, op8, parse_instructions
from itertools import permutations


def op3(prog, position, modes, value):
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

def run_amp(phase, signal):
    prog = parse_file()
    position = 0
    try:
        op, modes = parse_instructions(prog[position])
        prog, position = op3(prog, position, modes, phase)
    except Exceptionn:
        return
    
    while True:
        try:
            op, modes = parse_instructions(prog[position])
        except Exception:
            print('exception at instruction position: ' + str(position))
            pass
    
        if op == '99':
            return output
        elif op == '01':
            prog, position = op1(prog, position, modes)
        elif op == '02':
            prog, position = op2(prog, position, modes)
        elif op == '03':
            prog, position = op3(prog, position, modes, signal)
        elif op == '04':
            output, position = op4(prog, position, modes)
        elif op == '05':
            prog, position = op5(prog, position, modes)
        elif op == '06':
            prog, position = op6(prog, position, modes)
        elif op == '07':
            prog, position = op7(prog, position, modes)
        elif op == '08':
            prog, position = op8(prog, position, modes)

        else:
            print('err at position: ' + str(position))

            return 

def test_thrusters(phases):
    amp_a_output = run_amp(phases[0], 0)
    amp_b_output = run_amp(phases[1], amp_a_output)
    amp_c_output = run_amp(phases[2], amp_b_output)
    amp_d_output = run_amp(phases[3], amp_c_output)
    amp_e_output = run_amp(phases[4], amp_d_output)
    return amp_e_output

def test_phase_permutations(permutations):
    highest_output = 0
    for perm in permutations:
        amp_output = test_thrusters(perm)
        if highest_output < amp_output:
            highest_output = amp_output
    return highest_output


phase_permutations = list(permutations(range(0,5)))
