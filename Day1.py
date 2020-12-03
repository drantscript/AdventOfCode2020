# Advent of Code 2020 Day 1

def two_value_sum():
    
    file_name = "inputs/day1.txt"
    array = []
    file = open(file_name, "r")
    
    for line in file:
        array.append(int(line))
        
    array.sort()
    
    lesser = 0
    greater = len(array) - 1
    
    while(True):
        combined = array[lesser] + array[greater]
        if(combined > 2020):
            greater -= 1
        elif(combined < 2020):
            lesser += 1
        else:
            break
        
    final_multiply = array[lesser] * array[greater]
    print("Two value sum:" , final_multiply)

def three_value_sum_the_stupid_way():

    file_name = "inputs/day1.txt"
    array = []
    file = open(file_name, "r")
    
    for line in file:
        array.append(int(line))

    file.close()
        
    array.sort()
    
    for a in range(0, len(array) - 3):
        for b in range(1, len(array) - 2):
            for c in range(2, len(array) - 1):
                if(array[a] + array[b] + array[c] == 2020):
                    final_multiply = array[a] * array[b] * array[c]
                    print("Three value sum:", final_multiply)
                    return

print("Day1")
two_value_sum()
three_value_sum_the_stupid_way()
