

class proc2:

   def run(self, busObjDict=None, arg1=None, arg2=None, arg3=None, mapFunc=None):
      print "proc2", arg1, arg2, arg3
      
      testString = "test string"
      if mapFunc: testString = mapFunc(testString)
      print "proc2 testString =", testString 