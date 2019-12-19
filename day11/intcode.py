import pdb
"""
OPS
op1 = ADD
op2 = Multiply
op3 = input
op4 = output
op5 = jump if true
op6 = jump if false
op7 = if < store 1 else 0
op8 = if = store 1 else 0
op9 = move relative base
53 = 0
"""


class Intcode:
    def __init__(self, data):
        self.data = data
        self.position = 0
        self.relative_base = 0
        self.needs_input = True
        self.input = None
        self.output = None
        self.current_op = None
        self.current_modes = {}
        self.status = {}
        self.current_params = {}

    def get_status(self):
        self.status = {'pos': self.position,
                       'current op': self.current_op,
                       'current modes': self.current_modes,
                       'relative_base': self.relative_base,
                       'needs input': self.needs_input,
                       'input': self.input,
                       'output': self.output,
                       }

        return self.status

    def set_input(self, inpt=None):
        self.input = inpt
        self.needs_input = False

    def use_input(self):
        if self.needs_input is True:
            self.input = int(input('input: '))
        self.needs_input = True

        return self.input

    def extend_data(self, idx):
        try:
            if list(self.current_modes.values())[0] == 'position':
                for i in range(len(self.data), self.data[self.data[idx]] + 1):
                    self.data.append(0)
            elif list(self.current_modes.values())[0] == 'relative':
                for i in range(len(self.data), self.relative_base + self.data[idx] + 1):
                    self.data.append(0)

        except Exception as e:
            print(e)
            print('error {} at P{}'.format('extend_data', self.position))
            print(self.get_status())

    def parse_instructions(self):
        try:
            code = self.data[self.position]
            code_string = format(code, '5').replace(' ', '0')
            op_string = str(code_string)[-2:]
            modes_list = list(reversed(code_string[:-2]))
            modes = {}

            for i, v in enumerate(modes_list):
                if v == '0':
                    modes['mode{}'.format(i + 1)] = 'position'
                elif v == '1':
                    modes['mode{}'.format(i + 1)] = 'immediate'
                elif v == '2':
                    modes['mode{}'.format(i + 1)] = 'relative'
            self.current_op = op_string
            self.current_modes = modes
        except Exception:
            print('error {} at P{}'.format('parse_instructions', self.position))
            print(self.get_status())

    def get_param(self, inc):
        try:
            if self.current_modes['mode{}'.format(inc)] == 'position':
                value = self.data[self.data[self.position + inc]]
            elif self.current_modes['mode{}'.format(inc)] == 'immediate':
                value = self.data[self.position + inc]
            elif self.current_modes['mode{}'.format(inc)] == 'relative':
                relative_inc = self.data[self.position + inc]
                value = self.data[self.relative_base + relative_inc]
            self.current_modes.pop('mode{}'.format(inc))

            return value
        except IndexError:
            self.extend_data(self.position + inc)

            return self.get_param(inc)

        except Exception as e:
            print(e)
            print('error {} at P{}'.format('get_param', self.position))

    def store(self, value, position):
        try:

            if list(self.current_modes.values())[0] == 'position':
                self.data[self.data[position]] = value
            elif list(self.current_modes.values())[0] == 'relative':
                self.data[self.relative_base + self.data[position]] = value
        except IndexError:
            self.extend_data(position)
            self.store(value, position)

    def op1(self):
        try:
            param1 = self.get_param(1)
            param2 = self.get_param(2)
            sum = param1 + param2
            self.store(sum, self.position + 3)
            self.position += 4
        except IndexError:
            self.extend_data(self.position + 3)
            self.op1()
        except Exception as e:
            print(e)
            print('error {} at P{}'.format('op1', self.position))

    def op2(self):
        try:
            param1 = self.get_param(1)
            param2 = self.get_param(2)
            product = param1 * param2
            self.store(product, self.position + 3)
            self.position += 4
        except IndexError:
            self.extend_data(self.position + 3)
            self.op2()
        except Exception:
            print('error {} at P{}'.format('op2', self.position))
            print(self.get_status())

    def op3(self):
        try:
            self.store(self.use_input(), self.position + 1)
            self.position += 2
        except Exception:
            print('error {} at P{}'.format('op3', self.position))
            print(self.get_status())

    def op4(self):
        try:
            param = self.get_param(1)
            self.output = param
            self.position += 2
        except Exception:
            print('error {} at P{}'.format('op4', self.position))
            print(self.get_status())

    def op5(self):
        try:
            param1 = self.get_param(1)
            param2 = self.get_param(2)

            if bool(param1) is True:
                self.position = param2
            elif bool(param1) is False:
                self.position += 3
        except Exception:
            print('error {} at P{}'.format('op5', self.position))
            print(self.get_status())

    def op6(self):
        try:
            param1 = self.get_param(1)
            param2 = self.get_param(2)

            if bool(param1) is False:
                self.position = param2
            elif bool(param1) is True:
                self.position += 3
        except Exception:
            print('error {} at P{}'.format('op6', self.position))
            print(self.get_status())

    def op7(self):
        try:
            param1 = self.get_param(1)
            param2 = self.get_param(2)

            if param1 < param2:
                self.store(1, self.position + 3)
            else:
                self.store(0, self.position + 3)

            self.position += 4
        except Exception:
            print('error {} at P{}'.format('op7', self.position))
            print(self.get_status())

    def op8(self):
        try:
            param1 = self.get_param(1)
            param2 = self.get_param(2)

            if param1 == param2:
                self.store(1, self.position + 3)
            else:
                self.store(0, self.position + 3)

            self.position += 4
        except Exception:
            print('error {} at P{}'.format('op8', self.position))
            print(self.get_status())

    def op9(self):
        try:
            param1 = self.get_param(1)
            self.relative_base += param1
            self.position += 2
        except Exception:
            print('error {} at P{}'.format('op9', self.position))
            print(self.get_status())

    def run(self):
        try:

            self.position = 0

            while True:
                self.parse_instructions()

                if self.current_op == '99':
                    break
                elif self.current_op == '01':
                    self.op1()
                elif self.current_op == '02':
                    self.op2()
                elif self.current_op == '03':
                    self.op3()
                elif self.current_op == '04':
                    self.op4()
                    print(self.output)
                elif self.current_op == '05':
                    self.op5()
                elif self.current_op == '06':
                    self.op6()
                elif self.current_op == '07':
                    self.op7()
                elif self.current_op == '08':
                    self.op8()
                elif self.current_op == '09':
                    self.op9()

        except Exception:
            print('error {} at P{}'.format('run', self.position))


def parse_file(file):
    with open(file) as f:
        string = f.read().replace('\n', '')
        data_list = string.split(',')

        return [int(x) for x in data_list]


sample1_d5 = [
    3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
    1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
    999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99


]
sample1_d9 = [
    109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99
]
sample2_d9 = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
sample3_d9 = [104, 1125899906842624, 99]


if __name__ == '__main__':
    file = parse_file('input.txt')
    comp = Intcode(file)
    comp.run()
