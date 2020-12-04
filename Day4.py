# Advent of Code 2020 Day 4

import AOC

def check_passports():

    lines = AOC.get_input_lines(4, AOC.format_strip)

    # generate passports
    passports = []
    passport_entries = []
    for line in lines:

        if(line == ""):
            passports.append(passport_entries[:])
            passport_entries.clear()
        else:
            chunks = line.split()
            for chunk in chunks:
                passport_entries.append(chunk)

    passports.append(passport_entries)

    # generate passport requirements
    def in_range(value : str, min : int, max : int):
        return int(value) >= min and int(value) <= max

    def pass_hgt(value : str):
        if("cm" in value):
            return in_range(value.replace("cm", ""), 150, 193)
        elif("in" in value):
            return in_range(value.replace("in", ""), 59, 76)
        return False

    def pass_hcl(value : str):
        if(value[0] == "#"):
            if(len(sub := value.replace("#", "")) == 6):
                for c in sub:
                    if(c not in "0123456789abcdef"):
                        return False
                return True
        return False

    def pass_pid(value :str):
        if(len(value) == 9):
            for c in value:
                if c not in "0123456789":
                    return False
            return True
        return False

    # map keys to requirement conditions
    requirements = {}
    requirements["byr"] = lambda val : in_range(val, 1920, 2002)
    requirements["iyr"] = lambda val : in_range(val, 2010, 2020)
    requirements["eyr"] = lambda val : in_range(val, 2020, 2030)
    requirements["hgt"] = pass_hgt
    requirements["hcl"] = pass_hcl
    requirements["ecl"] = lambda val : val in ["amb","blu","brn","gry","grn","hzl","oth"]
    requirements["pid"] = pass_pid

    # validate passports
    valid_passports = 0
    for passport in passports:

        valid = True

        # convert entries to key-value pairs
        pairs = {}
        for entry in passport:
            pair = entry.split(":")
            pairs[pair[0]] = pair[1]

        # check requirements
        for key in requirements.keys():
            if(not (valid := requirements[key](pairs[key]) if key in pairs.keys() else False)):
                break

        if(valid == True):  
            valid_passports += 1

    return valid_passports

#end check_passports()

print("Valid passports:" , check_passports())