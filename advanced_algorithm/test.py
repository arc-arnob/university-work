import unittest
import branch_and_bound_1
from mip import *


class Sign(Enum):
    Smaller = 1
    Equals = 2
    Greater = 3


class Mode(Enum):
    Minimization = 1
    Maximization = 2


class TestSolution(unittest.TestCase):

    def run_test_from_file(self, model_sense, file_name, expected_objective_value, epsilon=0.0001):
        m = Model(sense=model_sense)
        m.verbose = 0
        m.read(file_name)

        original = m.copy()  # make copy to check solution

        x = branch_and_bound_1.Solution(
            branch_and_bound_1.ProblemType.MINIMIZATION if m.sense == "MIN" else branch_and_bound_1.ProblemType.MAXIMIZATION,
            branch_and_bound_1.VariableSelectionStrategy.LECTURE)

        (best_found, global_bound) = x.branch_and_bound(m)

        self.assertAlmostEqual(expected_objective_value, global_bound, places=4)

        if global_bound != float("inf") and global_bound != float("-inf"):
            for index, var in enumerate(best_found):
                original += original.vars[index] == var
                self.assertTrue(abs(best_found[index] - round(best_found[index])) < epsilon)
            status = original.optimize()

            self.assertEqual(status, OptimizationStatus.OPTIMAL)
            self.assertAlmostEqual(expected_objective_value, original.objective_value, places=4)

    # TEST CASES

    def test_matrix(self):
        self.run_test_from_file(MAXIMIZE, "random.mps", 70)

    def test_knapsack(self):
        self.run_test_from_file(MAXIMIZE, "knapsack_students.mps.gz", 23376)

    def test_g503inf(self):
        self.run_test_from_file(MINIMIZE, "g503inf.mps.gz", float("inf"))


if __name__ == '__main__':
    unittest.main()