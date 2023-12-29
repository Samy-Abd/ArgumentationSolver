from utils.fileReader import read_arguments_and_attacks
from utils.powerset import powerset

class Graph:
    def __init__(self, file_path: str) -> None:
        self.arguments, self.attacks = read_arguments_and_attacks(file_path)
    
    ########### private ###########
    def _generate_all_possible_argument_combinations(self) -> list:
        chain = powerset(self.arguments)
        return list(chain)
    
    def _is_argument_combination_conflict_free(self, argument_combination : set) -> bool:
        for argument1 in argument_combination:
            for argument2 in argument_combination:
                if (argument1, argument2) in self.attacks:
                    return False  # Conflict found
        return True

    def _find_attackers_of_argument(self, argument: str) -> tuple:
        attackers = tuple()
        for attack in self.attacks:
            if attack[1] == argument:
                attackers = attackers + (attack[0], ) # Attacker found
        return attackers
    
    def _find_attackers_of_argument_combination(self, argument_combination: set):
        attackers_of_combination = set()
        for argument in argument_combination:
            attackers_of_argument = self._find_attackers_of_argument(argument)
            attackers_of_combination.update(attackers_of_argument)
        return attackers_of_combination
    
    def _is_argument_attacked_by_combination(self, input_argument: str, argument_combination: set) -> bool:
        attackers_of_input_argument = self._find_attackers_of_argument(input_argument)
        for argument in argument_combination:
            if argument in attackers_of_input_argument:
                return True
        return False
            
    def _is_combination_attacked_by_combination(self, input_combination: set, attacking_combination : set) -> bool:
        """Does the attacking combination attack every argument of the input combination
        (one attacking argument from the attacking combination is enough)"""
        return all([self._is_argument_attacked_by_combination(input_argument, attacking_combination) for input_argument in input_combination])
    
    def _does_argument_combination_completely_defend_itself(self, argument_combination : set) -> bool:
        #Find all attackers of any argument of S:
        attackers_of_combination = self._find_attackers_of_argument_combination(argument_combination)
	    #Are they all attacked by at least one member of S ?
        if not self._is_combination_attacked_by_combination(attackers_of_combination, argument_combination):
            return False
		#if yes, then pass, otherwise it is not complete
        return True

    ########### Public ############


    def find_all_complete_extensions(self) -> list:
        complete_extensions = list()
        all_argument_combinations = self._generate_all_possible_argument_combinations()
        for argument_combination in all_argument_combinations:
            #Check if it is conflict free
            if not self._is_argument_combination_conflict_free(argument_combination):
                continue
            #Check if it completely defends itself
            if not self._does_argument_combination_completely_defend_itself(argument_combination):
                continue
            #Check if it does not completely defend an outside argument

            complete_extensions.append(argument_combination)

        return complete_extensions