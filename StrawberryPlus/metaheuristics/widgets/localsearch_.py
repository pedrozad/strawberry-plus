import sys
from jmetal import problem
import numpy

import Orange.data
from Orange.widgets import widget, gui
from Orange.widgets.widget import Input, Output
from Orange.widgets.settings import Setting
from AnyQt.QtGui import QIntValidator
#from Orange.widgets.utils.signals import Input, Output

# from JMetalpy
from jmetal.algorithm.singleobjective.local_search import LocalSearch
from jmetal.operator import BitFlipMutation
from jmetal.operator import PolynomialMutation
from jmetal.problem import OneMax
from jmetal.util.solution import print_function_values_to_file, print_variables_to_file
from jmetal.util.termination_criterion import StoppingByEvaluations
from jmetal.core.problem import Problem, BinaryProblem

class LocalSearch_widget(widget.OWWidget):
    name = "Local Search"
    description = "Local Search, expects a problem (Single Objective) and an Integer (Max Evaluation)"
    icon = "icons/local-search.svg"
    priority = 10

    #problem = OneMax(number_of_bits=0)
    max_evaluations = int()
    problem = None
    
    class Inputs:
        problem = Input("Problem Unconstrained (Single Objective)", Problem )

    class Outputs:
        solution = Output("Solution", str)
        computing_time = Output("Computing Time", str)
        fitness = Output("Fitness", str)

    want_main_area = False
    max_evaluations = Setting(100)

    def __init__(self):
        super().__init__()
        self.problem = None

        self.setFixedHeight(240)
        self.label1 = gui.widgetLabel(self.controlArea, "Please attach a Problem to the Input")

        gui.lineEdit(self.controlArea, self, "max_evaluations", "Enter the Max Evaluations quantity",
            box="Max Evaluations Quantity",
            callback=None,
            valueType=int, validator=QIntValidator())
        

        # Box to click the botton
        self.optionsBox = gui.widgetBox(self.controlArea, "Options")
        self.b = gui.button(self.optionsBox, self, "Run", callback=self.run)
        self.b.setDisabled(True)

    @Inputs.problem
    def set_problem(self, problem):
        """Set the input number."""
        self.problem = problem
        if self.problem is not None:
            self.label1.setText('Problem: ' + self.problem.get_name())
            if self.problem is not None and self.max_evaluations is not None:
                self.b.setEnabled(True)
        else:
            self.label1.setText('Please attach a Problem to the Input')
            self.b.setDisabled(True)

    def run(self):
        if self.problem is not None and self.max_evaluations is not None:
            print('\nMax Evaluation: ' + str(self.max_evaluations))
            if isinstance(self.problem, BinaryProblem):
                algorithm = LocalSearch(
                    problem=self.problem,
                    mutation=BitFlipMutation(probability=1.0 / self.problem.number_of_bits),
                    termination_criterion=StoppingByEvaluations(max_evaluations=self.max_evaluations)
                )
                algorithm.run()
                self.Outputs.solution.send('Solution: ' + algorithm.get_result().get_binary_string())
                self.Outputs.computing_time.send('Computing time: ' + str(algorithm.total_computing_time))
                self.Outputs.fitness.send('Fitness:  ' + str(algorithm.get_result().objectives[0]))
            else:
                algorithm = LocalSearch(
                    problem=self.problem,
                    mutation=PolynomialMutation(1.0 / self.problem.number_of_variables, distribution_index=20.0),
                    termination_criterion=StoppingByEvaluations(max_evaluations=self.max_evaluations)
                )
                algorithm.run()
                self.Outputs.solution.send('Solution: ' + str(algorithm.get_result().variables))
                self.Outputs.computing_time.send('Computing time: ' + str(algorithm.total_computing_time))
                self.Outputs.fitness.send('Fitness:  ' + str(algorithm.get_result().objectives[0]))
        else:
            self.Outputs.solution.send(None)
            self.Outputs.computing_time.send(None)
            self.Outputs.fitness.send(None)

# if __name__ == '__main__':
#     problem = OneMax(number_of_bits=16)

#     max_evaluations = 100
#     algorithm = LocalSearch(
#         problem=problem,
#         mutation=BitFlipMutation(probability=1.0 / problem.number_of_bits),
#         termination_criterion=StoppingByEvaluations(max_evaluations=max_evaluations)
#     )

#     algorithm.run()
#     result = algorithm.get_result()

    # # Save results to file
    # print_function_values_to_file(result, 'FUN.'+ algorithm.get_name() + "." + problem.get_name())
    # print_variables_to_file(result, 'VAR.' + algorithm.get_name() + "." + problem.get_name())

    # print('Algorithm: ' + algorithm.get_name())
    # print('Problem: ' + problem.get_name())
    # print('Solution: ' + result.get_binary_string())
    # print('Fitness:  ' + str(result.objectives[0]))
    # print('Computing time: ' + str(algorithm.total_computing_time))