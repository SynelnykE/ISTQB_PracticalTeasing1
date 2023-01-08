#that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.

list_with_str_int = input("Input soup from letters and numbers: ")

def filter_list(list_with_str_int):
    output_list = []
    for i in list_with_str_int:
        if i.isdigit():
            output_list.append(int(i))
    return output_list

print(filter_list(list_with_str_int)) 
