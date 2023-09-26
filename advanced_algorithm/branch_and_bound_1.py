from mip import *
from enum import Enum, unique
import numpy as np
import math

from typing import List, Tuple


class ProblemType(Enum):
    MAXIMIZATION = 1
    MINIMIZATION = 2


class VariableSelectionStrategy(Enum):
    LECTURE = 1
    SELF = 2


class Solution:

    def __init__(self, problem_type: ProblemType, selection_strategy: VariableSelectionStrategy):
        pass

    def branch_and_bound(self, m: Model) -> Tuple[List[int], int]:
        # Solve First LP Problem
        # setup a new list of nodes to be traversed in BFS
        solved_eqn = m.optimize(relax=True)
        # TODO: Make it usable for Minimization as well
        optimal_solution = float("-inf")
        lower_bound = float("-inf")
        upper_bound = int(m.objective_value)
        # upper_bound = int(m.objective_value)
        # new_constraint_var = self.variable_selection_method_lecture(m.vars)

        # subproblem_1 = m.copy()
        # subproblem_1 += new_constraint_var <= int(new_constraint_var.x)

        # subproblem_2 = m.copy()
        # subproblem_2 += new_constraint_var >= int(new_constraint_var.x) + 1

        # TODO:
        # Pruning
        # Add Infeasibility Test Pruning
        # Add Pruning by optimality
        # Add pruning by

        current_node = [(m, lower_bound, upper_bound)]
        while current_node:
            node, lower_bound, upper_bound = current_node.pop()
            node.optimize(relax=True)

            if (node.status == OptimizationStatus.OPTIMAL):
                current_solution = node.objective_value
                if optimal_solution < current_solution:
                    optimal_solution = current_solution
                if (int(optimal_solution) > upper_bound):
                    upper_bound = int(optimal_solution)

            new_constraint_on_this_var = self.variable_selection_method_lecture(node.vars)

            # Check: Branch the variable that is yet not Integer

            lhs_branch = node.copy()  # copy all existing constraints
            lhs_branch += new_constraint_on_this_var <= int(new_constraint_on_this_var.x)  # Add a new Constraint
            current_node.append((lhs_branch, lower_bound, upper_bound))  # append as tuple

            rhs_branch = node.copy()
            rhs_branch += new_constraint_on_this_var >= int(new_constraint_on_this_var.x) + 1
            current_node.append((lhs_branch, lower_bound, upper_bound))

    def variable_selection_method_lecture(self, variables: List[mip.Var]) -> mip.Var:
        self.choose_variable_closest_to_half(variables)

    def choose_variable_closest_to_half(self, variables):
        closest_variable = None
        closest_difference = float('inf')
        for var in variables:
            fractional_part = abs(var.x - round(var.x))
            difference = abs(fractional_part - 0.5)

            if difference < closest_difference:
                closest_difference = difference
                closest_variable = var

        return closest_variable

    # def variable_selection_method_lecture_1by2(self, variables: List[mip.Var]) -> mip.Var:

    def variable_selection_method_self(self, variables: List[mip.Var]) -> mip.Var:
        pass