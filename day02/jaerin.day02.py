## Fill in the following methods for the class 'Clock'

class Clock(object):
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    @classmethod
    def at(cls, hour, minutes=0):
        return cls(hour, minutes)

    ## Print the time
    def __str__(self):
        return 'It is %d h %d m'%(self.hour,self.minutes)
    ## Add time
    ## Don't return anythhing
    def __add__(self,minutes):
        if self.minutes+minutes>59:
            self.minutes=(self.minutes+minutes)%60
            self.hour=self.hour+(self.minutes+minutes)/60
        else: self.minutes=self.minutes+minutes

    ## Subtract time
    ## Don't return anything
    def __sub__(self,minutes):
        if self.minutes-minutes<0:
            self.minutes=(self.minutes-minutes)%60
            self.hour=self.hour-(self.minutes-minutes)/60
        else: self.minutes=self.minutes-minutes
    ## Are two times equal?
    def __eq__(self, other):
        return(self.hour==other.hour and self.minutes==other.minutes)
    ## Are two times not equal?
    def __ne__(self, other):
        return(self.hour!=other.hour or self.minutes!=other.minutes)
