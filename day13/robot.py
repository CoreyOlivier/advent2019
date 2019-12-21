from intcode import Intcode, parse_file


class Robot(Intcode):
    def __init__(self, data):
        super().__init__(data)
        self.direction = 90
        self.x_location = 0
        self.y_location = 0
        self.output = []
        self.locations_visited = {(0, 0): 1}

    def op4(self):
        try:
            param = self.get_param(1)
            self.output.append(param)
            self.position += 2
        except Exception:
            print('error {} at P{}'.format('op4', self.position))
            print(self.get_status())

    def move(self):
        try:

            if self.output[1] == 0:
                self.direction = (self.direction + 90) % 360
            elif self.output[1] == 1:
                self.direction = (self.direction - 90) % 360

            if self.direction == 90:
                self.y_location += 1
            elif self.direction == 180:
                self.x_location -= 1
            elif self.direction == 270:
                self.y_location -= 1
            elif self.direction == 0:
                self.x_location += 1

            self.output = []

        except Exception as e:
            print(e)
            print('error {} at P{}'.format('move', self.position))
            print(self.get_status())

    def get_coord(self):
        return (self.x_location, self.y_location)

    def should_paint(self):
        if len(self.output) == 2:

            return True

        else:
            return False

    def paint(self):
        self.locations_visited[self.get_coord()] = self.output[0]
        self.move()

    def read_paint(self):
        if self.get_coord() in self.locations_visited:
            self.set_input(self.locations_visited[self.get_coord()])
        else:
            self.set_input(0)

    def get_rows(self):
        rows = {}

        for key in self.locations_visited.keys():
            if key[1] in rows:
                rows[key[1]] = {**rows[key[1]],
                                key[0]: self.locations_visited[key]}
            else:
                rows[key[1]] = {key[0]: self.locations_visited[key]}

        sorted_rows = self.sort_row(rows)
        sorted_rows_columns = {}

        for key in sorted_rows.keys():
            sorted_rows_columns[key] = self.sort_row(sorted_rows[key])

        return sorted_rows_columns

    def sort_row(self, row):
        keys_list = []

        for key in row.keys():
            keys_list.append(key)
        keys_list.sort()
        sorted_row = {}

        for key in keys_list:
            sorted_row[key] = row[key]

        return sorted_row

    def shift_rows(self):
        rows = self.get_rows()
        shifted_rows = {}

        for key in rows.keys():
            shifted_rows[key + abs(min(rows))
                         ] = self.shift_y(rows, rows[key])

        return shifted_rows

    def get_lowest_x(self, rows):
        min_x = None

        for key in rows.keys():
            row_x = min(rows[key])

            if min_x is None:
                min_x = row_x
            else:
                min_x = min(min_x, row_x)

        return min_x

    def shift_y(self, rows, dict):
        min_x = self.get_lowest_x(rows)
        x_shifted = {}

        for key in dict.keys():
            x_shifted[key + abs(min_x)] = dict.get(key)

        return x_shifted

    def display(self):
        rows = self.shift_rows()
        rows_list = []
        black = ' '
        block = '\u2588'
        paddle = '\u2581'
        ball = '\u25CF'
        white = '\u2592'

        for i in range(min(rows), max(rows) + 1):
            if i in rows:
                row = []

                for j in range(0, max(rows[i]) + 1):
                    if j in rows[i]:
                        row.append(rows[i][j])
                    else:
                        row.append(0)
                row_string = ''.join(map(str, row))
                rows_list.append(row_string)

            else:
                rows_list.append([0])
        reversed_rows = reversed(rows_list)
        raw_display_string = '\n'.join(map(str, reversed_rows))
        black_display = raw_display_string.replace('0', black)
        blocks_display = black_display.replace('2', block)
        paddle_display = blocks_display.replace('3', paddle)
        ball_display = paddle_display.replace('4', ball)
        full_display = ball_display.replace('1', white)

        print(full_display)

    def run(self):
        try:

            self.position = 0

            while True:
                self.parse_instructions()

                import pdb

                if self.position == 343:
                    pdb.set_trace()

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

                    if self.should_paint() is True:
                        self.paint()
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


if __name__ == '__main__':
    file = parse_file('input.txt')
    robby = Robot(file)
    robby.run()
