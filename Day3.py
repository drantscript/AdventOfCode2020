# Advent of Code 2020 Day 3

def is_tree(char):
    return char == "#"

def trees_for_slope(slope):
    
    file_name = "inputs/day3.txt"
    file = open(file_name, "r")
    rows = []
    
    for line in file:
        rows.append(line.strip())

    file.close()
    
    position = [0, 0]
    trees_hit = 0
    width = len(rows[0])
    #print(rows)
    
    position[0] += slope[0]
    position[1] += slope[1]
    position[0] = position[0] % width
    
    while(position[1] < len(rows)):
        
        #print(position)
        position_char = rows[position[1]][position[0]]
        
        if(is_tree(position_char)):
            trees_hit += 1
        
        position[0] += slope[0]
        position[1] += slope[1]
        position[0] = position[0] % width
            
    print("Trees hit:" , trees_hit)
    return trees_hit

def multi_tree():
    
    multiplied_total = trees_for_slope([1, 1])
    multiplied_total *= trees_for_slope([3, 1])
    multiplied_total *= trees_for_slope([5, 1])
    multiplied_total *= trees_for_slope([7, 1])
    multiplied_total *= trees_for_slope([1, 2])
    print("Multiplied trees:" , multiplied_total)

if __name__ == "__main__":
    print ("Day3")
    trees_for_slope([3,1])
    multi_tree()