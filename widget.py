# Standard imports...
from Orange.widgets import widget, gui
from Orange.widgets.utils.widgetpreview import WidgetPreview
from Orange.widgets.settings import Setting

__version__ = "0.01"


class SCIhubator(widget.OWWidget):
    """An Orange widget that lets the user select an integer value"""

    # ----------------------------------------------------------------------
    # Widget's metadata...

    name = "SCIhubator"
    description = "input a DOI/URL to convert to text"
    icon = "icons/mywidget.svg"  # à modifier
    priority = 10

    # ----------------------------------------------------------------------
    # Channel definitions (NB: no input in this case)...

    inputs = []
    outputs = [("text segmentation", LTTL.Segment)] #à verifier

    # ----------------------------------------------------------------------
    # GUI layout parameters...

    want_main_area = False
    resizing_enabled = True

    # ----------------------------------------------------------------------
    # Settings declaration and initializations (default values)...

    selected_url = Setting(None)

    def __init__(self):
        super().__init__()

        # ----------------------------------------------------------------------
        # User interface...

        #tentative de faire un lineedit pour l'url et un checkbox
        gui.lineEdit(
            widget=self.controlArea,  # Containing interface element (usually
            # self.controlArea or some widgetBox).
            master=self,  # Object which stores the corresponding
            # setting (normally self).
            value='selected_url',  # Setting name.
            label='input a url/DOI: ',  # Label.
            labelWidth = None,
            orientation = 2,
            box = None,
            callback=self.url_changed,  # Method called when control changes.
            valueType = None,
            validator = None,
            controlWidth = None,
            callbackOnType=False,
            focusInCallback=None
        )

        #gui.checkBox(
            widget=self.controlArea,
            master = self,
            value ="selected_url",
            label ='All: ',
            box=None,
            callback=self.url_changed,
            getwidget=False,
            id_=None,
            labelWidth=None,
            disables=None,
            stateWhenDisabled=None
        #)

        self.url_changed()

    def int_changed(self):
        """Send the entered number on "Number" output"""
        self.send("text segmentation", self.selected_url)


# The following code lets you execute the code outside of Orange (to view the
# resulting interface)...
if __name__ == "__main__":
    WidgetPreview(SCIhubator).run()

