from Orange.widgets.widget import OWWidget, Output
from Orange.widgets.settings import Setting
from Orange.widgets import gui

class IntNumber(OWWidget):
    # Widget's name as displayed in the canvas
    name = "Input an integer Number"
    # Short widget description
    description = "Lets the user input a number"

    # An icon resource file path for this widget
    # (a path relative to the module where this widget is defined)
    icon = "icons/input.svg"

    want_main_area = False
    
    number = Setting(42)
    # Widget's outputs; here, a single output named "Number", of type int
    class Outputs:
        number = Output("Number", int)

    def __init__(self):
        super().__init__()

        self.setFixedHeight(150)
        
        from AnyQt.QtGui import QIntValidator
        gui.lineEdit(self.controlArea, self, "number", "Enter a number",
                    box="Number",
                    callback=self.number_changed,
                    valueType=int, validator=QIntValidator())
        self.number_changed()

    def number_changed(self):
        # Send the entered number on "Number" output
        self.Outputs.number.send(self.number)