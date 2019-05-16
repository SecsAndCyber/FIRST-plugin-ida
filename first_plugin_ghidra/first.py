# FIRST Plugin

# Add via "In Tool"
# 
# @category: Examples.Python
# @menupath Window.Load FIRST
# @keybinding alt z

from ghidra.util.classfinder import ClassSearcher
from ghidra.util.classfinder.ClassSearcher import *
from ghidra.framework.plugintool import Plugin, PluginEvent

DO_NOTHING_FILTER = lambda c: True

print ClassSearcher.getInstances(Plugin, DO_NOTHING_FILTER )