#Calculates average of digit in number

number = int(input("Enter number: "))

def mean(number):           
    sum = 0
    counter = 0
    for i in str(number):
        sum += int(i) 
        # counter += 1
    average = sum // counter
    
    return average

print(mean(number))
