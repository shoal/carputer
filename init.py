#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Main GUI window.  


Layout:
 - Tabs along the top for functions
 - Bit in the middle for the feature itself 
 - Bar along the bottom for common controls

"""

import sys
from PyQt4 import QtGui
from PyQt4.QtGui import *


# Import all of the widgets.
from RadioWidget import RadioWidget
from CBWidget import CBWidget
from MP3Widget import MP3Widget
from ModeListWidget import ModeListWidget
from CommonWidget import CommonWidget




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

        # Tell the old widget to pause.
        currentWidget = self.modeStack.currentWidget()
        currentWidget.deactivate()

        # Load the new widget
        self.modeStack.setCurrentIndex(modeIndex)
        
        # Tell the new widget to play.
        currentWidget = self.modeStack.currentWidget()
        currentWidget.activate()



def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Carputer()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

