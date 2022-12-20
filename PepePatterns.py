import pygame
import random

#### NEW PATTERNS TO IMPLEMENT:

## - A RANDOM SQUARES PATTERNS(PEPEMACHINESIGNATURE) - 2 - DONE
## - LOSANGLE INSIDE LOSANGLE - 1 - DONE
## - SQUARE INSIDE SQUARE - 1 - DONE
## - ROUND CORNERS SQUARE (OLD "BC" OR BIG CIRCLE) - 3 - Not gonna Do it

#### NEW PATTERNS TO IMPLEMENT WITH ??SPRITESHEETS?? - 5

## - CAMUFLADO
## - BRIGADEIRO
## - ZEBRADO

#### OBJECTS FOR DEEPER MEANING - 4

## - FLOWER
## - SMILE
## - HEART
## - EYE

class PatternStyles:
    def __init__(self,CorFundo,CorPattern,Filletes,patternEssencials,PepeQuad1,PepeQuad2):
        self.CorPattern = CorPattern
        self.CorFundo = CorFundo
        self.Filletes = Filletes
        self.patternEssencials = patternEssencials
        self.divLarg = patternEssencials[0]
        self.divAlt = patternEssencials[1]
        self.largTela = patternEssencials[2]
        self.altTela = patternEssencials[3]
        self.screen = patternEssencials[4]
        self.PepeQuad1 = PepeQuad1
        self.PepeQuad2 = PepeQuad2
        

    def pepesAiSignature(self,FinalPepeColors):
        x,y,sizeX,sizeY = self.Filletes[-1]

        oldX = x
        Xtimes = int(sizeX / (self.largTela/self.divLarg))
        Ytimes = int(sizeY / (self.altTela/self.divAlt))

        for yfuck in range(Ytimes):
            for xfuck in range(Xtimes):
                self.PatColor = random.choice(FinalPepeColors)
                self.imaa = pygame.draw.rect(self.screen,self.PatColor,((self.largTela/self.divLarg)*(x+xfuck) ,((self.altTela/self.divAlt)*(y+yfuck)),self.largTela/self.divLarg,self.altTela/self.divAlt))
                print("x = ",x,"y =",y)
                xfuck+=1
            xfuck=oldX
            yfuck+=1
        print("ITTs working",FinalPepeColors)
      
    
    def MakesCirclesOnFillete(self):
        x,y,sizeX,sizeY = self.Filletes[-1]

        center = (x * (self.largTela/self.divLarg)) + (sizeX/2),(y * (self.largTela/self.divLarg))+ (sizeY/2)

        if sizeX > sizeY:
            rad = sizeY/2
        elif sizeY > sizeX:
            rad = sizeX/2
        else:
            rad = sizeY/2

        pygame.draw.circle(self.screen,self.CorPattern,center,rad)

    def MakeSquaresInsideSquares(self):
        x,y,sizeX,sizeY = self.Filletes[-1]

        startpoint1 = (x * (self.largTela/self.divLarg)) + (sizeX/4),(y * (self.largTela/self.divLarg))+ (sizeY/4)
        dimensions1 = (sizeX/4) * 2, (sizeY/4) * 2

        pygame.draw.rect(self.screen,self.CorPattern,(startpoint1,dimensions1))
    

    def MakesCirclesinCirclesOnFillete(self):
        Patcolor = self.CorPattern

        x,y,sizeX,sizeY = self.Filletes[-1]
        center = (x * (self.largTela/self.divLarg)) + (sizeX/2),(y * (self.largTela/self.divLarg))+ (sizeY/2)
        if sizeX > sizeY:
            rad = sizeY/2
        elif sizeY > sizeX:
            rad = sizeX/2
        else:
            rad = sizeY/2
        pygame.draw.circle(self.screen,Patcolor,center,rad)
        pygame.draw.circle(self.screen,self.CorFundo,center,(rad/3)*2)
        pygame.draw.circle(self.screen,Patcolor,center,rad/3)
        

    def MakesCirclesPatternOnFillete(self):
        x,y,sizeX,sizeY = self.Filletes[-1]
        px = x + 1
        nx = int(sizeX/(self.largTela/self.divLarg))
        ny = int(sizeY/(self.altTela/self.divAlt))
        PatColor = self.CorPattern

        for s in range(0,ny):
            for u in range(0,nx,2):
                if s % 2 == 0:
                    self.MakesCirclesPosforPattern(x+u,y+s,PatColor)
                    #print("CIRCLE ",x+u,y+s," is on",nx+x)
                elif s % 2 != 0 and (px+u)>=(nx+x) and (px+u) != (self.altTela/self.divAlt):
                    break
                elif s % 2 != 0:
                    self.MakesCirclesPosforPattern(px+u,y+s,PatColor)

    def MakesCirclesPosforPattern(self,NewX,NewY,PatColor):
        center = ((self.largTela/self.divLarg)* NewX) + ((self.largTela/self.divLarg)/2), ((self.altTela/self.divAlt) * NewY) + ((self.altTela/self.divAlt)/2)
        if self.self.altTela/self.divAlt <= self.largTela/self.divLarg:
            rad = (self.altTela/self.divAlt)/2
        else:
            rad = (self.largTela/self.divLarg)/2
        pygame.draw.circle(self.screen,PatColor,center,rad)
        


    ### Pattern Shapes --- Not in order sorry

    def MakeSquarePattern(self):
        x = int(input("Start Horizontal: ")) - 1
        y = int(input("Start Vertical: ")) - 1
        PatColor = self.CorPattern
        self.DrawSquarePattern()


    def DrawSquarePattern(self,x,y,PatColor):
        daseX =((self.largTela/self.divLarg)/2)
        daseY =((self.altTela/self.divAlt)/2)
        cubo1 = pygame.draw.rect(self.screen,PatColor,((self.largTela/self.divLarg)*x,((self.altTela/self.divAlt)*y),((self.largTela/self.divLarg)/2),((self.altTela/self.divAlt)/2)))
        cubo2 = pygame.draw.rect(self.screen,PatColor,(((self.largTela/self.divLarg)*x) + daseX,((self.altTela/self.divAlt)*y) + daseY,((self.largTela/self.divLarg)/2),((self.altTela/self.divAlt)/2)))
        #print("made Square Pattern",daseX,daseY)

    def LineSquarePattern(self,x,y):
        x,y = self.PepeQuad2
        x = x - 1
        y = y - 1
        comp,alt = self.PepeQuad1
        PatColor = self.CorPattern
        for y in range(y,y + alt):
            self.LinePattern(x,y,PatColor,comp)

    def LinePattern(self,x,y,PatColor,comp):
        for x in range(x,x+comp):
            self.DrawSquarePattern(x,y,PatColor)
            x += 1


    # Fillete Shapes

    def MakesZigZagPatternFillete(self):   
        x,y,sizeX,sizeY = self.Filletes[-1]
        nx = int(sizeX/(self.largTela/self.divLarg))
        ny = int(sizeY/(self.altTela/self.divAlt))
        qx = self.largTela/self.divLarg
        qy = self.altTela/self.divAlt
        realX = x * qx
        realY = y * qy
        therealX = realX

        PatColor = self.CorPattern

    
        for s in range(ny):
            if s % 2 == 0:
                a = 0
            else:
                a = qx
            #realX = therealX + (s*qx)
            for p in range(nx):
                pos1 = (realX + (qx*p))+a, (realY) + (qy*s)
                pos2 = (realX + (qx*p)), (realY + qy) + (qy*s)
                pos3 = ((realX + qx) + (qx*p)), (realY + qy) + (qy*s)
                p += 1
                #pygame.draw.rect(self.screen,PatColorHolder[-1],(pos1[0],pos1[1],qx,qy))
                pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3))
                #print(p,s,pos1,pos2,pos3,PatColorHolder[-1],PatColor,"par")
            s +=1              



    def Makes45gLinesPatternFillete(self):
        x,y,sizeX,sizeY = self.Filletes[-1]
        nx = int(sizeX/(self.largTela/self.divLarg))
        ny = int(sizeY/(self.altTela/self.divAlt))
        qx = self.largTela/self.divLarg
        qy = self.altTela/self.divAlt
        realX = x * qx
        realY = y * qy
        therealX = realX

        PatColor = self.CorPattern

        realPatColor = PatColor
        realFilletesCor = self.CorFundo

        realrealPatColor = PatColor
        realrealFilletesCor = self.CorFundo

    
        for s in range(ny):
            if s % 2 != 0:
                realPatColor = realrealPatColor
                realFilletesCor = realrealFilletesCor 
            else:
                realFilletesCor = realrealPatColor 
                realPatColor = realrealFilletesCor
            #realX = therealX + (s*qx)
            for p in range(nx):
                if p % 2 != 0:
                    PatColor = realFilletesCor
                    self.CorPattern = realPatColor
                else:
                    PatColor = realPatColor
                    self.CorPattern = realFilletesCor
                pos1 = realX + (qx*p), (realY) + (qy*s)
                pos2 = realX + (qx*p), (realY + qy) + (qy*s)
                pos3 = (realX + qx) + (qx*p), (realY + qy) + (qy*s)
                p += 1
                pygame.draw.rect(self.screen,self.CorPattern,(pos1[0],pos1[1],qx,qy))
                pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3))
                #print(p,s,pos1,pos2,pos3,PatColorHolder[-1],PatColor,"par")
            s +=1

    def MakesDistortLosanglesPatternFillete(self):
        x,y,sizeX,sizeY = self.Filletes[-1]
        nx = int(sizeX/(self.largTela/self.divLarg))
        ny = int(sizeY/(self.altTela/self.divAlt))
        qx = self.largTela/self.divLarg
        qy = self.altTela/self.divAlt
        realX = x * qx
        realY = y * qy

        PatColor = self.CorPattern


        for s in range(ny):
            for p in range(nx):
                if p % 2 == 0:
                    pos1 = realX + (qx*p), (realY) + (qy*s)
                    pos2 = realX + (qx*p), (realY + qy) + (qy*s)
                    pos3 = (realX + qx) + (qx*p), (realY + qy) + (qy*s)
                    p += 1
                    pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3))
                else:
                    pos1 = realX + (qx*p), (realY) + (qy*s)
                    pos2 = realX + (qx*p), (realY + qy) + (qy*s)
                    pos3 = (realX + qx) + (qx*p), (realY + qy) + (qy*s)
                    p += 1
                    pygame.draw.rect(self.screen,PatColor,(pos1[0],pos1[1],qx,qy))
                    pygame.draw.polygon(self.screen,self.CorFundo,(pos1,pos2,pos3))
            s +=1

    def MakesTriangleGridPatternFillete(self):
        x,y,sizeX,sizeY = self.Filletes[-1]
        nx = int(sizeX/(self.largTela/self.divLarg))
        ny = int(sizeY/(self.altTela/self.divAlt))
        qx = self.largTela/self.divLarg
        qy = self.altTela/self.divAlt
        realX = x * qx
        realY = y * qy

        PatColor = self.CorPattern
        for s in range(ny):
            for p in range(nx):
                pos1 = realX + (qx*p), (realY) + (qy*s)
                pos2 = realX + (qx*p), (realY + qy) + (qy*s)
                pos3 = (realX + qx) + (qx*p), (realY + qy) + (qy*s)
                p += 1
                pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3))
            s +=1


    def MakesLosanglePatternFillete(self):
        x,y,sizeX,sizeY = self.Filletes[-1]
        nx = int(sizeX/(self.largTela/self.divLarg))
        ny = int(sizeY/(self.altTela/self.divAlt))
        qx = self.largTela/self.divLarg
        qy = self.altTela/self.divAlt
        realX = x * qx
        realY = y * qy
        therealY = realY
        PatColor = self.CorPattern

        p = 1


        for s in range(ny):
            realY = therealY
            realY = realY + (qy*s)
            s += 1
            for p in range(nx):

                pos1 = (realX +(qx*p)) + (qx/2), realY
                pos2 = (realX +(qx*p)), realY + (qy/2)
                pos3 = (realX +(qx*p)) + (qx/2), realY + qy
                pos4 = (realX +(qx*p)) + qx, realY + (qy/2)
                p+=1
                pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3,pos4))


    def MakesLosangleInsideLosangle(self):
        x,y,sizeX,sizeY = self.Filletes[-1]

        x = x*(self.largTela/self.divLarg)
        y = y*(self.altTela/self.divAlt)

        pos1 = x + (sizeX/2), y
        pos2 = x , y + (sizeY/2)
        pos3 = x + (sizeX/2) , y + sizeY
        pos4 = x + sizeX , y + (sizeY/2)
        PatColor = self.CorPattern

        pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3,pos4))

        pos5 = x + (sizeX/2), y + (sizeY/4)
        pos6 = x + (sizeX/4), y + (sizeY/2)
        pos7 = x + (sizeX/2), y + ((sizeY/4)*3)
        pos8 = x + ((sizeX/4)*3), y + (sizeY/2)

        pygame.draw.polygon(self.screen,self.CorFundo,(pos5,pos6,pos7,pos8))





    def MakesLosangleFillete(self):
        x,y,sizeX,sizeY = self.Filletes[-1]

        x = x*(self.largTela/self.divLarg)
        y = y*(self.altTela/self.divAlt)

        pos1 = x + (sizeX/2), y
        pos2 = x , y + (sizeY/2)
        pos3 = x + (sizeX/2) , y + sizeY
        pos4 = x + sizeX , y + (sizeY/2)
        PatColor = self.CorPattern
        pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3,pos4))


    def MakeSetas(self):
        x,y,sizeX,sizeY = self.Filletes[-1]

        yLevel = int(sizeY / (self.altTela/self.divAlt))

        x = x*(self.largTela/self.divLarg)
        y = y*(self.altTela/self.divAlt)
        Patcolor = self.CorPattern

        t = x + (sizeX/2), y
        e = x, y + sizeY
        d = x + sizeX, y + sizeY

        CorP = 2

        for f in range(yLevel-1):
            if CorP == 2:
                t = x + (sizeX/2), y + (f * (self.altTela/self.divAlt))
                e = x, (y + ((self.altTela/self.divAlt)*2)) + (f * (self.altTela/self.divAlt))
                d = x + sizeX, (y + ((self.altTela/self.divAlt)*2)) + (f * (self.altTela/self.divAlt))
                r = sizeX, (sizeY - (f * (self.altTela/self.divAlt)))- ((self.altTela/self.divAlt)*2)
                pygame.draw.polygon(self.screen,Patcolor,(t,e,d))
                pygame.draw.rect(self.screen,Patcolor,(e,r))
                #print("par",r)
                f +=1
                CorP = 3
            elif CorP == 3:
                t = x + (sizeX/2), y + (f * (self.altTela/self.divAlt))
                e = x, (y + ((self.altTela/self.divAlt)*2)) + (f * (self.altTela/self.divAlt))
                d = x + sizeX, (y + ((self.altTela/self.divAlt)*2)) + (f * (self.altTela/self.divAlt))

                r = sizeX, (sizeY - (f * (self.altTela/self.divAlt)))- ((self.altTela/self.divAlt)*2)

                pygame.draw.polygon(self.screen,self.CorFundo,(t,e,d))
                pygame.draw.rect(self.screen,self.CorFundo,(e,r))
                    #print("impar",r)

                f +=1
                CorP = 2


    def MakesCirclesPatternOnFillete(self,CorPattern):
        x,y,sizeX,sizeY = self.Filletes[-1]
        px = x + 1
        nx = int(sizeX/(self.largTela/self.divLarg))
        ny = int(sizeY/(self.altTela/self.divAlt))
        PatColor = CorPattern

        for s in range(0,ny):
            for u in range(0,nx,2):
                if s % 2 == 0:
                    self.MakesCirclesPosforPattern(x+u,y+s,PatColor)
                    #print("CIRCLE ",x+u,y+s," is on",nx+x)
                elif s % 2 != 0 and (px+u)>=(nx+x) and (px+u) != (self.altTela/self.divAlt):
                    print()
                #elif s % 2 != 0 and (px+u) == (self.altTela/self.divAlt):
                #    MakesCirclesPosforPattern(px+u,y+s,PatColor)
                #    print("CIRCLE ",px+u,y+s," is special",nx+x)
                elif s % 2 != 0:
                    self.MakesCirclesPosforPattern(px+u,y+s,PatColor)
                    #print("CIRCLE ",px+u,y+s," is on",nx+x)

    def MakesCirclesPosforPattern(self,NewX,NewY,PatColor):
        center = ((self.largTela/self.divLarg)* NewX) + ((self.largTela/self.divLarg)/2), ((self.altTela/self.divAlt) * NewY) + ((self.altTela/self.divAlt)/2)
        if self.altTela/self.divAlt <= self.largTela/self.divLarg:
            rad = (self.altTela/self.divAlt)/2
        else:
            rad = (self.largTela/self.divLarg)/2
        self.MakesCirclePat(center,rad,PatColor)

    def MakesCirclePat(self,center,rad,PatColor):
        pygame.draw.circle(self.screen,PatColor,center,rad)
        
        #print("IT MAKES CIRCLES")


    def MakesCirclesOnFillete(self):
        Patcolor = self.CorPattern

        x,y,sizeX,sizeY = self.Filletes[-1]
        center = (x * (self.largTela/self.divLarg)) + (sizeX/2),(y * (self.largTela/self.divLarg))+ (sizeY/2)
        if sizeX > sizeY:
            rad = sizeY/2
        elif sizeY > sizeX:
            rad = sizeX/2
        else:
            rad = sizeY/2
        self.MakesCircle(center,rad,Patcolor)
        #print(x,y,sizeX,sizeY)

    def MakesTriangleOnFillete(self,CorPattern):
        x,y,sizeX,sizeY = self.Filletes[-1]

        pos1 = x * (self.largTela/self.divLarg), y * (self.altTela/self.divAlt)
        pos2 = x * (self.largTela/self.divLarg), (y * (self.altTela/self.divAlt)) + sizeY
        pos3 = x * (self.largTela/self.divLarg) + sizeX, (y * (self.altTela/self.divAlt)) + sizeY
        self.MakesTriangles(pos1,pos2,pos3,CorPattern)

    def MakesTrianglePatternOnFillete(self):
        x,y,sizeX,sizeY = self.Filletes[-1]
        rangeX = int(sizeX / (self.largTela/self.divLarg))
        rangeY = int(sizeY / (self.altTela/self.divAlt))
        mk = 1
        PatColor = self.CorPattern


        if rangeX >= rangeY:
            for mk in range(rangeX):
                pos1 = x * (self.largTela/self.divLarg) + (self.largTela/self.divLarg)*mk, y * (self.altTela/self.divAlt)
                pos2 = x * (self.largTela/self.divLarg) + (self.largTela/self.divLarg)*mk, (y * (self.altTela/self.divAlt)) + sizeY
                pos3 = x * (self.largTela/self.divLarg) + ((self.largTela/self.divLarg)*(mk+1)), (y * (self.altTela/self.divAlt)) + sizeY
                self.MakesTrianglesPattern(pos1,pos2,pos3,PatColor)
                mk += 1
        else:
            for mk in range(rangeY):
                pos1 =  x * (self.largTela/self.divLarg), (y * (self.altTela/self.divAlt)) + ((self.altTela/self.divAlt)*mk)
                pos2 = (x * (self.largTela/self.divLarg))+sizeX, (y * (self.altTela/self.divAlt)) + ((self.altTela/self.divAlt)*mk)
                pos3 = (x * (self.largTela/self.divLarg))+sizeX, (y * (self.altTela/self.divAlt)) + ((self.altTela/self.divAlt)*(mk + 1))
                self.MakesTrianglesPattern(pos1,pos2,pos3,PatColor)
                mk += 1

    def MakesVerticalLinePatternOnFillete(self):
        x,y,NFsizeX,NFsizeY = self.Filletes[-1]
        rangeX = NFsizeX / (self.largTela/self.divLarg)
        rangeY = int(NFsizeY / (self.altTela/self.divAlt))
        PatColor = self.CorPattern
        if rangeX % 2 == 0:
            rangeC = (rangeX / 2)
        else:
            rangeC = rangeX / 2 + 1
        for mk in range(int(rangeC)):
            sizeY = NFsizeY
            sizeX = (NFsizeX/rangeX)
            #print("I m A Square",x,rangeX,mk,rangeC)
            self.DrawLinePatternOnFillete(x,y,sizeX,sizeY,PatColor)
            x += 2
            mk += 2

    def MakesHorizontalLinePatternOnFillete(self):
        x,y,NFsizeX,NFsizeY = self.Filletes[-1]
        rangeX = NFsizeX / (self.largTela/self.divLarg)
        rangeY = NFsizeY / (self.altTela/self.divAlt)
        PatColor = self.CorPattern

        if rangeY % 2 == 0:
            rangeC = (rangeY / 2)
        else:
            rangeC = rangeY / 2 + 1
        for mk in range(int(rangeC)):
            sizeY = NFsizeY/rangeY
            sizeX = NFsizeX
            #print("I m A Square",x,rangeY,mk,rangeC)
            self.DrawLinePatternOnFillete(x,y,sizeX,sizeY,PatColor)
            y += 2
            mk += 2

    def MakesGridonFillete(self):
        x,y,sizeX,sizeY = self.Filletes[-1]
        lineStroke = 5
        nx = int(sizeX/(self.largTela/self.divLarg))
        ny = int(sizeY/(self.altTela/self.divAlt))
        qx = self.largTela/self.divLarg
        qy = self.altTela/self.divAlt
        realX = x * qx
        realY = y * qy

        PatColor = self.CorPattern
    
            #draw Horizontal Lines
        for s in range(nx-1):
            s += 1
            pos1 = realX + (qx*s) - (lineStroke/2) , realY
            pos2 = realX + (qx*s) + (lineStroke/2), realY
            pos3 = realX + (qx*s) - (lineStroke/2) , realY + sizeY
            pos4 = realX + (qx*s) + (lineStroke/2) , realY + sizeY

            pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos4,pos3))
        #draw Vertical Lines
        for t in range(ny-1):
            t += 1
            pos1 = realX , realY + (qy*t) - (lineStroke/2)
            pos2 = realX , realY + (qy*t) + (lineStroke/2)
            pos3 = realX + sizeX, realY + (qy*t) - (lineStroke/2)
            pos4 = realX + sizeX, realY + (qy*t) + (lineStroke/2)

            pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos4,pos3))

    def DrawLinePatternOnFillete(self,x,y,sizeX,sizeY,PatColor):
        pygame.draw.rect(self.screen,PatColor,((self.largTela/self.divLarg)*x,((self.altTela/self.divAlt)*y),sizeX,sizeY))

    def MakesStairsonFillete(self):
        x,y,sizeX,sizeY = self.Filletes[-1]
        PatColor = self.CorPattern
        yNumber = int(sizeY / (self.altTela/self.divAlt))
        xNumber = int(sizeX / (self.largTela/self.divLarg))
        a = 0
        e = 0

        if yNumber >= xNumber:
            for a in range(yNumber):
                #print("CARRRRALHO",y+a)
                d = e
                e += 1
                for n in range(xNumber-d):
                    self.QuadradosPatcolor(x+n,y+a,PatColor)
                    #print("merda",x+n,y+a)
                    n += 1        
                    a += 1
                    d += 1 
        else:
            for a in range(xNumber):
                #print("CARRRRALHO",y+a)
                d = e
                e += 1
                for n in range(yNumber-d):
                    self.QuadradosPatcolor(x+n,y+a,PatColor)
                    #print("merda",x+n,y+a)
                    n += 1        
                    a += 1
                    d += 1 
    
    def QuadradosPatcolor(self,x,y,PatColor):
        cubo = pygame.draw.rect(self.screen,PatColor,((self.largTela/self.divLarg)*x,((self.altTela/self.divAlt)*y),self.largTela/self.divLarg,self.altTela/self.divAlt))

    def MakesPatternQuadradosOnFillete(self):
        x,y,sizeX,sizeY = self.Filletes[-1]
        px = x + 1
        nx = int(sizeX/(self.largTela/self.divLarg))
        ny = int(sizeY/(self.altTela/self.divAlt))
        PatColor = self.CorPattern

        for s in range(0,ny):
            for u in range(0,nx,2):
                if s % 2 == 0:
                    self.QuadradosPatcolor(x+u,y+s,PatColor)
                    #print("SQUARE ",x+u,y+s," is on",nx+x)
                elif s % 2 != 0 and (px+u)>=(nx+x) and (px+u) != (self.altTela/self.divAlt):
                    print()
                elif s % 2 != 0:
                    self.QuadradosPatcolor(px+u,y+s,PatColor)
                    #print("SQUARE ",px+u,y+s," is on",nx+x)




    def MakesCircle(self,center,rad,Patcolor):
        pygame.draw.circle(self.screen,Patcolor,center,rad)
        
        #print("IT MAKES CIRCLES")


    def Line(self,LineX,LineY,RealDirectionX,RealDirectionY,PepeCor):
        cubo = pygame.draw.rect(self.screen,PepeCor,((self.largTela/self.divLarg)*LineX,((self.altTela/self.divAlt)*LineY),RealDirectionX,RealDirectionY))
        


    def MakesTriangles(self,pos1,pos2,pos3,CorPattern):
        Patcolor = CorPattern

        pygame.draw.polygon(self.screen,Patcolor,(pos1,pos2,pos3))
        
        #print("IT MAKES TRIANGLES")

    def MakesTrianglesPattern(self,pos1,pos2,pos3,PatColor):
        pygame.draw.polygon(self.screen,PatColor,(pos1,pos2,pos3))
        
        #print("IT MAKES TRIANGLES")





#   def DrawPattern(self):
#         ### PEPESAI can choose pattern here
#       if self.ShapeComand == "c":
#           patrao.MakesCirclesOnFillete()         
#           
#           ShapeComandHolder.append(ShapeComand)
#       elif self.ShapeComand == "cp":
#           MakesCirclesPatternOnFillete(self,CorPattern)      
#           
#           ShapeComandHolder.append(ShapeComand)
#       elif self.ShapeComand == "t":
#           MakesTriangleOnFillete(self,CorPattern)               
#           
#       elif self.ShapeComand == "tp":
#           MakesTrianglePatternOnFillete(self,CorPattern)         
#           
#           ShapeComandHolder.append(ShapeComand)
#       elif self.ShapeComand == "vlp":
#           MakesVerticalLinePatternOnFillete(self,CorPattern)     
#           
#           ShapeComandHolder.append(ShapeComand)
#       elif self.ShapeComand == "hlp":
#           MakesHorizontalLinePatternOnFillete(self,CorPattern)   
#           
#           ShapeComandHolder.append(ShapeComand)
#       elif ShapeComand == "pq":
#           MakesPatternQuadradosOnFillete(self,CorPattern)        
#           
#           ShapeComandHolder.append(ShapeComand)
#       elif self.ShapeComand == "st":
#           MakesStairsonFillete(self,CorPattern)                  
#           
#           ShapeComandHolder.append(ShapeComand)
#       elif self.ShapeComand == "gr":
#           MakesGridonFillete(self,CorPattern)                  
#           
#           ShapeComandHolder.append(ShapeComand)
#       elif self.ShapeComand == "l":
#           MakesLosangleFillete(self,CorPattern)                  
#           
#       elif self.ShapeComand == "lp":
#           MakesLosanglePatternFillete(self,CorPattern)                  
#           
#           ShapeComandHolder.append(ShapeComand)
#       elif self.ShapeComand == "s":                    
#           MakeSetas(self,CorPattern)
#           
#           ShapeComandHolder.append(ShapeComand)
#       elif self.ShapeComand == "tgp":                    
#           MakesTriangleGridPatternFillete(self,CorPattern)
#           
#           ShapeComandHolder.append(ShapeComand)
#       elif self.ShapeComand == "dl":                    
#           MakesDistortLosanglesPatternFillete(self,CorPattern)
#           
#           ShapeComandHolder.append(ShapeComand)
#       elif self.ShapeComand == "45":
#           Makes45gLinesPatternFillete(self,CorPattern)                    
#           
#           ShapeComandHolder.append(ShapeComand)
#       elif self.ShapeComand == "zz":
#           MakesZigZagPatternFillete(self,CorPattern)                    
#           
#           ShapeComandHolder.append(ShapeComand)
#       else:
#           print("You did nothing BITCH")



