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

    def _find_attackers_of_argument(self, argument: str) -> set:
        attackers = set()
        for attack in self.attacks:
            if attack[1] == argument:
                attackers.update(attack[0]) # Attacker found
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
    
    def _get_compliment_of_argument_combination(self, argument_combination : set) -> set:
        return self.arguments.difference(argument_combination)
    
    def _does_argument_combination_completely_defend_outsider(self, argument_combination : set) -> bool:
        outside_arguments = self._get_compliment_of_argument_combination(argument_combination)
        for outside_argument in outside_arguments:
            outside_argument_attackers = self._find_attackers_of_argument(outside_argument)
            if self._is_combination_attacked_by_combination(input_combination=outside_argument_attackers,
                                                            attacking_combination=argument_combination):
                return True
        return False
    
    def _does_argument_combination_completely_defend_itself(self, argument_combination : set) -> bool:
        #argument_combination is the extension we consider
        attackers_of_combination = self._find_attackers_of_argument_combination(argument_combination)
	    #Are they all attacked by at least one member of S ?
        if not self._is_combination_attacked_by_combination(input_combination=attackers_of_combination,
                                                            attacking_combination=argument_combination):
            return False
		#if yes, then pass, otherwise it is not complete
        return True

    ########### Public ############

    def find_all_complete_extensions(self) -> list:
        complete_extensions = list()
        all_argument_combinations = self._generate_all_possible_argument_combinations()
        for argument_combination in all_argument_combinations:
            if not self._is_argument_combination_conflict_free(argument_combination):
                continue
            if not self._does_argument_combination_completely_defend_itself(argument_combination):
                continue
            if self._does_argument_combination_completely_defend_outsider(argument_combination):
                continue
            complete_extensions.append(argument_combination)

        return complete_extensions

    def is_argument_combination_a_stable_extension(self, argument_combination : set) -> bool:
        if not self._is_argument_combination_conflict_free(argument_combination):
            return False
        arguments_outside_of_combination = self._get_compliment_of_argument_combination(argument_combination)
        return self._is_combination_attacked_by_combination(input_combination=arguments_outside_of_combination,
                                                            attacking_combination=argument_combination)

    def find_all_stable_extensions(self) -> list:
        stable_extensions = list()
        all_argument_combinations = self._generate_all_possible_argument_combinations()
        for argument_combination in all_argument_combinations:
            if self.is_argument_combination_a_stable_extension(argument_combination):
                stable_extensions.append(argument_combination)
        return stable_extensions

    def find_credulous_arguments(self, extensions : list) -> set:
        return set().union(*extensions)

    def find_skeptical_arguments(self, extensions : list) -> set:
        return set().intersection(*extensions)