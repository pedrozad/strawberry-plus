import sys
import numpy

import Orange.data
from Orange.widgets import widget, gui
from Orange.widgets.widget import Input, Output
#from Orange.widgets.utils.signals import Input, Output


# from JMetalpy
from jmetal.problem import Sphere


class Sphere_SingleObjetive(widget.OWWidget):
    name = "Sphere - Single-Objective - Problem"
    description = "Sphere Test Function Optimization"
    icon = "icons/sphere.svg"
    priority = 30

    class Inputs:
        number_of_variables = Input("number_of_variables", int)

    class Outputs:
        problem = Output("Problem",  Sphere)
   

    want_main_area = False

    def __init__(self):
        super().__init__()
        self.number_of_variables = None

        # Problem
        self.problem = None

        self.setFixedHeight(150)

        self.optionsBox = gui.label(self.controlArea, self, "Sphere Problem")
        
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
            print("\n\n*******\n Sphere sending problem")
            self.problem = Sphere(number_of_variables=self.number_of_variables)
            self.label.setText("The number of variables is %s" %self.number_of_variables)
        else:
            self.problem = None
        self.Outputs.problem.send(self.problem)

