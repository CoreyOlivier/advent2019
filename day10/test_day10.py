from day10 import * 

small_sample = '''.#..#
.....
#####
....#
...##
'''

small_coords = [(1,0), (4,0), (0,2), (1,2), (2,2), (3,2), (4,2), (4,3), (3,4), (4,4)]

def test_asteroids_to_coords():
    assert asteroids_to_coords(small_sample) == small_coords

def test_get_line_slope():
    assert get_line_slope((1,3), (4,8)) == 5/3

def test_set_of_slopes():
    assert get_set_of_slopes(small_coords) == (3,4)
