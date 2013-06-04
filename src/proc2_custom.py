

class proc2:

   def run(self, busObjDict=None, arg1=None, arg2=None, arg3=None, mapFunc=None):
      print "proc2_custom", arg1, arg2, arg3
      
      testString = "test string"
      if mapFunc: testString = mapFunc("test string")
      print "proc2_custom testString =", testString 