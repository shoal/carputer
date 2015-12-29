
from PyQt4 import QtGui


""" Features common to all centre widgets - base class.

    Used as interface to ensure the widgets get the correct setup/teardown.
"""
class CentreWidgetBase(QtGui.QWidget):
    def __init__(self, parent=None):
        super(CentreWidgetBase, self).__init__(parent)

    """ Widget is now being displayed """
    def activate(self):
        pass

    """ Widget has been hidden """
    def deactivate(self):
        pass


