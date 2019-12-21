from intcode import parse_file
from robot import Robot
import pdb


class Game(Robot):
    def __init__(self, data):
        super().__init__(data)
        self.output = []
        self.score = 0

    def op4(self):
        try:
            param = self.get_param(1)
            self.output.append(param)
            self.add_tile()
            self.position += 2
        except Exception:
            print('error {} at P{}'.format('op4', self.position))
            print(self.get_status())

    def add_tile(self):
        if len(self.output) == 3:
            if self.output[2] not in [0, 1, 2, 3, 4]:
                self.set_score()
            else:
                self.locations_visited[(
                    self.output[0], -(self.output[1]))] = self.output[2]
                self.display()
                print()
            self.output = []
        else:
            pass

    def op3(self):
        try:
            self.store(self.get_input(), self.position + 1)
            self.position += 2
        except Exception:
            print('error {} at P{}'.format('op3', self.position))
            print(self.get_status())

    def pay_up(self):
        self.data[0] = 2

    def set_score(self):
        if self.output[0] == -1 and self.output[1] == 0:
            self.score = self.output[2]

    def get_input(self):
        return 0

        while True:
            inpt = input('input: ')

            if inpt == 'a':
                return -1
            elif inpt == 'd':
                return 1
            elif inpt == 's':
                return 0

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

    def continue_run(self):
        while True:
            if 2 in list(self.locations_visited.values()):
                self.run()
            else:
                break


if __name__ == '__main__':
    data = parse_file('input.txt')
    game = Game(data)
    game.pay_up()
    game.run()
    game.continue_run()
