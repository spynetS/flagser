import sys

class Flag:
    # this is a description of the flag (gets printed when FlagManager.printHelp) is called
    description = "This is a test text. Here you should write the discription if the flag"
    # this method is called when a flag has been seen
    def __init__(self, shortFlag="",longFlag = "", onCall=None):
        self.shortFlag = shortFlag # this is the flag -i
        self.longFlag  = longFlag # this is for long flag names--install flag name
        self.onCall = onCall

    def onCall(self,args):
        print("Flag test was called with this args",args)
    #prints the flags and the description
    def __str__(self):
        return "-"+self.shortFlag+" --"+self.longFlag+"    "+self.description

# help flag class
class Help(Flag):
    shortFlag = "-h"
    longFlag = "--help"
    description = "prints flags and how to use the program"
    a = None
    def __init__(self,flagManager):
        self.a = flagManager

    def onCall(self, args):
        self.a.printHelp()


class FlagManager:
    flags = [] # flags to check for
    args = [] # all arguments taken when start
    description=""
    def __init__(self,flags=[]):
        self.flags = flags

        #If there is no help flag we add a default to the flags
        if(self.getFlag("-h") == None or self.getFlag("-help")==None):
            self.flags.append(Help(self))

        self.args = sys.argv
    # returns true if the arg is is a flag or not
    def isFlag(self,arg):
        for flag in self.flags:
            if(arg == (flag.shortFlag) or arg == (flag.longFlag)):
                return True
        return False
    # returns flag object with flagName
    def getFlag(self,flagName):
        for flag in self.flags:
            if (flag.longFlag) == flagName or (flag.shortFlag) == flagName:
                return flag
        return None

    #checks all the arguments for flags and calls thier onCall functions
    def check(self):
        reading = False
        flagArgs = []
        index = 0
        currentFlag = None
        for arg in self.args:
            if(reading and arg not in self.flags):
                flagArgs.append(arg)

            if(self.isFlag(arg)):
                if currentFlag != None:
                    temp = flagArgs
                    temp.pop()
                    currentFlag.onCall(temp)
                currentFlag = self.getFlag(arg)
                flagArgs.clear()
                reading = True

        if(currentFlag!=None):currentFlag.onCall(flagArgs)

    # prints all flags disciprtions and a helodescription
    def printHelp(self):
        print(self.description)
        for flag in self.flags:
            print(flag)
