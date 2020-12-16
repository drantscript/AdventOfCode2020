# Advent of Code 2020 Day 14

import AOC

def array_to_string(array : []) -> str:
    return "".join([str(elem) for elem in array])

def bits_to_int(value : str) -> int:
    return int(value, 2)

def int_to_bits(value : int) -> str:
    return bin(value)[2:].zfill(36)

def apply_mask(mask : str, register : str) -> str:
    return "".join([(v if mask[i] == "X" else mask[i]) for i, v in enumerate(register)])

def apply_mask_v2(mask : str, register : str) -> str:
    return "".join([(v if mask[i] == "0" else mask[i]) for i, v in enumerate(register)])

def part_1():

    lines = AOC.get_input_lines(14, AOC.format_strip)

    full_memory = {}
    current_mask = int_to_bits(0)
    
    for line in lines:

        # Mask setter
        if "mask = " in line:
            current_mask = line.replace("mask = ","")

        # Memory setter
        if "mem" in line:
            mem_index = int(line.replace("mem" + "[","").partition("] = ")[0])
            mem_value = int(line.replace("mem" + "[","").partition("] = ")[2])
            full_memory[mem_index] = apply_mask(current_mask, int_to_bits(mem_value))

    total = 0
    for value in full_memory.keys():
        total += bits_to_int(full_memory[value])
    print("Total:", total)

    return

def part_2():

    lines = AOC.get_input_lines(14, AOC.format_strip)

    full_memory = {}
    current_mask = int_to_bits(0)
    
    for line in lines:

        # Mask setter
        if "mask = " in line:
            current_mask = line.replace("mask = ","")
            # print(current_mask)

        # Memory setter
        if "mem" in line:
            mem_index = int(line.replace("mem" + "[","").partition("] = ")[0])
            mem_value = int(line.replace("mem" + "[","").partition("] = ")[2])

            base_address = int_to_bits(mem_index)
            masked_address = apply_mask_v2(current_mask, base_address)
            # print(masked_address)

            addresses = []

            def generate_floating_addresses(from_address : str) -> []:
                if from_address.find("X") != -1:
                    new_0 = from_address.replace("X", "0", 1)
                    new_1 = from_address.replace("X", "1", 1)
                    generate_floating_addresses(new_0)
                    generate_floating_addresses(new_1)
                else:
                    addresses.append(from_address)

            generate_floating_addresses(masked_address)
            # print(addresses)
            
            for address in addresses:
                full_memory[address] = mem_value

    total = 0
    for value in full_memory.keys():
        total += full_memory[value]
    print("Total:", total)

    return

# Main
part_1()
part_2()
    