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
        # Solve Main LP Relaxed Problem
        solved_eqn = m.optimize(relax=True)
        # TODO: Make it usable for Minimization as well
        optimal_solution = m.objective_value
        lower_bound = float("-inf")
        upper_bound = int(m.objective_value)
        most_optimal_node_and_z = None

        current_node = [(m, lower_bound, upper_bound)]
        while current_node:
            # Get the Node to be solved
            node, lower_bound, upper_bound = current_node.pop()

            # optimize the the equation
            node.optimize(relax=True)

            if (node.status == OptimizationStatus.NO_SOLUTION_FOUND):
                # TODO: Fix for Minimization
                most_optimal_node_and_z = ([], float("inf"))
                return most_optimal_node_and_z

            # Prune due to Infeasibility
            if (node.status == OptimizationStatus.INFEASIBLE):
                continue

            if (node.status == OptimizationStatus.OPTIMAL):
                current_solution = node.objective_value

                # Prune due to Bound
                if (int(current_solution) <= lower_bound):
                    continue

                # Check and update Lower Bound
                # If optimal value is Integer, then lower bound of max solution gives lower bound
                if (float(current_solution) == int(current_solution)):
                    lower_bound = int(current_solution)
                    most_optimal_node_and_z = ([var.x for var in m.vars], lower_bound)
                    continue  # Prune by optimality

            new_constraint_on_this_var = self.variable_selection_method_lecture(node.vars)

            # Check: Branch the variable that is yet not Integer
            # Fix on how to decide on upper and lower bound

            lhs_branch = node.copy()  # copy all existing constraints
            lhs_branch += new_constraint_on_this_var <= int(new_constraint_on_this_var.x)  # Add a new Constraint
            current_node.append((lhs_branch, lower_bound, upper_bound))  # append as tuple

            rhs_branch = node.copy()
            rhs_branch += new_constraint_on_this_var >= int(new_constraint_on_this_var.x) + 1
            current_node.append((lhs_branch, lower_bound, upper_bound))

        return most_optimal_node_and_z

    def variable_selection_method_lecture(self, variables: List[mip.Var]) -> mip.Var:
        # Chooses the variable that has its fractional part closest to 0.5
        return self.choose_variable_closest_to_half(variables)

    def choose_variable_closest_to_half(self, variables):
        closest_variable = None
        closest_difference = float('inf')
        for var in variables:
            if (var.x is None):
                print(var, var.x is not None)
                continue
            fractional_part = abs(var.x - round(var.x))
            difference = abs(fractional_part - 0.5)

            if difference < closest_difference:
                closest_difference = difference
                closest_variable = var
        return closest_variable

    def variable_selection_method_self(self, variables: List[mip.Var]) -> mip.Var:
        pass