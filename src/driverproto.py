import ConfigParser

import proc1
import proc2
from imp import load_source # Note this must be put into the global namespace so evals against
                            # load_source in config files don't require an imp. prefix.  To use,
                            # add an entry like the following to the config file:
                            #   CustomModule=load_source("processor_name", "custom_processor_module.py")

# Import additional configuration functions (if any).  These can then be
# referenced in driver config files as "ConfigFunctions.func_name" and
# then passed/called as function references.  Note these can be combined with
# custom processor overrides as well.

try:
   import ConfigFunctions
except ImportError:
   ConfigFunctions = None

config = ConfigParser.ConfigParser()
config.optionxform = str
config.read("driverproto.cfg")

#---------------------------------------------------------------
def getConfigArgs(processorName, processorModule):

   argsDict = {}
   if config.has_section(processorName):
      for (arg, val) in config.items(processorName): argsDict[arg] = eval(val)

   # Return either default processor module or custom one if one was defined plus any configured arguments

   return (argsDict.pop("CustomModule", processorModule), argsDict)

#---------------------------------------------------------------

busObjDict = {1:2, 3:4}

(p1Module, p1Args) = getConfigArgs("proc1", proc1)
p1 = p1Module.proc1()
p1.run(busObjDict, **p1Args)

(p2Module, p2Args) = getConfigArgs("proc2", proc2)
p2 = p2Module.proc2()
p2.run(busObjDict, **p2Args)
