def numbers_to_indexes(number):
    #convert number to string
    number = str(number)
    if len(number) == 2:
        return int(number[0]), int(number[1])
    else:
        return 0, int(number[0])

def indexes_to_numbers(row, column):
    return int(str(row) + str(column))

def make_subtitution_table_for_day(day_in_month):
    substitution_table = [
        "", "a","b","c","č","d","e","ě","f","g",
        "h","i","j","k","l","m","n","o","p","q",
        "r","ř","s","š","t","u","v","w","x","y",
        "z","ž",".","?","-","/","1","2","3","4",
        "5","6","7","8","9","0","" ,"", "" , ""
    ]
    lst = [
        ["" for _ in range(10)],
        ["" for _ in range(10)],
        ["" for _ in range(10)],
        ["" for _ in range(10)],
        ["" for _ in range(10)],
    ]

    for i in range(len(substitution_table)):
        new_position = i + (day_in_month - 1)
        row_index = (new_position // 10) % 5
        column_index = new_position % 10
        lst[row_index][column_index] = substitution_table[i]

    # find the first empty element and move it to the front
    find_row = 0
    find_column = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == "":
                find_row = i
                find_column = j
                break
        if find_row != 0 or find_column != 0:
            break

    index = indexes_to_numbers(find_row, find_column)

    for i in range(index, 0,-1):
        if i == 0:
            lst[0][0] = ""
        row1, col1 = numbers_to_indexes(i-1)
        row2, col2 = numbers_to_indexes(i)
        lst[row2][col2] = lst[row1][col1]
    lst[0][0]= ""
    return lst
def make_dict_from_table(table):
    dct = {}
    for i in range(len(table)):
        for j in range(len(table[i])):
            dct[f"{i}{j}"] = table[i][j]
    return dct

def translate_message(text, dct):
    raw_message = "".join(text.split(' '))

    # group two characters together
    message = [raw_message[i:i+2] for i in range(0, len(raw_message), 2)]
    final_message = ""
    for pair in message:
        final_message+=dct.get(pair, ']')
    return final_message

if __name__ == "__main__":
    table = make_subtitution_table_for_day(11)
    dct = make_dict_from_table(table)
    # load file and read it
    subtitued_messages = []
    for i in range(1,9):
        with open(f"message{i}.txt", "r") as file:
            text = file.read()
        subtitued_message = translate_message(text, dct)
        with open(f"./subtitued/subtitued{i}.txt","w") as file:
            file.write(subtitued_message)
        subtitued_messages.append(subtitued_message)
    
    with open("all_mesages_substitued.txt", "w") as file:
        file.write("\n".join(subtitued_messages))
    connected_messages = "".join(subtitued_messages)
    # count number of each character in the message
    count = {}
    for char in connected_messages:
        count[char] = count.get(char, 0) + 1

    #print this dictionary by count ascending
    for key in sorted(count.keys()):
        print(f"{key}: {count[key]}")
    sorted_counts = sorted( ((v,k) for k,v in count.items()), reverse=True)
    with open("sorted_counts.txt", "w") as file:
        for count, char in sorted_counts:
            file.write(f"{char}: {count}\n")