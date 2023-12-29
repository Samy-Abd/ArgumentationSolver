from utils.parser import parse_arguments

parsed_args = parse_arguments()
# print("Parsed arguments:")
# print(f"-p: {parsed_args.XX_YY}")
# print(f"-f: {parsed_args.FILE}")
# print(f"-a: {parsed_args.ARGUMENTS}")
p = str(parsed_args.XX_YY).split('_')
if p[0] == 'VE':
    if p[1] == 'CO':
        argument, attack = read_arguments_and_attacks(parsed_args.FILE)
        print(verify_extension_complete(argument, attack, parsed_args.ARGUMENTS))
    elif p[1] == 'ST':
        argument, attack = read_arguments_and_attacks(parsed_args.FILE)
        print(verify_extension_stable(argument, attack, parsed_args.ARGUMENTS))
if p[0] == 'DC':
    if p[1] == 'CO':
        argument, attack = read_arguments_and_attacks(parsed_args.FILE)
        comp_arg = compute_complete_extension(argument, attack)
        print(decide_credulous_complete(argument, attack, comp_arg, parsed_args.ARGUMENTS))
    elif p[1] == 'ST':
        argument, attack = read_arguments_and_attacks(parsed_args.FILE)
        st_arg = compute_stable_extension(argument, attack)
        print(decide_credulous_stable(argument, attack, st_arg, parsed_args.ARGUMENTS))
if p[0] == 'DS':
    if p[1] == 'CO':
        argument, attack = read_arguments_and_attacks(parsed_args.FILE)
        comp_arg = compute_complete_extension(argument, attack)
        print(decide_skeptical_complete(argument, attack, comp_arg, parsed_args.ARGUMENTS))
    elif p[1] == 'ST':
        argument, attack = read_arguments_and_attacks(parsed_args.FILE)
        st_arg = compute_stable_extension(argument, attack)
        print(decide_skeptical_stable(argument, attack, st_arg, parsed_args.ARGUMENTS))