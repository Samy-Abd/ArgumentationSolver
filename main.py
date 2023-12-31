# Authors:
# Aghiles Samy AOUABED
# Abdelghani Yanis BOUCHELAGHEM

from classes.ArgumentationFramework import ArgumentationFramework
from utils.parser import parse_arguments

parsed_args = parse_arguments()
argumentationFramework = ArgumentationFramework(file_path=parsed_args.FILE)

p = str(parsed_args.XX_YY).split('_')

isTrue = False

if p[1] == 'CO':
    complete_extensions = argumentationFramework.find_all_complete_extensions()
    print("Complete extensions found : ", complete_extensions)
    if p[0] == 'VE':
        given_arguments = tuple(parsed_args.ARGUMENTS)
        isTrue = given_arguments in complete_extensions
    elif p[0] == 'DC':
        given_arguments = parsed_args.ARGUMENTS
        credulous_arguments = argumentationFramework.find_credulous_arguments(complete_extensions)
        print("Credulous arguments found : ", credulous_arguments)
        isTrue = parsed_args.ARGUMENTS in credulous_arguments
    elif p[0] == 'DS':
        given_arguments = parsed_args.ARGUMENTS
        skeptical_arguments = argumentationFramework.find_skeptical_arguments(complete_extensions)
        print("Skeptical arguments found : ", skeptical_arguments)
        isTrue = parsed_args.ARGUMENTS in skeptical_arguments
elif p[1] == 'ST':
    stable_extensions = argumentationFramework.find_all_stable_extensions()
    print("Stable extensions found : ", stable_extensions)
    if p[0] == 'VE':
        given_arguments = tuple(parsed_args.ARGUMENTS)
        isTrue = given_arguments in stable_extensions
    elif p[0] == 'DC':
        given_arguments = parsed_args.ARGUMENTS
        credulous_arguments = argumentationFramework.find_credulous_arguments(stable_extensions)
        print("Credulous arguments found : ", credulous_arguments)
        isTrue = parsed_args.ARGUMENTS in credulous_arguments
    elif p[0] == 'DS':
        given_arguments = parsed_args.ARGUMENTS
        skeptical_arguments = argumentationFramework.find_skeptical_arguments(stable_extensions)
        print("Skeptical arguments found : ", skeptical_arguments)
        isTrue = parsed_args.ARGUMENTS in skeptical_arguments

if isTrue:
    print("YES")
else:
    print("NO")

############ The logic ############
### Calculating the complete extensions : ###
# Generate all possible argument combination
# for every argument combination :
# -conflict free

# -S completely defends itself
# Find all attackers of any argument of S:
# 	Are they all attacked by at least one member of S ?
# 		if yes, then check the other conditions, if no, it is not complete, move on.

# -S does not completely defend an outsider
# For every argument outside of S :
# 	Get all the attackers of that argument:
# 		If they are all atacked by S :
# 			Then it is not complete

# If all of the above conditions have been met, then S is complete.
			


#### Calculating the stable extensions : ###

# for every complete extension :
# 	For every argument outside of the extension:
# 		is it attacked by at least one member of S ?
# 			if not, then it is not a stable extension
	

