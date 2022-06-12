# Args

This is a library that makes args very easy to hanfle in python

to add a new flag  write
```
class NewFlag(Flag):
  shortFlag = "n"
  longFlag = "newFlag"
  def onCall(self,args):
    print("here you can do what you want")
    
a = Args([NewFlag()])
a.start()
```
