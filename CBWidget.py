from PyQt4.QtGui import *
from PyQt4 import QtGui

from CentreWidgetBase import CentreWidgetBase

""" CB radio control.
    
    Note that this is designed to be used whilst driving so minimal features.

    Go up the channels.
    Go down the channels.
    Scan the channels & stop on one where there's traffic.
    Display the current channel.
"""
class CBWidget(CentreWidgetBase):
    def __init__(self, parent=None):
        super(CBWidget, self).__init__(parent)
 
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(True)

        prevButton = QtGui.QPushButton(" -- ", self)
        prevButton.setSizePolicy(sizePolicy)
        nextButton = QtGui.QPushButton(" ++ ", self)
        nextButton.setSizePolicy(sizePolicy)


        freqDisplay = QtGui.QLCDNumber(self)
        freqDisplay.display(8)
        freqDisplay.setSizePolicy(sizePolicy)
        
        scanButton = QtGui.QPushButton("Scan", self)
        scanButton.setSizePolicy(sizePolicy)


        radioGrid = QtGui.QGridLayout()
        radioGrid.addWidget(prevButton, 0, 0, 2, 1)
        radioGrid.addWidget(freqDisplay, 0, 1, 1, 2)
        radioGrid.addWidget(scanButton, 1, 1, 1, 2)
        radioGrid.addWidget(nextButton, 0, 3, 2, 1)
       
        self.setLayout(radioGrid)


