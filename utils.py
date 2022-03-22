import math


class Utils:

    def dist(self,pX1,pY1,pX2,pY2):
        return ((pX2-pX1)^2+(pY2-pY1)^2)^0.5


    def checkCollision(self,pX1,pY1,pW1,pH1,pX2,pY2,pW2,pH2):

        if pX1+pW1>=pX2 and pX1<=pX2+pW2:
            if pY1+pH1>=pY2 and pY1<=pY2+pH2:
                return True

        return False


    def easeInSine(self,t,b,c,d):
        return  -c * math.cos(t/d * (math.pi/2)) + c + b