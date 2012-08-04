class Clock:
    def Time(self):
        print("Clock says 6:00")

class WallClock(Clock):
    def Time(self):
        print("The wall clock says 6:00")


class WristWatch(Clock):
    def Time(self):
        print("The wrist watch says 6:00")
        
class Rolex(WristWatch ):
    def Time(self):
        print("This expensive rolex says 6:00")
        
class FakeRolex(Rolex):
    def Time(self):
        Rolex.Time(self)
        
Watch=FakeRolex()
Watch.Time()


