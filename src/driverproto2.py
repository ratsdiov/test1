import ConfigParser

import proc1
import proc2

config = ConfigParser.ConfigParser()
config.read("driverproto.cfg")

def getConfigArgs(section):

   args = {}
   if config.has_section(section):
      for (arg, val) in config.items(section): args[arg] = eval(val)
      
   return args 


def run(options, args):

   busObjDict = {1:2, 3:4}
   
   p1 = proc1.proc1()
   p1args = getConfigArgs("proc1")
   p1.run(busObjDict, **p1args)
   
   p2 = proc2.proc2()
   p2args = getConfigArgs("proc2")
   p2.run(busObjDict, **p2args)


def main():
   parser = OptionParser(usage="Use me")

   parser.add_option ("", "--debug",
                      dest="dbgLevel",
                      default=1,
                      type="int",
                      action="store",
                      help="Debug message verbosity, 0-3, 0=disable, 3=very verbose info, default is 1")

   parser.add_option ("", "--excluded_folders",
                      dest="excluded_folders",
                      default=None,
                      action="store",
                      help="Comma separated list of excluded folder names. Any objects within an excluded folder will not be migrated.")

   parser.add_option ("", "--final_mdx",
                      dest="final_mdx",
                      default=False,
                      action="store_true",
                      help="Write an EFS data set immediately before calling MDXtoTc.  The output EFS file name will be the base name of the output_efs file with '_FinalMDX appended.  Default is to NOT create this file.")

   (options, args) = parser.parse_args()

   run (options, args)

if __name__ == "__main__": main()