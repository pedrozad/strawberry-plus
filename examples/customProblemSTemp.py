import math
import random

from jmetal.core.problem import BinaryProblem, FloatProblem
from jmetal.core.solution import BinarySolution, FloatSolution

class CustomProblem(BinaryProblem):

    def __init__(self, number_of_bits: int = 256):
        super(CustomProblem, self).__init__()
        self.number_of_bits = number_of_bits
        self.number_of_objectives = 1
        self.number_of_variables = 1
        self.number_of_constraints = 0

        self.obj_directions = [self.MINIMIZE]
        self.obj_labels = ['Ones']

    def evaluate(self, solution: BinarySolution) -> BinarySolution:
        counter_of_ones = 0
        for bits in solution.variables[0]:
            if bits:
                counter_of_ones += 1

        solution.objectives[0] = -1.0 * counter_of_ones

        return solution

    def create_solution(self) -> BinarySolution:
        new_solution = BinarySolution(number_of_variables=1, number_of_objectives=1)
        new_solution.variables[0] = \
            [True if random.randint(0, 1) == 0 else False for _ in range(self.number_of_bits)]
        return new_solution

    def get_name(self) -> str:
        return 'CustomProblem'
#
# Don not modify above this line
#
out_problem = CustomProblem()
