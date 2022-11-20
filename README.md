# Flagser

This is a library that makes args very easy to handle in python

to add a new flag write
```
class NewFlag(Flag):
  shortFlag = "-n"
  longFlag = "--newFlag"
  description="this is a discripton of what this flag does"
  def onCall(self,args):
    print("here you can do what you want")

a = FlagManager([NewFlag()])
a.check()

```
Then add the flags you have created as the constructor
parameters for the FlagManager
then call the check() of the flagmanager object
and the flagmanager will check the flags
