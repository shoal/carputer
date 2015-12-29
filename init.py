#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we create a bit
more complicated window layout using
the QtGui.QGridLayout manager. 

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtGui
from PyQt4.QtCore import QSize
from PyQt4.QtGui import *


""" Centre widget to control FM radio """
class RadioWidget(QtGui.QWidget):
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


""" CB radio control.
    
    Note that this is designed to be used whilst driving so minimal features.

    Go up the channels.
    Go down the channels.
    Scan the channels & stop on one where there's traffic.
    Display the current channel.
"""
class CBWidget(QtGui.QWidget):
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


""" MP3 player.

    Plays whatever is on the disk.   
 
    TODO: Scan phone for music, if connected.

"""
class MP3Widget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MP3Widget, self).__init__(parent)
 
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(True)

        holder = QtGui.QPushButton(" MP3 ", self)
        holder.setSizePolicy(sizePolicy)

        radioGrid = QtGui.QGridLayout()
        radioGrid.addWidget(holder, 0, 0)

       
        self.setLayout(radioGrid)



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


""" Features common to all widgets.  Eg volume.
"""
class CommonWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(CommonWidget, self).__init__(parent)

        holder = QtGui.QPushButton(" Common: Volume etc. ", self)

        radioGrid = QtGui.QGridLayout()
        radioGrid.addWidget(holder, 0, 0)

        self.setLayout(radioGrid)



class Carputer(QtGui.QWidget):
    
    def __init__(self):
        super(Carputer, self).__init__()
        
        self.initUI()

    def initUI(self):

        # Top bar to select mode.
        modeWidget = ModeListWidget(self)
        modeWidget.radioMode.clicked.connect(lambda: self.modeChange(0))
        modeWidget.mp3Mode.clicked.connect(lambda: self.modeChange(1))
        modeWidget.cbMode.clicked.connect(lambda: self.modeChange(2))
        modeWidget.phoneMode.clicked.connect(lambda: self.modeChange(3))

        # Stuff all centre layouts into a stack;
        radioWidget = RadioWidget(self)
        mp3Widget = MP3Widget(self)
        cbWidget = CBWidget(self)

        self.modeStack = QStackedWidget()
        self.modeStack.addWidget(radioWidget)
        self.modeStack.addWidget(mp3Widget)
        self.modeStack.addWidget(cbWidget)


        # Bottom widget does common stuff.  Volume etc.
        commonControls = CommonWidget(self)

        # Main display;
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        
        # Modes go along the top;
        grid.addWidget(modeWidget, 0, 0)

        # Content in the middle.
        grid.addWidget(self.modeStack, 1, 0)

        # Volume etc at the bottom.
        grid.addWidget(commonControls, 2, 0)


        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Carputer')    
        self.show()


    """ Called when someone presses one of the mode change buttons.
        
        Get the current widget.
        Send it the "you're getting closed" signal.
        Load the new widget
        Send the "you're open" signal.
    """
    def modeChange(self, modeIndex):
        if modeIndex < 0:
            print "Mode index < 0"
            return
        if modeIndex >= self.modeStack.count():
            print "Mode index >= count"
            return

        #TODO: "you're getting closed" signal.
        self.modeStack.setCurrentIndex(modeIndex)
        #TODO: "you're opened" signal.
        



def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Carputer()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

