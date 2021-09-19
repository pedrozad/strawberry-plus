import sys
import numpy

import Orange.data
from Orange.widgets import widget, gui
from Orange.widgets.widget import Input, Output

# from JMetalpy
from jmetal.problem.singleobjective.unconstrained import SubsetSum


class SubSet_SingleObjetive(widget.OWWidget):
    name = "SubSet Single-Objective - Problem"
    description = """Given an integer array A  of size N. 
    You are also given an integer B, you need to find whether their exist a subset in A whose sum equal B.
    If there exist a subset then return 1 else return 0."""
    icon = "icons/subset.svg"
    priority = 10

    class Inputs:
        C = Input("Sum to find", int) 
        W = Input("List of integers", list)
        data = Input("Data Table with the data", Orange.data.Table)
        
    class Outputs:
        problem = Output("Problem",  SubsetSum)

    want_main_area = False

    def __init__(self):
        super().__init__()
        self.C = None
        self.W = None
        self.data = None

        # Problem
        self.problem = None

        self.setMaximumWidth(600)
        self.setFixedHeight(300)

        self.optionsBox = gui.widgetBox(self.controlArea, "Subset Sum Problem")
        
        self.label = gui.widgetLabel(self.optionsBox, "The number is: ??")
        self.label_list = gui.widgetLabel(self.optionsBox, "List is: ??")
        # Box to click the botton
        # from AnyQt.QtGui import QIntValidator
        # gui.lineEdit(self.controlArea, self, "One Max Problem", "Enter the number of bits",
        #             box="One Max Problem",
        #             callback=self.number_changed,
        #             valueType=int, validator=QIntValidator())
        # self.number_changed()

    @Inputs.C
    def set_C(self, C):
        """Set the input number."""
        self.C = C
        self.label.setText("The number to find is %s" %self.C)

    @Inputs.W
    def set_W(self, W):
        """Set the input number."""
        self.W = W

    @Inputs.data
    def set_data(self, data):
        """Set the input number."""
        self.data = data
        if data is not None:
            self.W = []
            for d in data:
                self.W.extend(d)
        self.label_list.setText("List %s" %str(self.W))

    def handleNewSignals(self):
        if self.C is not None : #and self.W is not None:
            print("\n\n*******\n Subset Sum sending problem")
            if self.W is None :
                self.W = [2902, 5235, 357, 6058, 4846, 8280, 1295, 181, 3264,
                    7285, 8806, 2344, 9203, 6806, 1511, 2172, 843, 4697,
                    3348, 1866, 5800, 4094, 2751, 64, 7181, 9167, 5579,
                    9461, 3393, 4602, 1796, 8174, 1691, 8854, 5902, 4864,
                    # 5488, 1129, 1111, 7597, 5406, 2134, 7280, 6465, 4084,
                    # 3087, 5276, 9250, 1835, 9241, 1790, 1947, 8146, 8328,
                    # 973, 1255, 9733, 4314, 6912, 8007, 8911, 6802, 5102,
                    # 5451, 1026, 8029, 6628, 8121, 5509, 3603, 6094, 4447,
                    # 683, 6996, 3304, 3130, 2314, 7788, 8689, 3253, 5920,
                    3660, 2489, 8153, 2822, 6132, 7684, 3032, 9949, 59,
                    6669, 6334]
            self.problem = SubsetSum(self.C, self.W)
            
            
            self.label.setText("The number to find is %s" %self.C)
            self.label_list.setText("List %s" %str(self.W))
            print(self.problem)
            
        else:
            self.problem = None
        

        self.Outputs.problem.send(self.problem)

if __name__ == "__main__":
    from Orange.widgets.utils.widgetpreview import WidgetPreview
    
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


    WidgetPreview(SubSet_SingleObjetive).run(
        set_C = 300500,
        set_W = list_numbers
    )