from PyQt4 import QtGui
from PyQt4.QtGui import *

from CentreWidgetBase import CentreWidgetBase

""" Centre widget to control FM radio """
class RadioWidget(CentreWidgetBase):
    def __init__(self, parent=None):
        super(RadioWidget, self).__init__(parent)
 
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(True)

        prevButton = QtGui.QPushButton(" << ", self)
        prevButton.setSizePolicy(sizePolicy)
        nextButton = QtGui.QPushButton(" >> ", self)
        nextButton.setSizePolicy(sizePolicy)


        freqDisplay = QtGui.QLCDNumber(self)
        freqDisplay.display(88.9)
        freqDisplay.setSizePolicy(sizePolicy)
        
        infoLabel = QtGui.QLabel("Station/Artist", self)
        #infoLabel.setSizePolicy(sizePolicy)


        radioGrid = QtGui.QGridLayout()
        radioGrid.addWidget(prevButton, 0, 0, 2, 1)
        radioGrid.addWidget(freqDisplay, 0, 1, 1, 2)
        radioGrid.addWidget(infoLabel, 1, 1, 1, 2)
        radioGrid.addWidget(nextButton, 0, 3, 2, 1)
       
        self.setLayout(radioGrid)
