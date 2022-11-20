# Args

This is a library that makes args very easy to handle in python

to add a new flag  write
```
class NewFlag(Flag):
  shortFlag = "n"
  longFlag = "newFlag"
  discription="this is a discripton of what this flag does"
  def onCall(self,args):
    print("here you can do what you want")
    
a = Args([NewFlag()])
a.check()
```
