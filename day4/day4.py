start = 153517
end = 630395
s1 = 111111
s2 = 223450
s3 = 123789


def is_6_digit(input):
    return 99999 < input and input < 1000000


def is_monotonic_increase(input):
    lst = list(str(input))

    return lst == sorted(lst)


def invert(d):
    result = {}

    for k, v in d.items():
        result[v] = result.get(v, []) + [k]

    return result


def index_string(input):
    lst = list(input)

    return {i: x for i, x in enumerate(lst)}


def has_doubles(input):
    string = str(input)
    dct = index_string(string)
    inv_dct = invert(dct)

    for k, v in inv_dct.items():
        for i in v:
            if i + 1 in v and len(v) == 2:
                return True

    return False


def part1():
    counter = 0

    for n in range(start, end):
        if is_6_digit(n) and is_monotonic_increase(n) and has_doubles(n):
            counter += 1

    return counter
