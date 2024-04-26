def read_file(filename): #takes filename, returns list (file split by newline)
    with open(filename, "r") as file:
        return file.read().split("\n")

def pair_elves(file):
    paired_elves = []
    for elf in file:
        paired_elves.append(elf.split(","))
    return paired_elves

def split_ranges(paired_elves):
    split_ranges = []
    temp_list = []
    for pair in paired_elves:
        for range in pair:
            temp_list.append(list(map(int, range.split("-"))))
        split_ranges.append(temp_list)
        temp_list = []
    return split_ranges

def create_ranges(split_ranges):
    rangified_list = []
    for pair in split_ranges:
        temp_list = []
        for elf in pair:
            temp_list.append(set(range(elf[0],elf[1]+1)))
        rangified_list.append(temp_list)
    return rangified_list

def is_subset(rangified_list):
    score = 0
    for pair in rangified_list:
        set1 = pair[0]
        set2 = pair[1]
        if set1.issubset(set2) or set2.issubset(set1):
            score += 1
    return score

def is_overlapping(rangified_list):
    score = 0
    for pair in rangified_list:
        set1 = pair[0]
        set2 = pair[1]
        if set1 & set2:
            score += 1
    return score

def part1():
    print(is_subset(create_ranges(split_ranges(pair_elves(read_file("input.txt"))))))

def part2():
    print(is_overlapping(create_ranges(split_ranges(pair_elves(read_file("input.txt"))))))

part1()
part2()