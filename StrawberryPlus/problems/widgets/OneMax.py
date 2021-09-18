import sys
import numpy

import Orange.data
from Orange.widgets import widget, gui
from Orange.widgets.widget import Input, Output
#from Orange.widgets.utils.signals import Input, Output


# from JMetalpy
from jmetal.problem import OneMax


class OneMax_SingleObjetive(widget.OWWidget):
    name = "OneMax - Single-Objective - Problem"
    description = "Randomly selects a subset of instances from the data set"
    icon = "icons/mywidget.svg"
    priority = 10

    class Inputs:
        number_of_bits = Input("number_of_bits", int)

    class Outputs:
        problem = Output("Problem",  OneMax)
   

    want_main_area = False

    def __init__(self):
        super().__init__()
        self.number_of_bits = None

        # Problem
        self.problem = None

        self.optionsBox = gui.widgetBox(self.controlArea, "One Max Problem")
        
        self.label = gui.widgetLabel(self.controlArea, "The number is: ??")
        # Box to click the botton
        # from AnyQt.QtGui import QIntValidator
        # gui.lineEdit(self.controlArea, self, "One Max Problem", "Enter the number of bits",
        #             box="One Max Problem",
        #             callback=self.number_changed,
        #             valueType=int, validator=QIntValidator())
        # self.number_changed()

    @Inputs.number_of_bits
    def set_number_of_bits(self, number_of_bits):
        """Set the input number."""
        self.number_of_bits = number_of_bits

    def handleNewSignals(self):
        if self.number_of_bits is not None:
            print("\n\n*******\n OneMax sending problem")
            self.problem = OneMax(number_of_bits=self.number_of_bits)
            self.label.setText("The number of bits is %s" %self.number_of_bits)
        else:
            self.problem = None
        self.Outputs.problem.send(self.problem)

if __name__ == "__main__":
    from Orange.widgets.utils.widgetpreview import WidgetPreview
    
    WidgetPreview(OneMax_SingleObjetive).run(
        set_number_of_bits = 100
    )