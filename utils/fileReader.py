import re

def read_arguments_and_attacks(file_path : str):
    arguments = set()
    attacks = set()

    with open(file_path, 'r') as file:
        for line in file:
            # Extract arguments
            arg_match = re.match(r'arg\((\w+)\)\.', line)
            if arg_match:
                arguments.add(arg_match.group(1))

            # Extract attacks
            attack_match = re.match(r'att\((\w+),(\w+)\)\.', line)
            if attack_match:
                attacks.add((attack_match.group(1), attack_match.group(2)))

    return arguments, attacks