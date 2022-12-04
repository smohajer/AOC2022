# --- Day 4: Camp Cleanup ---
#
# Space needs to be cleared before the last supplies can be unloaded from the ships,
# and so several Elves have been assigned the job of cleaning up sections of the camp. Every section has a unique ID
# number, and each Elf is assigned a range of section IDs.
#
# However, as some of the Elves compare their section assignments with each other, they've noticed that many of the
# assignments overlap. To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big
# list of the section assignments for each pair (your puzzle input).
#
# For example, consider the following list of section assignment pairs:
#
# 2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8
# For the first few pairs, this list means:
#
# Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second
# Elf was assigned sections 6-8 (sections 6, 7, 8). The Elves in the second pair were each assigned two sections. The
# Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also got
# 7, plus 8 and 9. This example list uses single-digit section IDs to make it easier to draw; your actual list might
# contain larger numbers. Visually, these pairs of section assignments look like this:
#
# .234.....  2-4
# .....678.  6-8
#
# .23......  2-3
# ...45....  4-5
#
# ....567..  5-7
# ......789  7-9
#
# .2345678.  2-8
# ..34567..  3-7
#
# .....6...  6-6
# ...456...  4-6
#
# .23456...  2-6
# ...45678.  4-8
#
# Some of the pairs have noticed that one of their assignments fully contains the
# other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully
# contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be
# cleaning, so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.
#
# In how many assignment pairs does one range fully contain the other?
#
# Your puzzle answer was 441.
#
# --- Part Two ---
#
# It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like
# to know the number of pairs that overlap at all.
#
# In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,
# 7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:
#
# 5-7,7-9 overlaps in a single section, 7.
# 2-8,3-7 overlaps all of the sections 3 through 7.
# 6-6,4-6 overlaps in a single section, 6.
# 2-6,4-8 overlaps in sections 4, 5, and 6.
# So, in this example, the number of overlapping assignment pairs is 4.
#
# In how many assignment pairs do the ranges overlap?
#
# Your puzzle answer was 861.

def get_input(file):
    """
    [['20-45', '13-44'],[...]...]
    :param file:
    :return:
    """
    with open(file, 'r') as f:
        lines = f.readlines()
        return [line.strip().split(',') for line in lines]


def get_ranges(assmnt):
    """
    Takes the input file list created earlier and will create a list of lists with each range split by '-'
    [[['20', '45'], ['13', '44']],[[...],[...]],...]
    :param assmnt:
    :return:
    """
    return [[rnge[0].split('-'), rnge[1].split('-')] for rnge in assmnt]


def get_nums(ranges):
    """
    takes the range list of list and splits into 4 nums, [Pair1 lower, upper, pair2 lower, upper] [[20, 45, 13, 44],[...]...]
    :param ranges:
    :return:
    """
    return [[int(range[0][0]), int(range[0][1]), int(range[1][0]), int(range[1][1])] for range in ranges]


def contained_pairs(ranges):
    """
    Sum up when either pair is contained withing the other pair:
    lower1 is less/equal lower2 and upper1 is more/equal upper2 or  (1-5,2-4)
    lower1 is more than lower2 and upper1 is less than upper2.      (2-3,1-5)
    :param ranges:
    :return:
    """
    return sum([num[0] <= num[2] and num[1] >= num[3] or num[0] >= num[2] and num[1] <= num[3] for num in ranges])


def overlap(ranges):
    """
    Sum up when overlap condition exists:
    lower2 is less than lower1 is less than upper2 or (2-5,1-3)
    lower2 is less than upper1 is less than upper3 or (2-3,2-5)
    lower1 is less than lower2 is less than upper1 or (1-3,2-5)
    lower1 is less than upper2 is less than upper1    (1-5,2-4)
    :param ranges:
    :return:
    """
    return sum([num[2] <= num[0] <= num[3] or num[2] <= num[1] <= num[3] or num[0] <= num[2] <= num[1] or num[0] <= num[
        3] <= num[1] for num in ranges])


if __name__ == '__main__':
    assignements = get_input('input')
    rang = get_ranges(assignements)
    nums = get_nums(rang)
    print(contained_pairs(nums))
    print(overlap(nums))
