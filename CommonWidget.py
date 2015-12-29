from PyQt4.QtGui import *
from PyQt4 import QtGui


""" Features common to all widgets.  Eg volume.
"""
class CommonWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(CommonWidget, self).__init__(parent)

        holder = QtGui.QPushButton(" Common: Volume etc. ", self)

        radioGrid = QtGui.QGridLayout()
        radioGrid.addWidget(holder, 0, 0)

        self.setLayout(radioGrid)

