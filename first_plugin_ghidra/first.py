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

 
tool = state.getTool()
dtm = currentProgram.getDataTypeManager()

print dir(currentProgram.functionManager)
print currentProgram.functionManager
print currentProgram.functionManager.getFunctionCount()
print help(currentProgram.functionManager.getFunctions)
for func in currentProgram.functionManager.getFunctions(False):
    print func

# selectionDialog = DataTypeSelectionDialog(tool, dtm, -1, AllowedDataTypes.FIXED_LENGTH)
# tool.showDialog(selectionDialog)
# dataType = selectionDialog.getUserChosenDataType()
# if dataType is not None:
#     print "Chosen data type: " + str(dataType)
