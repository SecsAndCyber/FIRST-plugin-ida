# FIRST Plugin

# Add via "In Tool"
# 
# @category: Examples.Python
# @menupath Script.FIRST
# @keybinding alt z

import os
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

class FIRST_FormClass(JFrame):
    def __init__(self, *args, **kwargs):
        JFrame.__init__(self, *args, **kwargs)

        self.populate_model()
        self.populate_main_form()

    def populate_model(self):
        #   Selectable views in the main plug-in window
        self.views_ui = {'Configuration' : self.view_configuration_info,
                            'Management' : self.view_created,
                            'Currently Applied' : self.view_applied,
                            'About' : self.view_about}
        self.views = ['About', 'Configuration', 'Management', 'Currently Applied']
        self.views_model = FIRST.Model.Base(['Views'], self.views)

    def view_configuration_info(self):
        pass

    def save_config(self):
        pass

    def view_created(self):
        pass

    def __data_callback(self, thread, data):
        pass

    def __complete_callback(self, thread, data):
        pass

    def delete_metadata(self):
        pass

    def metadata_history(self):
        pass

    def view_about(self):
        pass

    def view_applied(self):
        pass

    def applied_custom_menu(self, point):
        pass

    def _metadata_history(self, metadata_id):
        pass

    def setText(self, event):
        print(self, event)
        
    def populate_main_form(self):
        self.setSize(100, 100)
        self.setLayout(BorderLayout())
        self.label = JLabel('Hello from Jython')
        self.add(self.label, BorderLayout.NORTH)
        button = JButton('Click Me',actionPerformed=self.setText)
        self.add(button, BorderLayout.SOUTH)
        self.setVisible(True)

    def view_clicked(self, index):
        pass

    def check_function_accept(self, dialog):
        pass

    def check_function(self, ctx):
        pass

    def check_all_function(self, ctx):
        pass

    def upload_func(self, ctx):
        pass

    def upload_all_func(self, ctx):
        pass

    def update_funcs(self, ctx):
        pass

    def view_history(self, ctx):
        pass

class FIRST(object):
    debug = True

    #   About Information
    #------------------------
    VERSION = 'DEV'
    DATE = 'May 2019'
    BEGIN = 2019
    END = 2019

    server = None
    config = None
    config_path = os.path.expanduser(os.path.join('~', '.first_ghidra.cfg'))
    installed_hooks = []
    function_list = None
    plugin = None
    iat = []

    #   Colors used
    # color_changed = QtGui.QBrush(QtGui.QColor.fromRgb(255, 153, 139))
    # color_unchanged = QtGui.QBrush(QtGui.QColor.fromRgb(238, 238, 238))
    # color_default = QtGui.QBrush(QtGui.QColor.fromRgb(255, 255, 255))
    # color_selected = QtGui.QBrush(QtGui.QColor.fromRgb(160, 216, 241))
    # color_applied = QtGui.QBrush(QtGui.QColor.fromRgb(214, 227, 181))
 
    class Error(Exception):
        '''FIRST Exception Class'''
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)

    
    class Metadata():
        '''Class containing Misc Metadata functions.
        Contains helper functions that will allow interaction with the memory
        list containing all functions within the IDB.
        This class contains only static methods and should be accessed as such.
        '''
        pass

    class Info():
        '''Information gathering functions.
        Will get different information required by FIRST to interact with
        server or other plug-in side operations.
        This class contains only static methods and should be accessed as such.
        Attributes:
            processor_map (:obj:`dict`): Dictionary mapping between IDA's naming
                convention to FIRST's.
            include_bits (:obj:`list`): List of processors that should include
                the number of bits.
        '''
        pass

    class DB():
        '''FIRST DB Class
        Provides functions to save data to and retrieve data from IDA's
        IDB backend. Additionally, it contains functions for calculating the
        index functions should be saved to in the IDB to provide constant time
        lookups.
        This class contains only static methods and should be accessed as such.
        Attributes:
            record_size (:obj:`int`): The number of bytes that can be saved into
                one index in the IDB's array. Once the number of bytes are hit
                the record is split and will continue in the next index.
                Note:
                    IDA enforces a hard limit of 1024, setting this value higher
                    than that will result in information loss.
            max_records (:obj:`int`): Determines how many array indices can be
                used to store data for a given function.
                Note:
                    If this number is increased and there is enough data to use
                    all the indices, this could result in over writting other
                    FIRST function data saved in the IDB.
        '''
        record_size = 1024
        max_records = 16

    class MetadataServer(object):
        '''Class to contain a FIRST match and its data.
        FIRST Metadata container, it encapsulates the data received from the
        FIRST server.
        Args:
            data (:obj:`dict`): Dictionary with the following key values set:
                name, prototype, creator, id, comment, rank
            address (:obj:`int`): The VA associated with the function the
                instance refers to.
            engine_info (:obj:`dict`): Dictionary with engine names mapping to
                the engine's description.
        Raises:
            FIRST.Error: If data is not a :obj:`dict` or does not have the
                required keys.
        '''
        pass

    class Configuration(object):
        '''Class containing configuration details for FIRST.
        Args:
            config (:obj:`RawConfigParser`): Configuration details for plugin.
        '''
        pass

    class Model(object):
        class Base(object):
            '''A QT QAbstractTableModel Implementation.
            Args:
                header (:obj:`list`): The column values.
                data (:obj:`dict`): Dictionary of values.
                parent (:obj:`QtCore.QObject`): The parent object.
            Overloads many class methods to provide the functionality FIRST
            required.
            '''
            def __init__(self, *args, **kwargs):
                pass

        
    class Callbacks(object):
        '''Callbacks for FIRST's Dialog UI components.
        This class contains only static methods and should be accessed as such.
        '''
        @staticmethod
        def welcome(dialog):
            '''Welcome dialog box handler.
            Args:
                dialog (:obj:`FIRSTUI.Welcome`): Welcome dialog box.
            '''
            FIRST.config = FIRSTUI.SharedObjects.get_config(dialog)
            FIRST.config.save_config(FIRST.config_path)

            info = FIRST.Info.get_file_details()
            FIRST.server = FIRST.Server(FIRST.config,
                                        info['md5'],
                                        info['crc32'],
                                        h_sha1=info['sha1'],
                                        h_sha256=info['sha256'])

            FIRST.Metadata.populate_function_list()
            FIRST.plugin_enabled = True

class FIRSTUI(object):
    ROLE_ID = 35
    ROLE_COMMENT = 36
    ROLE_ADDRESS = 37
    ROLE_NAME = 38

    class Requests(object):
        class MsgBox(object):
            def __init__(self, title, msg, icon=None):
                self.title = title
                self.msg = msg
                self.icon = icon

            def __call__(self):
                msg_box = QtWidgets.QMessageBox()
                msg_box.setIcon(self.icon)
                msg_box.setWindowTitle(self.title)

                msg_box.setText(self.msg)
                msg_box.exec_()
                return False # Don't reschedule

        class Print(object):
            def __init__(self, msg):
                self.msg = msg

            def __call__(self):
                IDAW.msg(self.msg)
                return False # Don't reschedule

        class Callback(object):
            def __init__(self, func, **kwargs):
                self.func = func
                self.kwargs = kwargs

            def __call__(self):
                self.func(**self.kwargs)
                return False # Don't reschedule



if __name__ == "__main__":
     frame = FIRST_FormClass("Jython Example JButton")
    
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
