# FIRST Plugin

# Add via "In Tool"
# 
# @category: Examples.Python
# @menupath Script.FIRST
# @keybinding alt z

import ghidra.app.plugin

class MyPlugin(ghidra.app.plugin.ProgramPlugin):
    pass

from ghidra.app.util.datatype import DataTypeSelectionDialog
from ghidra.framework.plugintool import PluginTool
from ghidra.program.model.data import DataType
from ghidra.program.model.data import DataTypeManager
from ghidra.util.data.DataTypeParser import AllowedDataTypes

 
from javax.swing import JFrame, JLabel, JButton, WindowConstants
from java.awt import BorderLayout

class Example:
   def setText(self,event):
       self.label.text = "{}".format(currentProgram)
 
   def __init__(self):
     frame = JFrame("Jython Example JButton")
     frame.setSize(100, 100)
     frame.setLayout(BorderLayout())
     self.label = JLabel('Hello from Jython')
     frame.add(self.label, BorderLayout.NORTH)
     button = JButton('Click Me',actionPerformed=self.setText)
     frame.add(button, BorderLayout.SOUTH)
     frame.setVisible(True)

frame = Example()
# tool = state.getTool()
# dtm = currentProgram.getDataTypeManager()

# print dir(currentProgram.functionManager)
# print currentProgram.functionManager
# print currentProgram.functionManager.getFunctionCount()
# print help(currentProgram.functionManager.getFunctions)
# for func in currentProgram.functionManager.getFunctions(False):
#     print func

# selectionDialog = DataTypeSelectionDialog(tool, dtm, -1, AllowedDataTypes.FIXED_LENGTH)
# tool.showDialog(selectionDialog)
# dataType = selectionDialog.getUserChosenDataType()
# if dataType is not None:
#     print "Chosen data type: " + str(dataType)
