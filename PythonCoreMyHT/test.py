def progress_day(days):
    result = 0
    for i in range(1, len(days)):
        if days[i] > days[i-1]:
            result += 1
    return result
 

print(progress_day([1, 3, 2, 6, 10, 12, 4]))
