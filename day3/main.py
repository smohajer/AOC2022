def get_input():
    with open('input', 'r') as f:
        lines = f.readlines()
        return [line.strip() for line in lines]


def split_ruck(ruck):
    mid = int(len(ruck) / 2)
    return [ruck[:mid], ruck[mid:]]


def get_priority(char):
    pri = ord(char)
    if pri < 91:
        return pri - 38
    else:
        return pri - 96


def get_duplicate(ruck):
    for item in ruck[0]:
        if item in ruck[1]:
            return item


def get_sum(rucks):
    total = 0
    for ruck in rucks:
        pockets = split_ruck(ruck)
        char = get_duplicate(pockets)
        total += get_priority(char)
    return total


def get_elf_rucks(rucks):
    elf_rucks = []
    for i in range(0, len(rucks), 3):
        elf_rucks.append([rucks[i], rucks[i + 1], rucks[i + 2]])
    return elf_rucks


def get_elf_duplicates(elf_rucks):
    for item in elf_rucks[0]:
        if item in elf_rucks[1] and item in elf_rucks[2]:
            return item


def get_elf_sum(rucks):
    total = 0
    elf_rucks = get_elf_rucks(rucks)
    for rucks in elf_rucks:
        char = get_elf_duplicates(rucks)
        total += get_priority(char)
    return total


if __name__ == '__main__':
    rucks = get_input()
    print(get_sum(rucks))
    print(get_elf_sum(rucks))
