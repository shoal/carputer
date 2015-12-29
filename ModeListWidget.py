from PyQt4.QtGui import *
from PyQt4 import QtGui


""" List all of the functions available.
"""
class ModeListWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ModeListWidget, self).__init__(parent)

        self.radioMode = QtGui.QPushButton("Radio", self)
        self.mp3Mode = QtGui.QPushButton("MP3", self)
        self.cbMode = QtGui.QPushButton("CB", self)
        self.phoneMode = QtGui.QPushButton("Phone", self)

        modeGrid = QtGui.QGridLayout()
        modeGrid.setSpacing(10)
        modeGrid.addWidget(self.radioMode, 0, 0)
        modeGrid.addWidget(self.mp3Mode, 0, 1)
        modeGrid.addWidget(self.cbMode, 0, 2)
        modeGrid.addWidget(self.phoneMode, 0, 3)

        self.setLayout(modeGrid)

