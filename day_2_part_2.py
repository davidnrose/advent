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
            nums.append(start)
            start += 1
        all_nums.append(nums)

    return all_nums

# add all the lists together into a single big list
def combine_lists_into_single(lst):
    new_list = []
    for l in lst:
        new_list = new_list + l

    return new_list


# drop numbers which are only 1 digit in length - this is catching me out as my checking is allowing these through as "invalid" ids
def drop_single_digit(lst):
    return [id for id in lst if len(str(id)) != 1]



# return the number of ways that there are to divide up the ID with no remainder
def get_factors_of_length(id): 

    id_str = str(id)
    len_id = len(id_str)

    factors = []
    for i in range(len_id):
        if i not in [0, 1]:
            if len_id % i == 0:
                factors.append(i)

    factors.append(len_id)            

    return factors


# split the if up by the factor and return the slices
def slice_id(num, fac=5): 

    # force id to string
    id_str = str(num)

    # get the total length
    id_len = len(id_str)

    # get the length of each slice
    id_slice_len = int(id_len / fac)

    # slice up the id and increment
    slices = []
    start_idx = 0
    for i in range(fac):
        slice = id_str[start_idx:start_idx+id_slice_len]
        slices.append(slice)
        start_idx += id_slice_len

    return slices




# ccheck if a number follows the pattern
def check_pattern(num):

    # first get the factors for the id
    factors = get_factors_of_length(num)

    # iterate through the factors, creating the slices, and checking equality
    for fac in factors: 
        # slice the id 
        slices = slice_id(num, fac)
        # create a set - if len == 1 then the value is repeated
        if len(set(slices)) == 1: 
            return num

    return 0
    


# apply check to a list and sum the numbers
def sum_list_with_pattern(lst):
    return sum([check_pattern(id) for id in lst])
        

# this is all data prep to create a single list
lst = split_string(string)
str_pairs = get_string_pairs(lst)
all_numbers_list = generate_between_pairs(str_pairs)
all_numbers = combine_lists_into_single(all_numbers_list)
all_numbers = drop_single_digit(all_numbers) 


# this is chekcing numbers individually
answer = sum_list_with_pattern(all_numbers)
print(answer)

