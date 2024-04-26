def read_file(filename): #takes filename, returns list (file split by newline)
    with open(filename, "r") as file:
        return file.read().split("\n")

def split_rucksack(file): #takes opened file list, returns list of lists (rucksacks)
    rucksacks = []
    for line in file:
        middle = len(line)//2
        new_line = line[:middle] + "|" + line[middle:]
        split_line = new_line.split("|")
        rucksacks.append(split_line)
    return rucksacks

def find_shared_items(rucksacks): #takes list of lists, returns list (shared_items)
    shared_items = []
    for rucksack in rucksacks:
        pocket1 = rucksack[0]
        pocket2 = rucksack[1]
        for item in pocket1:
            location = pocket2.find(item)
            if location != -1:
                shared_items.append(pocket2[location])
                break
    return shared_items

def create_groups(file):
    grouped_elves = []
    temp_grouping = []
    total_elves = len(file)
    i = 0
    while i != total_elves:
        j = 0
        while j < 3 :
            temp_grouping.append(file[i])
            i+=1
            j+=1
        grouped_elves.append(temp_grouping)
        temp_grouping = []
    return grouped_elves

def find_badges(grouped_elves): #takes list of lists, returns list (shared_items)
    badges = []
    for group in grouped_elves:
        elf1 = group[0]
        elf2 = group[1]
        elf3 = group[2]
        for item in elf1:
            location = elf2.find(item)
            if location != -1:
                in_elf1_and_elf2 = elf2[location]
                badge = elf3.find(in_elf1_and_elf2)
                if badge != -1:
                    badges.append(elf3[badge])
                    break
    return badges

def find_values(shared_items): #takes list, returns int (total_score)
    character_values = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total_score = 0
    for item in shared_items:
        item_score = character_values.find(item)+1
        total_score += item_score
    return total_score

def part1():
    file = read_file("input.txt")
    rucksacks = split_rucksack(file)
    shared_items = find_shared_items(rucksacks)
    total_score = find_values(shared_items)
    print(total_score)

def part2():
    file = read_file("input.txt")
    grouped_elves = create_groups(file)
    badges = find_badges(grouped_elves)
    total_score = find_values(badges)
    print(total_score)

part1()
part2()