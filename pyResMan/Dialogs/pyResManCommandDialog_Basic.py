# -*- coding: utf-8 -*-

'''
Modified on 2017-03-28

@author: javacardos@gmail.com
@organization: https://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

from pyResMan.BaseDialogs.pyResManCommandDialogBase_Basic import CommandDialogBase_Basic
from pyResMan.Util import IDOK, IDCANCEL
from pyResMan.Util import HexValidator

###########################################################################
## Class CommandDialog_Basic
###########################################################################

MODE_IDLE = 0
MODE_PARSING = 1
MODE_BUILDING = 2

class CommandDialog_Basic ( CommandDialogBase_Basic ):
    def __init__( self, parent, bytesCount = 1 ):
        CommandDialogBase_Basic.__init__ ( self, parent )
        self.__mode = MODE_IDLE
        self._textctrlCommandValue.SetMaxLength(bytesCount * 2)
        # Set validator;
        self._textctrlCommandValue.SetValidator(HexValidator())
    
    def _buttonOKOnButtonClick(self, event):
        self.EndModal(IDOK)
    
    def _buttonCancelOnButtonClick(self, event):
        self.EndModal(IDCANCEL)
    
    def getCommandName(self):
        return self._statictextCommandName.GetLabelText()
    
    def getCommandValue(self):
        return self._textctrlCommandValue.GetValue()
        
    def setCommandName(self, name):
        self._statictextCommandName.SetLabelText(name)
        self.SetTitle(name)
    
    def setCommandValue(self, value):
        self._textctrlCommandValue.SetValue(value)
        self.parseCommandValue()
    
    def parseCommandValue(self):
        if self.__mode == MODE_IDLE:
            self.__mode = MODE_PARSING
            self.__mode = MODE_IDLE
        else:
            pass
    
    def buildCommandValue(self):
        if self.__mode == MODE_IDLE:
            self.__mode = MODE_BUILDING
            self.__mode = MODE_IDLE
        else:
            pass
