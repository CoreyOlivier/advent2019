from day5 import parse_file, op1, op2, op4, op5,\
        op6, op7, op8, parse_instructions
from itertools import permutations
import pdb


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

def run_amp(prog, phase, signal):
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
            return output, True
        elif op == '01':
            prog, position = op1(prog, position, modes)
        elif op == '02':
            prog, position = op2(prog, position, modes)
        elif op == '03':
            prog, position = op3(prog, position, modes, signal)
        elif op == '04':
            output, position = op4(prog, position, modes)
            return output, False
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

def test_thrusters_loop(phases, prog):
    pdb.set_trace()
    progs = [prog for i in phases]
    stop = False
    amp_e_output = 0
    amp_a_output, stop = run_amp(progs[0], phases[0], amp_e_output)
    amp_b_output, stop = run_amp(progs[1], phases[1], amp_a_output)
    amp_c_output, stop = run_amp(progs[2], phases[2], amp_b_output)
    amp_d_output, stop = run_amp(progs[3], phases[3], amp_c_output)
    amp_e_output, stop = run_amp(progs[4], phases[4], amp_d_output)
    while stop is False:
        amp_a_output, stop = run_amp(progs[0], amp_e_output, amp_e_output)
        amp_b_output, stop = run_amp(progs[1], amp_a_output, amp_a_output)
        amp_c_output, stop = run_amp(progs[2], amp_b_output, amp_b_output)
        amp_d_output, stop = run_amp(progs[3], amp_c_output, amp_c_output)
        amp_e_output, stop = run_amp(progs[4], amp_d_output, amp_d_output)
    return amp_e_output


    
    



sample1 =[
    3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
    27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5
        ] 
phases1 = (9,8,7,6,5)
phase_permutations = list(permutations(range(5,10)))

if __name__ == '__main__':
    test_thrusters_loop((9,8,7,6,5), sample1)
