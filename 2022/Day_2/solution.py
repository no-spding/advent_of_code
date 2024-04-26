def part1():
    list_of_rounds = read_file("input.txt")
    list_of_split_rounds = split_item(list_of_rounds)
    result = 0
    for item in list_of_split_rounds:
        result += determine_result_part1(item)
    return result

def part2():
    list_of_rounds = read_file("input.txt")
    list_of_split_rounds = split_item(list_of_rounds)
    result = 0
    for item in list_of_split_rounds:
        result += determine_result_part2(item)
    return result

def read_file(filename):
    with open(filename, "r") as file:
        return file.read().split("\n") #returns list

def split_item(list):
    new_list = []
    for item in list:
        new_list.append(item.split(" "))
    return new_list

def determine_result_part1(round):
    # opponent = a is rock, b is paper, c is scissors

    # you = x is rock, y is paper, z is scissors
    # rock = 1, paper = 2, scissors = 3

    # loss = 0, draw = 3, win = 6

    #returns round_score integer

    if round[0] == "A":
        if round[1] == "X":
            return 1+3
        if round[1] == "Y":
            return 2+6
        if round[1] == "Z":
            return 3+0
    if round[0] == "B":
        if round[1] == "X":
            return 1+0
        if round[1] == "Y":
            return 2+3
        if round[1] == "Z":
            return 3+6
    if round[0] == "C":
        if round[1] == "X":
            return 1+6
        if round[1] == "Y":
            return 2+0
        if round[1] == "Z":
            return 3+3

def determine_result_part2(round):
    # opponent = a is rock, b is paper, c is scissors

    # you = x is LOSE, y is DRAW, z is WIN
    # rock = 1, paper = 2, scissors = 3

    # loss = 0, draw = 3, win = 6

    #returns round_score integer
    if round[0] == "A": # rock
        if round[1] == "X": #scissors loses
            return 3+0
        if round[1] == "Y": #rock draws
            return 1+3
        if round[1] == "Z": #paper wins
            return 2+6
    if round[0] == "B": # paper
        if round[1] == "X": #rock loses
            return 1+0
        if round[1] == "Y": #paper draws
            return 2+3
        if round[1] == "Z": #scissors wins
            return 3+6
    if round[0] == "C": # scissors
        if round[1] == "X": #paper loses
            return 2+0
        if round[1] == "Y": #scissors draws
            return 3+3
        if round[1] == "Z": #rock wins
            return 1+6

print(part1())
print(part2())