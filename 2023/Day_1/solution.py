def main():
    file = read_file("input.txt")
    list_of_extracted_ints = []
    for item in file:
        list_of_extracted_ints.append(extract_numbers(item))
    print(list_of_extracted_ints)
    sum = 0
    for item in list_of_extracted_ints:
        sum += add_first_and_last(item)
    print(sum)

def read_file(filename):
    with open(filename, "r") as file:
        return file.read().split("\n") #returns list

def extract_numbers(item):
    extracted_ints = []
    item = item.replace("one", "o1ne")
    item = item.replace("two", "t2wo")
    item = item.replace("three", "th3ree")
    item = item.replace("four", "fo4ur")
    item = item.replace("five", "fi5ve")
    item = item.replace("six", "s6ix")
    item = item.replace("seven", "se7ven")
    item = item.replace("eight", "ei8ght")
    item = item.replace("nine", "n9ine")
    item = item.replace("zero", "z0ero")
    for character in item:
        if character in ("1234567890"):
            extracted_ints.append(character)
    return extracted_ints

def add_first_and_last(list):
    return int(list[0] + list[-1])

def insert_digit_for_word(string):
    string.find

main()