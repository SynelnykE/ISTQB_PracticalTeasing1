#that returns the probability of choosing a number greater than or equal to n from the list

def probability(numbers_list, number):
    favour = 0
    for i in numbers_list:
        if i >= number:
            favour += 1
    return (round(((favour / len(numbers_list))*100), 1))

print(probability([1, 2, 3, 4, 5, 6, 7, 8], 5))
