import sys
import numpy

import Orange.data
from Orange.widgets import widget, gui
from Orange.widgets.widget import Input, Output
from Orange.widgets.settings import Setting
from AnyQt.QtGui import QIntValidator


# from JMetalpy
from jmetal.algorithm.singleobjective.simulated_annealing import SimulatedAnnealing
from jmetal.operator import BitFlipMutation
from jmetal.operator import PolynomialMutation
from jmetal.problem import OneMax
from jmetal.util.solution import print_function_values_to_file, print_variables_to_file
from jmetal.util.termination_criterion import StoppingByEvaluations
from jmetal.core.problem import Problem, BinaryProblem


class SimulatedAnneling(widget.OWWidget):
    name = "Simulated Annealing_SA"
    description = "Simulated Annealing, expects a problem"
    icon = "icons/simulated-annealing.svg"
    priority = 20

    problem = OneMax(number_of_bits=0)
    max_evaluations = int()
    problem = None
   
    class Inputs:
        problem = Input("Problem Unconstrained", Problem )

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
                algorithm = SimulatedAnnealing(
                    problem=self.problem,
                    mutation=BitFlipMutation(probability=1.0 / self.problem.number_of_bits),
                    termination_criterion=StoppingByEvaluations(max_evaluations=self.max_evaluations)
                )
                algorithm.run()
                self.Outputs.solution.send('Solution: ' + algorithm.get_result().get_binary_string())
                self.Outputs.computing_time.send('Computing time: ' + str(algorithm.total_computing_time))
                self.Outputs.fitness.send('Fitness:  ' + str(algorithm.get_result().objectives[0]))
            else:
                algorithm = SimulatedAnnealing(
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
    
if __name__ == "__main__":
    from Orange.widgets.utils.widgetpreview import WidgetPreview
    from jmetal.problem.singleobjective.unconstrained import SubsetSum

   
    list_numbers = [2902, 5235, 357, 6058, 4846, 8280, 1295, 181, 3264,
        7285, 8806, 2344, 9203, 6806, 1511, 2172, 843, 4697,
        3348, 1866, 5800, 4094, 2751, 64, 7181, 9167, 5579,
        9461, 3393, 4602, 1796, 8174, 1691, 8854, 5902, 4864,
        # 5488, 1129, 1111, 7597, 5406, 2134, 7280, 6465, 4084,
        # 8564, 2593, 9954, 4731, 1347, 8984, 5057, 3429, 7635,
        # 1323, 1146, 5192, 6547, 343, 7584, 3765, 8660, 9318,
        # 5098, 5185, 9253, 4495, 892, 5080, 5297, 9275, 7515,
        # 9729, 6200, 2138, 5480, 860, 8295, 8327, 9629, 4212,
        # 3087, 5276, 9250, 1835, 9241, 1790, 1947, 8146, 8328,
        # 973, 1255, 9733, 4314, 6912, 8007, 8911, 6802, 5102,
        5451, 1026, 8029, 6628, 8121, 5509, 3603, 6094, 4447,
        683, 6996, 3304, 3130, 2314, 7788, 8689, 3253, 5920,
        3660, 2489, 8153, 2822, 6132, 7684, 3032, 9949, 59,
        6669, 6334]
    WidgetPreview(SimulatedAnneling).run(
        set_problem=SubsetSum(100000,list_numbers),
        set_max_evaluations=100
    )
    