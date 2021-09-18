import sys
import numpy

import Orange.data
from Orange.widgets import widget, gui
from Orange.widgets.widget import Input, Output
#from Orange.widgets.utils.signals import Input, Output


# from JMetalpy
from jmetal.algorithm.singleobjective.simulated_annealing import SimulatedAnnealing
from jmetal.operator import BitFlipMutation
from jmetal.problem import OneMax
from jmetal.util.solution import print_function_values_to_file, print_variables_to_file
from jmetal.util.termination_criterion import StoppingByEvaluations



class OWSA_OneMax(widget.OWWidget):
    name = "Simulated Annealing - One Max"
    description = "Randomly selects a subset of instances from the data set"
    icon = "icons/mywidget.svg"
    priority = 10

    class Inputs:
        number_of_bits = Input("number_of_bits", int)
        max_evaluations = Input("max_evaluations", int)

    class Outputs:
        solution = Output("Solution", str)
        computing_time = Output("Computing Time", str)
        fitness = Output("Fitness", str)

   

    want_main_area = False

    def __init__(self):
        super().__init__()
        self.number_of_bits = None
        self.max_evaluations =  None

        #self.label = gui.widgetLabel(self.controlArea, "The number is: ??")

        # Box to click the botton
        self.optionsBox = gui.widgetBox(self.controlArea, "Options")
        gui.button(self.optionsBox, self, "Run", callback=self.run)

    @Inputs.number_of_bits
    def set_number_of_bits(self, number_of_bits):
        """Set the input number."""
        self.number_of_bits = number_of_bits

    @Inputs.max_evaluations
    def set_max_evaluations(self,ev):
        """Set the input of B"""
        self.max_evaluations = ev

    # def handleNewSignals(self):
        

    def run(self):
        if self.max_evaluations is not None and self.number_of_bits is not None:
            problem = OneMax(number_of_bits=self.number_of_bits)
            algorithm = SimulatedAnnealing(
                problem=problem,
                mutation=BitFlipMutation(probability=1.0 / problem.number_of_bits),
                termination_criterion=StoppingByEvaluations(max_evaluations=self.max_evaluations)
            )
            print("\n**************\n Ya declaré")
            algorithm.run()
            print("\n**************\n Ya Ejecuté")
            self.Outputs.solution.send('Solution: ' + algorithm.get_result().get_binary_string())
            self.Outputs.computing_time.send('Computing time: ' + str(algorithm.total_computing_time))
            self.Outputs.fitness.send('Fitness:  ' + str(algorithm.get_result().objectives[0]))
        else:
            self.Outputs.solution.send(None)
            self.Outputs.computing_time.send(None)
            self.Outputs.fitness.send(None)