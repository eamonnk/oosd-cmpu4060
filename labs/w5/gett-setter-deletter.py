class WithProp:
    
    def __init__(self):
        print("calling constructor")
        self._x = "a"

    def getx(self):
        print("calling getx")
        return self._x

    def setx(self, value):
        print("calling setx")
        self._x = value

    def delx(self):
        print("calling delx")
        del self._x

    x = property(getx, setx, delx)

def prhd(num):
    print("--------- {} -----------".format(num))
    
prhd(1)
wp = WithProp()

prhd(2)
print(wp.x)     # output: a

prhd(3)
wp.x = "b"

prhd(4)
print(wp.x)     # output: b

# prhd(5)
# del wp.x

# prhd(6)
# print(wp.x)     # error	
