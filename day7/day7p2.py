from day5 import parse_file, op1, op2, op4, op5,\
        op6, op7, op8, parse_instructions
from day7 import op3
from itertools import permutations
from copy import copy
import pdb

class Amp:
    def __init__(self, prog, phase):
        self.prog = copy(prog)
        self.phase = phase
        self.stopped = False
        self.output = 0
        self.input =  None
        self.first_call = True
        self.op = None
        self.modes = {}
        self.position = 0
        self.needs_input = False
        self.input_counter = 0

    def status(self):
        return (self.letter, self.position, self.get_io_info())

    def get_io_info(self):
        return self.prog[26:]

    def set_input(self, value):
        self.input = value
        self.needs_input = False

    def read_input(self):
        self.input_counter +=1
        if self.first_call is True:
            self.first_call = False
            return self.phase
        return self.use_input()
    
    def use_input(self):
        self.needs_input = True
        return self.input

    def get_output(self):
        return self.output

    def set_output(self, value):
        self.output = value

    def is_stopped(self):
        return self.stopped

    def run(self):
        while True:

            self.op, self.modes = parse_instructions(self.prog[self.position])

            if self.op == '99':
                self.stopped = True
                break 
            elif self.op == '01':
               #pdb.set_trace()
                self.prog, self.position = op1(self.prog, self.position, 
                                               self.modes)
            elif self.op == '02':
                self.prog, self.position = op2(self.prog, self.position,
                                               self.modes)
            elif self.op == '03':
               # pdb.set_trace()
                if self.needs_input is True:
                    break
                self.prog, self.position = op3(self.prog, self.position,
                                           self.modes, self.read_input())
            elif self.op == '04':
                self.output, self.position = op4(self.prog, self.position,
                                                 self.modes)
            elif self.op == '05':
                self.prog, self.position = op5(self.prog, self.position,
                                               self.modes)
            elif self.op == '06':
                self.prog, self.position = op6(self.prog, self.position,
                                               self.modes)
            elif self.op == '07':
                self.prog, self.position = op7(self.prog, self.position,
                                               self.modes)
            elif self.op == '08':
                self.prog, self.position = op8(self.prog, self.position,

                                                    self.modes)
            else:
                print('invalid self.op')
                break

        
def power_thrusters(prog, perm):
    amps = [Amp(prog, phase) for phase in perm]
    #pdb.set_trace()
    first = amps[0]
    last = amps[4]
    last.set_input(0)
    idx = 0
    while True:
        curr = amps[idx]
        prev = amps[idx - 1]
        curr.set_input(prev.get_output())
        curr.run()
        if last.is_stopped() is True:
            #pdb.set_trace()
            break
        idx += 1
        if idx > 4:
            idx = 0

    return last.output
def test_phase_permutations(prog):
    perms = list(permutations(range(5,10)))
    max_thrust = 0
    for perm in perms:
        amps_out = power_thrusters(prog, perm)
        max_thrust = max(amps_out, max_thrust)
    return max_thrust
    

def test_power_thrusters(prog, perm, n):
    n_loops = list(range(n))
    amps = [Amp(prog, phase) for phase in perm]
    #pdb.set_trace()
    first = amps[0]
    last = amps[4]
    last.set_input(0)
    idx = 0
    for i in n_loops:
        for n in range(5):
            curr = amps[idx]
            prev = amps[idx - 1]
            curr.set_input(prev.get_output())
            curr.run()
            if i == n_loops[-1]:
                print('Amp ' + str(idx))
                [print((i,v)) for (i, v) in enumerate(curr.prog)]
                print(last.output)
            if last.is_stopped() is True:
                #pdb.set_trace()
                break
            idx += 1
            if idx > 4:
                idx = 0

    return last.output, amps

def part1_test():
    prog = parse_file()
    perms = list(permutations(range(0,5)))
    highest_output = 0
    for perm in perms:
        amps = [Amp(prog, phase) for phase in perm]
        amps[0].set_input(0)
        amps[0].run()
        amps[1].set_input(amps[0].get_output())
        amps[1].run()
        amps[2].set_input(amps[1].get_output())
        amps[2].run()
        amps[3].set_input(amps[2].get_output())
        amps[3].run()
        amps[4].set_input(amps[3].get_output())
        amps[4].run()
        highest_output = max(highest_output, amps[4].get_output())
    if highest_output == 22012:
        return 'pass'
    else:
        return 'fail'


sample1 =[
    3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
    27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5
        ] 
phases1 = (9,8,7,6,5)
sample2 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
    -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
    53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
sample_me = [3,10,1001,10,-3,10,4,10,99,0,0,0]
phases_me = (1,2)

phases2 = (9,7,8,5,6)

if __name__ == '__main__':
    #print('part1 ' + part1_test())
    #a = Amp(sample_me, 1)
    #b = Amp(sample_me, 2)
#
#    #if power_thrusters(sample1, phases1) == 139629729:
#    #    print('pass sample1')
#    #else:
    #    print('fail sample1')
    #amps = [Amp(sample1, 9, 'A'),
    #        Amp(sample1, 8, 'B'),
    #        Amp(sample1, 7, 'C'),
    #        Amp(sample1, 6, 'D'),
    #        Amp(sample1, 5, 'E')]
    test_power_thrusters(sample1, phases1, 7)
