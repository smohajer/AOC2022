def get_input(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        return [line.strip().split(',') for line in lines]


def get_ranges(assmnt):
    return [[rnge[0].split('-'), rnge[1].split('-')] for rnge in assmnt]


def get_nums(ranges):
    return [[int(range[0][0]), int(range[0][1]), int(range[1][0]), int(range[1][1])] for range in ranges]


def contained_pairs(ranges):
    return sum([num[0] <= num[2] and num[1] >= num[3] or num[0] >= num[2] and num[1] <= num[3] for num in ranges])


def overlap(ranges):
    return sum([num[2] <= num[0] <= num[3] or num[2] <= num[1] <= num[3] or num[0] <= num[2] <= num[1] or num[0] <= num[
        3] <= num[1] for num in ranges])


if __name__ == '__main__':
    assignements = get_input('input')
    rang = get_ranges(assignements)
    nums = get_nums(rang)
    print(contained_pairs(nums))
    print(overlap(nums))
