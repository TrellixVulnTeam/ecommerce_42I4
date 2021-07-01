from pathlib import Path
import os,sys
import importlib
sys.path.append("../..")

class Loader:

    def __init__(self):
        self.controller = None
        self.action = None
        self.request = None
        self.response  =None
        self.args = None
        self.kwargs = None
        self.main_dir = Path(os.getcwd())
        self.controller_dir = self.main_dir/"Utilities/communications/Controllers"
        self.controller_package = 'Web_Buy.Utilities.communications.Controllers.'

    def load(self,controller,action,request,response={},parameters={}):
        current_module = self.controller_package+controller
        controller_module = importlib.import_module(current_module)
        controller_class  = getattr(controller_module,controller)
        controller_obj = controller_class()
        action_obj = getattr(controller_obj,action)
        return action_obj(request=request,response=response,parameters=parameters)

