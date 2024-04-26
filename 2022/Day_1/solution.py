def main():
    list_list = read_file("input.txt")
    parsed_input = []
    for item in list_list:
        data = item.split("\n")

        str_list = []
        for value in data:
            str_list.append(int(value))

        parsed_input.append(str_list)

    summed_list = []
    for item in parsed_input:
        summed_list.append(sum(item))

    summed_list.sort(reverse = True)
    return summed_list[0:3:1]

def read_file(filename):
    with open(filename, "r") as file:
        return file.read().split("\n\n") #returns list

print(main()[0])
print(sum(main()))