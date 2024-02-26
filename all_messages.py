import itertools

START_KEY_LENGTH = 8
END_KEY_LENGHT = 26
def split_by_various_key_lengths(text, start_key_length, end_key_length):
    # find the key length by comparing the index of coincidence
    # for different key lengths
    result = []
    for key_length in range(start_key_length, end_key_length+1):
        print(f"Calulating key Length: {key_length}")
        transposited = one_transposition(key_length, text)
        print("-"*100)
        print(f"For key length {key_length}:")
        for splitted in transposited:
            print(*splitted,sep="|")
        print("-"*100)
        result.append(transposited)
    return result
        
def one_transposition(key_length, text):
    line_count = len(text) // key_length
    line_count_f = len(text) / key_length
    if line_count_f != line_count:
        line_count += 1
    
    split_by_line_count = split_text_by_length(text,line_count)
    # Allign last list to be the same as everything else
    split_by_line_count[-1] = align_lst_for_length(split_by_line_count[-1],len(split_by_line_count[0]))
    tmp = ""
    # read the split by line count by columns
    char_number = 0
    while char_number < len(split_by_line_count[0]):
        for i in range(len(split_by_line_count)):
            tmp += split_by_line_count[i][char_number]
        char_number +=1

    return split_text_by_length(tmp, key_length)

def align_lst_for_length(row, length):
    aligned_last_row = ["" for _ in range(length)]
    for i in range(len(row)):
        aligned_last_row[i] = row[i]
    return aligned_last_row

def read_nth_chat_from_lst(lst, n):
    return lst[n]

def split_text_by_length(text, length):
    # split the text into a list of strings of length characters
    return [text[i:i+length] for i in range(0, len(text), length)]

def read_by_line(text, line_length):
    # make lists of line_length characters from text
    return [text[i:i+line_length] for i in range(0, len(text), line_length)]
if __name__ == "__main__":
    text_from_file = ''
    with open("./subtitued/subtitued2.txt", "r",encoding="utf-8") as file:
        text_from_file = file.read()
    text_from_file = "".join(text_from_file.split('\n'))
    result = split_by_various_key_lengths(text_from_file, START_KEY_LENGTH, END_KEY_LENGHT)
    for i in range(len(result)):
        with open(f"./transposed/t{i}.txt","w",encoding="utf-8") as file:
            for splitted in result[i]:
                print("-"*50,file=file)
                print(*splitted,sep=" | ",file=file)
    