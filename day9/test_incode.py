from day9 import Intcode

sample_data = [3, 1, 1201, 5, 4, 1, 209, 3, 99]


def test_input():
    comp = Intcode(sample_data)
    assert comp.input is None
    assert comp.needs_input is True
    comp.set_input(3)
    assert comp.input == 3
    assert comp.needs_input is False
    assert comp.use_input() == 3
    assert comp.needs_input is True


def test_extend_data():
    comp = Intcode(sample_data)
    comp.extend_data(999)
    assert len(comp.data) == 1000


def test_get_param():
    comp = Intcode(sample_data)
    comp.parse_instructions()
    assert comp.get_param(1) == 1
    comp.position = 2
    comp.parse_instructions()
    assert comp.get_param(1) == 1
    assert comp.get_param(2) == 4
    assert comp.get_param(3) == 1


def test_store():
    comp = Intcode(sample_data)
    comp.current_modes = {'mode1': 'position', 'mode2': 'relative'}
    comp.store(10, 0)
    assert comp.data[3] == 10
    comp.current_modes.pop('mode1')
    comp.relative_base = 2
    comp.store(15, 0)
    assert comp.data[2] == 15
    comp.store(23, 4)
    assert comp.data[6] == 23


def test_op1():
    comp = Intcode(sample_data)
    comp.position = 2
    comp.parse_instructions()
    comp.op1
    print(comp.data)
    assert comp.data[1] == 5
    assert comp.position == 6
