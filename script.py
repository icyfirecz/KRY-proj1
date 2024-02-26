def numbers_to_indexes(number):
    #convert number to string
    number = str(number)
    if len(number) == 2:
        return int(number[0]), int(number[1])
    else:
        return 0, int(number[0])

def indexes_to_numbers(row, column):
    return int(str(row) + str(column))

def roll_list(lst):
    return [lst[-1]] + lst[:-1] 

def make_subtitution_table_for_day(day_in_month):
    substitution_table = [
        "a","b","c","č","d","e","ě","f","g",
        "h","i","j","k","l","m","n","o","p","q",
        "r","ř","s","š","t","u","v","w","x","y",
        "z","ž",".","?","-","/","1","2","3","4",
        "5","6","7","8","9","0"
    ]
    for _ in range(day_in_month-1):
        substitution_table = roll_list(substitution_table)
    substitution_table.append("")
    substitution_table.append("")
    substitution_table.append("")
    substitution_table.append("")
    substitution_table = [""] + substitution_table
    result = []
    for i in range(5):
        tmp = []
        for j in range(10):
            if i*10+j < len(substitution_table):
                tmp.append(substitution_table[i*10+j])
        result.append(tmp)
    return result
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
    # print(table)
    for row in table:
        print(row)
    dct = make_dict_from_table(table)
    subtitued_messages = []
    
    for i in range(1,9):
        with open(f"message{i}.txt", "r",encoding="utf-8") as file:
            text = file.read()
        subtitued_message = translate_message(text, dct)
        print(subtitued_message)
        with open(f"./subtitued/subtitued{i}.txt","w",encoding='utf-8') as file:
            file.write(subtitued_message)
        subtitued_messages.append(subtitued_message)
    formated_substitutions = []
    first_message = [f"{i}" for i in range(1,61)]
    #formated_substitutions.append(" | ".join(first_message))

    for message in subtitued_messages:
        mess = ", ".join(list(message))
        
            
        formated_substitutions.append(mess)
        
    with open("all_mesages_substitued1.csv", "w",encoding='utf-8') as file:
        for message in formated_substitutions:
            print(message,file=file)