# Advent of Code 2020 Day 2

def count_letters(letter, in_string):
     
    count = 0
    for char in in_string:
        if char == letter:
            count += 1
            
    return count

def verify_password(pw):
    
    pos_one = int(pw["minmax"][0]) - 1
    pos_two = int(pw["minmax"][1]) - 1
    
    if(pos_one < 0 or pos_one >= len(pw["password"]) or pos_two < 0 or pos_two >= len(pw["password"])):
       return False
    
    one_valid = pw["letter"] == pw["password"][pos_one]
    two_valid = pw["letter"] == pw["password"][pos_two]
    
    return (one_valid or two_valid) and not (one_valid and two_valid)

def parse():
    
    file_name = "inputs/day2.txt"
    array = []
    file = open(file_name, "r")
    
    for line in file:
        array.append(line)
        
    file.close()
        
    passwords = []
    
    for entry in array:
        strings = entry.split()
        password = {}
        password["minmax"] = strings[0].split("-")
        password["letter"] = strings[1].strip(":")
        password["password"] = strings[2]
        passwords.append(password)
    
    valid_count = 0
    
    for pw in passwords:
        count = count_letters(pw["letter"], pw["password"])
        if(count >= int(pw["minmax"][0]) and count <= int(pw["minmax"][1])):
            valid_count += 1
        else:
            print(pw)
            
    print("Valid count:" , valid_count)
    
def parse_two():
    
    file_name = "inputs/day2.txt"
    array = []
    file = open(file_name, "r")
    
    for line in file:
        array.append(line)
        
    file.close()
        
    passwords = []
    
    for entry in array:
        strings = entry.split()
        password = {}
        password["minmax"] = strings[0].split("-")
        password["letter"] = strings[1].strip(":")
        password["password"] = strings[2]
        passwords.append(password)
        
    valid_count = 0
        
    for pw in passwords:
        if(verify_password(pw)):
            valid_count += 1
            
    print("Valid count:" , valid_count)
        

if __name__ == "__main__":
    print ("Day2")
    parse()
    parse_two()