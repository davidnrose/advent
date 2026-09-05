with open("day_2_input.txt", "r") as file:
    string = file.read()

def split_string(string):
    lst = string.split(",")
    return lst

def get_string_pairs(lst):
    return [l.split("-") for l in lst]

def generate_between_pairs(str_pairs):
    int_pairs = []
    for sp in str_pairs:
        pair = [int(s) for s in sp]
        int_pairs.append(pair)

    all_nums = []
    for pair in int_pairs:
        nums = []
        start = pair[0]
        end = pair[1]
        while start <= end:
            if len(str(start)) % 2 == 0:
                nums.append(start)
            else: 
                pass
            start += 1
        all_nums.append(nums)

    return all_nums

# add all the lists together into a single big list
def combine_lists_into_single(lst):
    new_list = []
    for l in lst:
        new_list = new_list + l

    return new_list

# ccheck if a number follows the pattern
def check_pattern(num):

    # force to string
    num_str = str(num)

    # get length
    len_ = len(num_str)
    half_len = int(len_ / 2)

    # slice the number to get each part
    part_1 = num_str[:half_len]
    part_2 = num_str[half_len:]

    # check if each half is the same
    if part_1 == part_2:
        return num
    else: 
        return 0


# apply check to a list and sum the numbers
def sum_list_with_pattern(lst):
    res = []
    for num in lst:
        res.append(check_pattern(num))

    return sum(res)
        


lst = split_string(string)
str_pairs = get_string_pairs(lst)
all_numbers_list = generate_between_pairs(str_pairs)
all_numbers = combine_lists_into_single(all_numbers_list)
answer = sum_list_with_pattern(all_numbers)
print(answer)









