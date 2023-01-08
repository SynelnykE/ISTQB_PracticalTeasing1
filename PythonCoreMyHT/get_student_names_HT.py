# Create a function get_student_names() that takes a dictionary of student names and 
# returns a list of student names in alphabetical order.

def get_student_names(dict_names):
    lst_names = []
    for value in dict_names.values():
        lst_names.append(value)
    return sorted(lst_names)

print(get_student_names({"Student 1" : "Steve", "Student 2" : "Becky", "Student 3" : "John"}))
# ➞ ["Becky", "John", "Steve"]
