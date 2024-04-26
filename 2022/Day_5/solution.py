def read_file(filename):
    with open(filename, "r") as file:
        return file.read().split("\n")

def parse_crates(crates_file:list) -> list:
    result = []
    for line in crates_file[:-1]:
        temp_str = ""
        for i in range(0, len(line), 4):
            temp_str = temp_str + line[i:i+4]
            if temp_str[-1] == " ":
                temp_str = temp_str[:-1]
            temp_str = temp_str + ","
        temp_str = temp_str[:-1].replace("[", "").replace("]", "").replace("   ", "_")
        result.append(temp_str.split(","))
    return result[::-1]

def parse_instructions(instructions_file:list) -> list:
    result = []
    for line in instructions_file:
        result.append(line.replace(" ", "").replace("move", "").replace("from", ",").replace("to", ",").split(","))
    keys = ["move", "from", "to"]
    result2 = []
    for i in result:
        temp_dict = {k:int(v) for (k,v) in zip(keys, i)}
        result2.append(temp_dict)
    return result2

def crateMover_9000(parsed_crates:list, parsed_instructions:list) -> list:
    for instruction in parsed_instructions:
        print("new instruction begins")

        from_index = instruction["from"] - 1
        to_index = instruction["to"] - 1
        move_num = instruction["move"]

        while move_num > 0:
            headspace = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

            i = parsed_crates.count(headspace)
            while i > 0:
                parsed_crates.remove(headspace)
                i -= 1

            n = 0
            m = -1

            if parsed_crates[-1] != headspace:
                print("headspace needed; adding an empty row.")
                parsed_crates.append(headspace)

            print(f"finding first open row from the bottom in column {to_index+1}")
            while True:
                if parsed_crates[n][to_index] != "_": # check for the top first open spot of the column we want to move "to"
                    print(f"(row {n+1}, column {to_index+1}) is NOT open, it contains {parsed_crates[n][to_index]}...")
                    n += 1 #go up an index
                else:
                    print(f"(row {n+1}, column {to_index+1}) is open.")
                    break
            
            print(f"finding first row with a letter from the top in column {from_index+1}")
            while True:
                if parsed_crates[m][from_index] == "_": # find top spot of a column with a crate we want to move "from"
                    print(f"(row {len(parsed_crates)+ 1 + m}, column {from_index+1}) is empty...")
                    m -= 1 #go down an index
                else:
                    print(f"(row {len(parsed_crates)+ 1 + m}, column {from_index+1}) has the letter {parsed_crates[m][from_index]}.")
                    break

            print(f"moving letter {parsed_crates[m][from_index]} from (row {len(parsed_crates)+ 1 + m}, column {from_index+1}) to (row {n+1}, column {to_index+1})")
            parsed_crates[n][to_index] = parsed_crates[m][from_index] # move the letter.
            parsed_crates[m][from_index] = "_"

            move_num -= 1 # decrement move_num
    
    print("\ndone")
    return parsed_crates

def crateMover_9001(parsed_crates:list, parsed_instructions:list) -> list:
    for instruction in parsed_instructions:
        print("new instruction begins")

        from_index = instruction["from"] - 1
        to_index = instruction["to"] - 1
        move_num = instruction["move"]

        headspace = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

        n = 0
        m = -1

        print(f"is there enough headspace to fit {move_num} crates?") # add headspace to fit all the crates that will be moved + 1.
        j = move_num
        s = parsed_crates.count(headspace)
        while s != j+1 :
            print("headspace needed; adding an empty row. Checking again...")
            parsed_crates.append(list(headspace))
            s += 1
        print(f"there is now a sufficient headspace of {parsed_crates.count(headspace)}")

        print(f"finding first open row from the bottom in column {to_index+1}")
        while True:
            if parsed_crates[n][to_index] != "_": # check for the top first open spot of the column we want to move "to"
                print(f"(row {n+1}, column {to_index+1}) is NOT open, it contains {parsed_crates[n][to_index]}...")
                n += 1 #go up an index
            else:
                print(f"(row {n+1}, column {to_index+1}) is open.")
                break

        print(f"finding first row with a letter from the top in column {from_index+1}")
        while True:
            if parsed_crates[m][from_index] == "_": # find top spot of a column with a crate we want to move "from"
                print(f"(row {len(parsed_crates)+ 1 + m}, column {from_index+1}) is empty...")
                m -= 1 #go down an index
            else:
                stack_of_crates = [] # lowest index is the top, highest index is the bottom
                for a in range(move_num): #repeat the lookup for the number of letters requested to move
                    print(f"(row {len(parsed_crates)+ 1 + m - a}, column {from_index+1-a}) has the letter {parsed_crates[m-a][from_index]}. Adding to stack...")
                    stack_of_crates.append(parsed_crates[m-a][from_index])
                    parsed_crates[m-a][from_index] = "_" #remove the crates from their original spots
                print(f"stack of crates to be moved is: {stack_of_crates}")
                break

        print(f"moving stack of crates {stack_of_crates} from origin (row {len(parsed_crates)+ 1 + m}, column {from_index+1}) to (row {n+1}, column {to_index+1})")
        g = 0
        while g < len(stack_of_crates):
            crate = stack_of_crates[(-1-g)]
            parsed_crates[n+g][to_index] = crate # stack.
            g += 1

        i = parsed_crates.count(headspace) #remove extra headspace
        while i > 0:
            parsed_crates.remove(headspace)
            i -= 1

    print("\ndone")
    return parsed_crates

def top_crates(final_crates):
    fixed_crates = list(reversed(final_crates))
    for each in fixed_crates:
        print(each)

def part1(parsed_crates = parse_crates(read_file("crates.txt")), parsed_instructions = parse_instructions(read_file("instructions.txt"))):
    final_crates = crateMover_9000(parsed_crates, parsed_instructions)
    print("\n----------------Part 1 answer----------------")
    top_crates(final_crates)

def part2(parsed_crates = parse_crates(read_file("crates.txt")), parsed_instructions = parse_instructions(read_file("instructions.txt"))):
    final_crates = crateMover_9001(parsed_crates, parsed_instructions)
    print("\n----------------Part 2 answer----------------")
    top_crates(final_crates)

part1()
part2()