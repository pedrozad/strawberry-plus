import sys
import numpy

import Orange.data
from Orange.widgets import widget, gui
from Orange.widgets.widget import Input, Output
#from Orange.widgets.utils.signals import Input, Output


# from JMetalpy
from jmetal.problem.singleobjective.unconstrained import Rastrigin


class Rastrigin_SingleObjetive(widget.OWWidget):
    name = "Rastrigin - Single-Objective - Problem"
    description = "Rastrigin test function optimization"
    icon = "icons/rastrigin.svg"
    priority = 40

    class Inputs:
        number_of_variables = Input("number_of_variables", int)

    class Outputs:
        problem = Output("Problem",  Rastrigin)
   

    want_main_area = False

    def __init__(self):
        super().__init__()
        self.number_of_variables = None

        # Problem
        self.problem = None

        self.setFixedHeight(150)

        self.optionsBox = gui.label(self.controlArea, self, "Rastrigin Problem")
        
        self.label = gui.widgetLabel(self.controlArea, "The number of Variables is: ??")
        # Box to click the botton
        # from AnyQt.QtGui import QIntValidator
        # gui.lineEdit(self.controlArea, self, "One Max Problem", "Enter the number of bits",
        #             box="One Max Problem",
        #             callback=self.number_changed,
        #             valueType=int, validator=QIntValidator())
        # self.number_changed()

    @Inputs.number_of_variables
    def set_number_of_variables(self, number_of_variables):
        """Set the input number."""
        self.number_of_variables = number_of_variables

    def handleNewSignals(self):
        if self.number_of_variables is not None:
            print("\n\n*******\n Rastrigin sending problem")
            self.problem = Rastrigin(number_of_variables=self.number_of_variables)
            self.label.setText("The number of variables is %s" %self.number_of_variables)
        else:
            self.problem = None
        self.Outputs.problem.send(self.problem)

