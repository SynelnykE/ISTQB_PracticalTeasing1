#that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.

list_with_str_int = [123, 546, 54.6]

def filter_list(list_with_str_int):
    output_list = []
    for i in list_with_str_int:
        if type(i) == int:
            output_list.append(i)
    return output_list

print(filter_list(list_with_str_int)) 
