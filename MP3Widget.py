from PyQt4.QtGui import *
from PyQt4 import QtGui

from CentreWidgetBase import CentreWidgetBase

""" MP3 player.

    Plays whatever is on the disk.   
 
    TODO: Scan phone for music, if connected.

"""
class MP3Widget(CentreWidgetBase):
    def __init__(self, parent=None):
        super(MP3Widget, self).__init__(parent)
 
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(True)

        holder = QtGui.QPushButton(" MP3 ", self)
        holder.setSizePolicy(sizePolicy)

        radioGrid = QtGui.QGridLayout()
        radioGrid.addWidget(holder, 0, 0)

       
        self.setLayout(radioGrid)


