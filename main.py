from classes.board import Graph
from utils.parser import parse_arguments

parsed_args = parse_arguments()
graph = Graph(file_path=parsed_args.FILE)

p = str(parsed_args.XX_YY).split('_')
if p[0] == 'VE':
    if p[1] == 'CO':
        complete_extensions = graph.find_all_complete_extensions()
        given_arguments = tuple(parsed_args.ARGUMENTS)
        if given_arguments in complete_extensions:
            print("YES") 
        else:
            print("NO")
    elif p[1] == 'ST':
        stable_extensions = graph.find_all_stable_extensions()
        given_arguments = tuple(parsed_args.ARGUMENTS)
        if given_arguments in stable_extensions:
            print("YES") 
        else:
            print("NO") 
if p[0] == 'DC':
    if p[1] == 'CO':
        complete_extensions = graph.find_all_complete_extensions()
        credulous_arguments = graph.find_credulous_arguments(complete_extensions)
        if parsed_args.ARGUMENTS in credulous_arguments:
            print("YES")
        else:
            print("NO")
    elif p[1] == 'ST':
        stable_extensions = graph.find_all_stable_extensions()
        credulous_arguments = graph.find_credulous_arguments(stable_extensions)
        if parsed_args.ARGUMENTS in credulous_arguments:
            print("YES")
        else:
            print("NO")
if p[0] == 'DS':
    if p[1] == 'CO':
        complete_extensions = graph.find_all_complete_extensions()
        skeptical_arguments = graph.find_skeptical_arguments(complete_extensions)
        if parsed_args.ARGUMENTS in skeptical_arguments:
            print("YES")
        else:
            print("NO") 
    elif p[1] == 'ST':
        stable_extensions = graph.find_all_stable_extensions()
        skeptical_arguments = graph.find_skeptical_arguments(stable_extensions)
        if parsed_args.ARGUMENTS in skeptical_arguments:
            print("YES")
        else:
            print("NO") 

####### The logic ############
# Calculate the complete extensions :
# Generate all possible argument combination
# for every argument combination :
# -conflict free
# already have this



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
			


# Calculate the stable extensions :

# for every complete extension :
# 	For every argument outside of the extension:
# 		is it attacked by at least one member of S ?
# 			if not, then it is not a stable extension
	



# functions :
# isAttackedByAtLeastOneOf(argument, setOfArguments)