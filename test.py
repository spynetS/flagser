from flagser import*


one = Flag("-o", onCall=lambda args: print(args))
two = Flag("-t", onCall=lambda args: print(args))

a = FlagManager([one, two])
a.check()
