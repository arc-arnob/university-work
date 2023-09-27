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
    problem_type = None
    selection_strategy = None

    def __init__(self, problem_type: ProblemType, selection_strategy: VariableSelectionStrategy):
        self.problem_type = problem_type
        self.selection_strategy = selection_strategy

    def branch_and_bound(self, m: Model) -> Tuple[List[int], int]:
        optimal_solution = None
        # Global upper Bound for Min, and Global Lower Bound for Max
        global_bound = float("inf") if self.problem_type == ProblemType.MINIMIZATION else float("-inf")
        most_optimal_node_and_z = ([], global_bound)
        current_solution_b = None  # book current_solution
        current_node = [(m, None, global_bound)] if self.problem_type == ProblemType.MINIMIZATION else [
            (m, global_bound, None)]
        while current_node:
            # Get the Node to be solved
            node, lower_bound, upper_bound = current_node.pop()
            # optimize the the equation
            node.optimize(relax=True)

            if (node.status == OptimizationStatus.NO_SOLUTION_FOUND):
                return most_optimal_node_and_z

            if (node.status == OptimizationStatus.UNBOUNDED):
                continue

            # Prune due to Infeasibility
            if (node.status == OptimizationStatus.INFEASIBLE):
                continue

            if node.status == OptimizationStatus.OPTIMAL:
                current_solution = node.objective_value
                if (self.problem_type == ProblemType.MAXIMIZATION):
                    rounded_objective_value = math.floor(current_solution)
                else:
                    rounded_objective_value = math.ceil(current_solution)

                # Local lower bound for Minimization and Local Upper Bound for Maximization
                local_bound = rounded_objective_value

                is_all_vars_integer = self.is_all_intergers(node)
                update_bound = current_solution < global_bound if self.problem_type == ProblemType.MINIMIZATION \
                    else current_solution > global_bound
                if is_all_vars_integer:
                    if update_bound:
                        global_bound = node.objective_value
                        current_solution_b = [var.x for var in node.vars]
                        most_optimal_node_and_z = (current_solution_b, global_bound)
                    continue  # Prune by optimality
                elif self.problem_type == ProblemType.MINIMIZATION and local_bound >= global_bound:
                    continue  # Prune by bound
                elif self.problem_type == ProblemType.MAXIMIZATION and local_bound <= global_bound:
                    continue  # Prune by bound

                else:
                    new_constraint_on_this_var = self.variable_selection_method_lecture(node.vars)

                    lhs_branch = node.copy()  # Copy all existing constraints
                    lhs_branch += new_constraint_on_this_var <= math.floor(
                        new_constraint_on_this_var.x)  # Add a new Constraint
                    current_node.append((lhs_branch, lower_bound, upper_bound))  # append as tuple

                    rhs_branch = node.copy()
                    rhs_branch += new_constraint_on_this_var >= math.floor(new_constraint_on_this_var.x) + 1
                    current_node.append((rhs_branch, lower_bound, upper_bound))

        return most_optimal_node_and_z

    def variable_selection_method_lecture(self, variables: List[mip.Var]) -> mip.Var:
        # Chooses the variable that has its fractional part closest to 0.5
        return self.choose_variable_closest_to_half(variables)

    def is_all_intergers(self, m):
        for var in m.vars:
            if not var.x - round(var.x) < 1e-6:
                return False
        return True

    def choose_variable_closest_to_half(self, variables):
        closest_variable = None
        closest_difference = float('inf')
        for var in variables:
            fractional_part = var.x - int(var.x)
            difference = abs(0.5 - fractional_part)
            if difference < closest_difference:
                closest_difference = difference
                closest_variable = var
        return closest_variable

    def variable_selection_method_self(self, variables: List[mip.Var]) -> mip.Var:
        pass