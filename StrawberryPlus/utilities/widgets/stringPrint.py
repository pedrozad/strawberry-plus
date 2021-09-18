from Orange.widgets.widget import OWWidget, Input
from Orange.widgets import gui

class PrintResults(OWWidget):
    name = "Print (String)"
    description = "Prints out a String"
    icon = "icons/print.svg"

    class Inputs:
        result = Input("String", str)

    want_main_area = False

    def __init__(self):
        super().__init__()
        self.result = None

        self.label = gui.widgetLabel(self.controlArea, "The result is: ??")

    @Inputs.result
    def set_result(self, number):
        """Set the input number."""
        self.result = number
        if self.result is None:
            self.label.setText("There isn't any result to show")
        else:
            # self.label.setText("The number is {}".format(self.number))
            self.label.setText(self.result)