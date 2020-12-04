# Advent of Code 2020 Day 4

import AOC

lines = AOC.get_input_lines(4, AOC.format_strip)

required_keys = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
ignored_key = "cid"
end_passport = ""

valid_passports = 0
passports = []

# generate passports
passport_entries = []
for line in lines:

    if(line == end_passport):
        passports.append(passport_entries[:])
        passport_entries.clear()
    else:
        chunks = line.split()
        for chunk in chunks:
            passport_entries.append(chunk)

passports.append(passport_entries)

# parse passports
for passport in passports:

    passport_keys = []
    key_values = {}
    for entry in passport:
        pair = entry.split(":")
        passport_keys.append(pair[0])
        key_values[pair[0]] = pair[1]

    valid = True
    valid_hcl_chars = "0123456789abcdef"
    valid_ecl_strings = ["amb","blu","brn","gry","grn","hzl","oth"]
    valid_pid_chars = "0123456789"

    for key in required_keys:
        if key not in passport_keys:
            valid = False
            print("Invalid key:", key, "in" , passport)
        elif key == "byr":
            value = int(key_values[key])
            if(value < 1920 or value > 2002):
                valid = False
                print("Invalid byr:", value, "in" , passport)
        elif key == "iyr":
            value = int(key_values[key])
            if(value < 2010 or value > 2020):
                valid = False
                print("Invalid iyr:",value, "in" , passport)
        elif key == "eyr":
            value = int(key_values[key])
            if(value < 2020 or value > 2030):
                valid = False
                print("Invalid eyr:", value, "in" , passport)
        elif key == "hgt":
            value = key_values[key]
            if("cm" in value):
                sub = int(value.replace("cm", ""))
                if(sub < 150 or sub > 193):
                    valid = False
                    print("Invalid hgt:", value, "in" , passport)
            elif("in" in value):
                sub = int(value.replace("in", ""))
                if(sub < 59 or sub > 76):
                    valid = False
                    print("Invalid hgt:", value, "in" , passport)
            else:
                valid = False
                print("Invalid hgt:", value, "in" , passport)
        elif key == "hcl":
            value = key_values[key]
            if(value[0] == "#"):
                sub = value.replace("#", "")
                if(len(sub) == 6):
                    for c in sub:
                        if(c not in valid_hcl_chars):
                            valid = False
                            print("Invalid hcl:", value, "in" , passport)
                else:
                    valid = False
                    print("Invalid hcl:", value, "in" , passport)
            else:
                valid = False
                print("Invalid hcl:", value, "in" , passport)
        elif key == "ecl":
            value = key_values[key]
            if(value not in valid_ecl_strings):
                valid = False
                print("Invalid ecl:", value, "in" , passport)
        elif key == "pid":
            value = key_values[key]
            print("pid:" , value)
            if(len(value) == 9):
                for c in value:
                    if(c not in valid_pid_chars):
                        valid = False
                        print("Invalid pid:", value, "in" , passport)
            else:
                valid = False
                print("Invalid pid:", value, "in" , passport)

        if(valid == False):
            break

    if(valid == True):  
        valid_passports += 1

print("Valid passports:" , valid_passports)