import sys

class Args:
    flags = []
    args = []
    def __init__(self,flags=[]):
        self.flags = flags
        self.args = sys.argv
        self.args.remove("main.py")

    def isFlag(self,arg):
        for flag in self.flags:
            #print(arg == ("-"+flag.shortFlag))
            if(arg == ("-"+flag.shortFlag) or arg == ("--"+flag.longFlag)):
                return True
        return False

    def getFlag(self,flagName):
        for flag in self.flags:
           # print(("--"+flag.shortFlag))
            if ("--"+flag.longFlag) == flagName or ("-"+flag.shortFlag) == flagName:
                return flag
        return "ingen stämde"

    def start(self):
        reading = False
        flagArgs = []
        index = 0
        currentFlag = None
        for arg in self.args:
            if(reading and arg not in self.flags):
                #print("read",arg)
                flagArgs.append(arg)

            if(self.isFlag(arg)):
               # print("isflag",arg)
                if currentFlag != None:
                    currentFlag.onCall(flagArgs)
                currentFlag = self.getFlag(arg)
                flagArgs.clear()
                reading = True
                
        #print(index)
        currentFlag.onCall(flagArgs)
        


class Flag:
    shortFlag = ""
    longFlag = ""
    
    def onCall(self,args):
        pass

    def __str__(self):
        return "short-"+self.shortFlag+"  long--"+self.longFlag

class Help(Flag):
    shortFlag = "h"
    longFlag = "help"
    def onCall(self,args):
        print("hello boys")

class Install(Flag):
    shortFlag = "s"
    longFlag = ""
    def onCall(self,args):
        print("Installing",args)


a = Args([Help(),Install()])
a.start()