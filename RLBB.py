from os import write, replace
from typing import Pattern, Text
import pygame,sys
import random
from PepePatterns import PatternStyles
from datetime import datetime
import babypepes as bbpp
import babypepesCanvassize as CanvasSize
import importlib

canIgoback = False
canIgobackintoFuture = False
gofoward = True

isdrawn = 0
largTela = int(input("largura da tela em cm:")) 
# altura da tela
altTela = int(input("altura da tela em cm:"))
# Divisores
divLarg = int((largTela/20)/2)    #int(input("Numero de lados:"))
if divLarg <=5:
    divLarg = 6
divAlt = int((altTela/20)/2)      #int(input("Numero de pisos:"))
x = 0
y = 0
steps = 0
cc = 1
cr = 1
PepeQuad = [(0,0),(1,1),(2,2)]
Filletes = []
FilletesCor = []    
PatColorHolder = []
CorFundoHolder = ["#000000","#000000"]
CorPatternHolder = ["#000000","#000000"]
ShapeComandHolder = ["tt"]
ShapeComandList = ["gr","pq","l","lp","dl","s","cp","t","tp","tgp","zz","vlp","hlp","45","lil","pepes"]
ShapeComandSquaresList = ["c","st","gr","pq","cic","l","lp","dl","s","cp","t","tp","tgp","zz","vlp","hlp","45","lil","sqi","pepes"] ## "c","cic,"st","sqi" PATTERNS MISSING HERE
Ypoints = []
points = []

#SavePepes = []
choosePat = False

screen = pygame.display.set_mode((largTela, altTela))
RandomNum = [2,3,4,5]

ADN = []

patternEssencials = [divLarg,divAlt,largTela,altTela,screen]


FinalPepeColors = ["#F5E2AA", "#F2C546", "#DC7648", "#E9B8CE", "#83C1CE", "#5A72EC", "#3164A6", "#D65267", "#0C0103"]
#FinalPepeColors = ["#0A2463","#4200DC","#690AAE","#D8315B","#F74A84","#A9FDAC","#32A287"]
#CoresPattern = ["#D8315B","#F74A84","#66E88F","#0A2463","#4200DC",]

AdnRegistry  = open("babypepes.py", "a+")
CanvasRegistry  = open("babypepesCanvassize.py", "a+")

SavedPepe = []









class GridGenerator:    
    def __init__(self):
        self.background_colour = (255,255,255)
        self.screen = pygame.display.set_mode((largTela, altTela))
        self.name = pygame.display.set_caption('RLBB')
        self.screen.fill(self.background_colour)
        

    def draw(self):    
        for y in range(divAlt):
            for x in range(divLarg):
                self.PatColor = random.choice(FinalPepeColors)
                self.imaa = pygame.draw.rect(self.screen,self.PatColor,((largTela/divLarg)*x,((altTela/divAlt)*y),largTela/divLarg,altTela/divAlt))
                x+=1
            x=0
            y+=1
        pygame.display.flip()   



        

class PepeAI:
    def __init__(self):
        self.GetColors()
        self.GetPatternShape()

    def GetColors(self):
        self.pepeCores = FinalPepeColors
        self.colorFundo = random.choice(self.pepeCores)
        self.colorPattern = random.choice(self.pepeCores)

        #print("FUNDO COLOR HOLDER =", CorFundoHolder[-1],"NEW FUNDO COLOR =",self.colorFundo,"OLD PATTERN COLOR =",CorPatternHolder[-1],"NEW PATTERN COLOR",self.colorPattern )

        while self.colorPattern == self.colorFundo or self.colorPattern == CorPatternHolder[-1] or self.colorFundo == CorFundoHolder[-1] or self.colorFundo == CorPatternHolder[-1] or self.colorPattern == CorFundoHolder[-1]:
            self.colorPattern = random.choice(self.pepeCores)
            self.colorFundo = random.choice(self.pepeCores)
            #print("REPEAT MODE ACTIVATED : FUNDO COLOR HOLDER =", CorFundoHolder[-1],"NEW FUNDO COLOR =",self.colorFundo,"OLD PATTERN COLOR =",CorPatternHolder[-1],"NEW PATTERN COLOR",self.colorPattern )
                
        CorFundoHolder.append(self.colorFundo)
        CorPatternHolder.append(self.colorPattern)
            
    def GetPatternShape(self):
        
        self.ShapeComand = random.choice(ShapeComandList)
        while self.ShapeComand == ShapeComandHolder[-1]:
            self.ShapeComand = random.choice(ShapeComandList)
        
        

class PepeDrawer:
    def __init__(self,CorFundo,CorPattern,PepeQuad1,PepeQuad2,ShapeComand):
        self.CorFundo = CorFundo
        self.CorPattern = CorPattern
        self.FirstX,self.FirstY = PepeQuad1
        self.SecX,self.SecY = PepeQuad2
        self.ShapeComand = ShapeComand      

        #SavePepes.append(((self.FirstX,self.FirstY),(self.SecX,self.SecY)))

    #### DRAWS FUNDOS    
    def startbyFilette(self):        
        if self.SecX < self.FirstX:
            self.SizeX = (self.FirstX - self.SecX) 
            self.FirstX = self.SecX
          
        else:
            self.SizeX = (self.SecX - self.FirstX) 
          
        if self.SecY < self.FirstY:
            self.SizeY = (self.FirstY - self.SecY) 
            self.FirstY = self.SecY
        
        else:
            self.SizeY = (self.SecY - self.FirstY)     
            
        self.RealDirectionX = self.SizeX * (largTela/divLarg)
        self.RealDirectionY = self.SizeY * (altTela/divAlt)

        ### Transforms Square Fillettes Patterns in circles and Stairs
        if self.SizeX == self.SizeY and choosePat == False:
            self.ShapeComand = random.choice(ShapeComandSquaresList)
            while self.ShapeComand == ShapeComandHolder[-1]:
                self.ShapeComand = random.choice(ShapeComandSquaresList)
        Filletes.append((self.FirstX,self.FirstY,self.RealDirectionX,self.RealDirectionY))

        pygame.draw.rect(screen,self.CorFundo,((largTela/divLarg)*self.FirstX,((altTela/divAlt)*self.FirstY),self.RealDirectionX,self.RealDirectionY))
        pygame.display.flip()
        self.DrawPattern()



    ####READS SHAPECOMAND AND DRAWS PATTERNS

    def DrawPattern(self):
        patternEssencials = []
        patternEssencials = [divLarg,divAlt,largTela,altTela,screen]
        patrao = PatternStyles(self.CorFundo,self.CorPattern,Filletes,patternEssencials,(self.FirstX,self.FirstY),(self.SecX,self.SecY))
        if self.ShapeComand == "c":
            patrao.MakesCirclesOnFillete()      
            pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "pepes":
            patrao.pepesAiSignature(FinalPepeColors)    
            pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "cic":
            patrao.MakesCirclesinCirclesOnFillete()    
            pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "cp":
            patrao.MakesCirclesPatternOnFillete(self.CorPattern)     
            pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "t":
            patrao.MakesTriangleOnFillete(self.CorPattern)               
            pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "tp":
            patrao.MakesTrianglePatternOnFillete()         
            pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "vlp":
            patrao.MakesVerticalLinePatternOnFillete()     
            pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "hlp":
            patrao.MakesHorizontalLinePatternOnFillete()   
            pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "pq":
            patrao.MakesPatternQuadradosOnFillete()        
            pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "st":
            patrao.MakesStairsonFillete()                  
            pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "gr":
            patrao.MakesGridonFillete()                  
            pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "sqi":
            patrao.MakeSquaresInsideSquares()               
            pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "lil":
            patrao.MakesLosangleInsideLosangle()                
            pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "l":
            patrao.MakesLosangleFillete()                  
            pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "lp":
            patrao.MakesLosanglePatternFillete()                  
            pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "s":                    
            patrao.MakeSetas()
            pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "tgp":                    
            patrao.MakesTriangleGridPatternFillete()
            pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "dl":                    
            patrao.MakesDistortLosanglesPatternFillete()
            pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "45":
            patrao.Makes45gLinesPatternFillete()                    
            pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "zz":
            patrao.MakesZigZagPatternFillete()                    
            pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        else:
            print("You did nothing BITCH")

    


class StartPepeFunction:
    def __init__(self):
        self.Xpoints = []
        self.start()
        
    def start(self):
        x = 0
        while x < divLarg:
            self.Xpoints.append(x)
            NewNum = random.choice(RandomNum) ### PEPESAI COULD MESS AROUND HERE
            x = x + NewNum
        self.Xpoints.append(divLarg) # adds last point of grid
        self.rowNumber = len(self.Xpoints)
        
        a = 0
        while a < self.rowNumber-1:
            a = a + 1
            self.Ypoints = []
            y = 0
            while y < divAlt:
                self.Ypoints.append(y)
                pygame.display.flip
                NewNum = random.choice(RandomNum) ### PEPESAI COULD MESS AROUND HERE
                if y + NewNum > divAlt:   ### condition for not going out of the canvas in y direction
                    NewNum = divAlt - y
                NewPepe = PepeAI()
                newPepitos = PepeDrawer(NewPepe.colorFundo,NewPepe.colorPattern,(self.Xpoints[a-1],y),(self.Xpoints[a],y+NewNum),NewPepe.ShapeComand)
                newPepitos.startbyFilette()
                ADN.append((NewPepe.colorFundo,NewPepe.colorPattern,(self.Xpoints[a-1],y),(self.Xpoints[a],y+NewNum),newPepitos.ShapeComand))
                ### Save Here The Pepe Reference Coordinates
                ###
                y = y + NewNum
            print(self.Xpoints,self.Ypoints) 

class ClicktoChangePP:
    def __init__(self,x,y):
        self.x,self.y = x,y
        NewX = divLarg
        for cc in range(divLarg):
            if self.x - (largTela/divLarg) <= (largTela/divLarg) * cc: 
                #print("point x:",cc)
                NewX -= 1

        NewY = divAlt
        for cr in range(divAlt):
            if self.y - (altTela/divAlt) <= (altTela/divAlt) * cr: 
                #print("point y:",cr)
                NewY -= 1
        print("this is your click coordinates :",NewX,NewY)


        shitter = 0
        shitterTimes = len(ADN)
        while shitter < shitterTimes:
            newPoints = ADN[shitter]
            newCorF,newCorP,(newPointX,newPointY),(SecnewPointX,SecnewPointY),newShapC = ADN[shitter]
            if newPointX <= NewX < SecnewPointX and newPointY <= NewY < SecnewPointY:
                self.DrawPattern(newPointX,newPointY,SecnewPointX,SecnewPointY,shitter)
                break
            shitter += 1
    
    def DrawPattern(self,newPointX,newPointY,SecnewPointX,SecnewPointY,shitter):
        NewPepe = PepeAI()
        if choosePat == False:   
            newPepitos = PepeDrawer(NewPepe.colorFundo,NewPepe.colorPattern,(newPointX,newPointY),(SecnewPointX,SecnewPointY),NewPepe.ShapeComand)
            newPepitos.startbyFilette()
            ADN[shitter] = NewPepe.colorFundo,NewPepe.colorPattern,(newPointX,newPointY),(SecnewPointX,SecnewPointY),newPepitos.ShapeComand

        elif choosePat == True:
            ShapeComand = input("Choose the Pattern of your desire:\nc   for Circle\ncic for Circles Inside Circles\nl   for Losangle\nlp  for Losangle Pattern\ndl  for Distort Losangle Pattern\ngr  for Grid Pattern\ns   for Setas\ncp  for Circle Pattern\nst  for Stairs\nt   for Triangle\npq  for Quadrados Pattern\ntp  for Triangle Pattern\ntgp for Triangle Grid Pattern\nzz  for Zig Zag Triangles Pattern\nvlp for Vertical Lines Pattern\nhlp for Horizontal Lines Pattern\n45  for 45 degrees Lines Pattern\nsqi for SquaresInsideSquares\nlil for Losangles Inside Losangles\n   ")
            newPepitos = PepeDrawer(NewPepe.colorFundo,NewPepe.colorPattern,(newPointX,newPointY),(SecnewPointX,SecnewPointY),ShapeComand)
            newPepitos.startbyFilette()
            ADN[shitter] = NewPepe.colorFundo,NewPepe.colorPattern,(newPointX,newPointY),(SecnewPointX,SecnewPointY),newPepitos.ShapeComand



    

class ADNprocessor:
    def __init__(self):
        print("You iniciated The Adn Processor:")

    def rewindOnePepe(self, lastPepeAdn):
        print("YOUAREHERE:")

        x = 0
        while x < len(lastPepeAdn):
                    newCorF,newCorP,(nX,nY),(sX,sY),newShapC = lastPepeAdn[x]
                    newPepitos = PepeDrawer(newCorF,newCorP,(nX,nY),(sX,sY),newShapC)
                    newPepitos.startbyFilette()
                    x += 1



    def colorChanger(self):
        x = 0
        while x < len(ADN):
            NewPepe = PepeAI()
            newCorF,newCorP,(nX,nY),(sX,sY),newShapC = ADN[x]
            newPepitos = PepeDrawer(NewPepe.colorFundo,NewPepe.colorPattern,(nX,nY),(sX,sY),newShapC)
            newPepitos.startbyFilette()
            x += 1



    def callSavedPepes(self):
        self.printSavedPepes()
        calledPepe = input("Who do Want to Call???")

        ## DRAWS SAVED CANVAS SIZE
        importlib.reload(CanvasSize)
        with open('babypepesCanvassize.py') as cs:
            if calledPepe in cs.read():
                loadCanvasSize = CanvasSize.savedPepesCanvas
                global largTela, altTela, divLarg, divAlt
                largTela, altTela, divLarg, divAlt = loadCanvasSize.get(calledPepe)
                redrawCanvas = GridGenerator()
                redrawCanvas.draw()
            else:
                print("This shit never existed before")


        ## DRAWS SAVED PEPE            
        importlib.reload(bbpp)
        with open('babypepes.py') as f:
            if calledPepe in f.read():
                newPepeLst = bbpp.savedPepes
                newAdn = newPepeLst.get(calledPepe)    
                global ADN 
                ADN = newPepeLst.get(calledPepe)
                x = 0
                while x < len(newAdn):
                    newCorF,newCorP,(nX,nY),(sX,sY),newShapC = newAdn[x]
                    newPepitos = PepeDrawer(newCorF,newCorP,(nX,nY),(sX,sY),newShapC)
                    newPepitos.startbyFilette()
                    x += 1
            else:
                print("This shit never existed before")


    def printSavedPepes(self):
        #CanvasRegistry = open("babypepesCanvassize.py", "r")
        SavedPepes = CanvasSize.savedPepesCanvas
        for x in SavedPepes:
          #stripped_line = line.strip()
          print(x)
        CanvasRegistry.close()
    

            




   
   
            
### KEYBOARD INTERACTION COMMANDS FOR FRONTRUNNING THE MACHINE ::::        

        
grid = GridGenerator()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print(steps,"steps")
      running = False
      


    elif event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
        ADN = []
        grid.draw()
        canIgoback = True
        if gofoward == False:
            if isdrawn >= 0 and isdrawn < 4:
                isdrawn += 1
            else :
                isdrawn == 0 
        gofoward = True
        
        if isdrawn == 0:
            new0 = StartPepeFunction()
            new00 = ADN
            del new0
            
            print("you print in :")
            print(isdrawn)
            
            isdrawn = 1
            
            print("you leave in :")
            print(isdrawn)

        elif isdrawn == 1:
            new1 = StartPepeFunction()
            new11 = ADN
            del new1
            
            print("you print in :")
            print(isdrawn)
            
            isdrawn = 2
            
            print("you leave in :")
            print(isdrawn)

        elif isdrawn == 2:
            new2 = StartPepeFunction()
            new22 = ADN
            del new2
            
            print("you print in :")
            print(isdrawn)
            
            isdrawn = 3
            
            print("you leave in :")
            print(isdrawn)

        elif isdrawn == 3:
            new3 = StartPepeFunction()
            new33 = ADN
            del new3
            
            print("you print in :")
            print(isdrawn)
            
            isdrawn = 4
            
            print("you leave in :")
            print(isdrawn)

        elif isdrawn == 4:
            canIgobackintoFuture = True
            new4 = StartPepeFunction()
            new44 = ADN
            del new4 
            
            print("you print in :")
            print(isdrawn)
            
            isdrawn = 0
            
            print("you leave in :")
            print(isdrawn)

        steps+=1

    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        x,y = pygame.mouse.get_pos()    
        newPepePattern = ClicktoChangePP(x,y)
    
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
        choosePat = True
        x,y = pygame.mouse.get_pos()    
        newPepePattern = ClicktoChangePP(x,y)
        choosePat = False

    # Rewind button in R
    # NOT WORKING YET    
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
        choosePat = True
        if gofoward == True:
            #gofoward = False
            if isdrawn > 0 and isdrawn <= 4:
                isdrawn -= 1
            else :
                isdrawn == 4
        if canIgoback == True:
            if isdrawn == 0 and canIgobackintoFuture == True:
                ADN = []
                ADN = new44
                Call00 = ADNprocessor()
                Call00.rewindOnePepe(new44)
                del Call00
                
                print("you print in :")
                print(isdrawn)
                
                isdrawn = 4

                print("you leave in :")
                print(isdrawn)

            elif isdrawn == 1:
                ADN = []
                ADN = new00
                Call11 = ADNprocessor()
                Call11.rewindOnePepe(new00)
                del Call11
                
                print("you print in :")
                print(isdrawn)
                
                isdrawn = 0

                print("you leave in :")
                print(isdrawn)

            elif isdrawn == 2:
                ADN = []
                ADN = new11
                Call22 = ADNprocessor()
                Call22.rewindOnePepe(new11)
                del Call22
                
                print("you print in :")
                print(isdrawn)
                
                isdrawn = 1

                print("you leave in :")
                print(isdrawn)

            elif isdrawn == 3:
                ADN = []
                ADN = new22
                Call33 = ADNprocessor()
                Call33.rewindOnePepe(new22)
                del Call33
                
                print("you print in :")
                print(isdrawn)
                
                isdrawn = 2

                print("you leave in :")
                print(isdrawn)

            elif isdrawn == 4:
                ADN = []
                ADN = new33
                Call44 = ADNprocessor()
                Call44.rewindOnePepe(new33)
                del Call44
                
                print("you print in :")
                print(isdrawn)
                
                isdrawn = 3

                print("you leave in :")
                print(isdrawn)
        if gofoward == True:
            gofoward = False
            if isdrawn >= 0 and isdrawn < 4:
                isdrawn += 1
            else :
                isdrawn == 0    
        choosePat = False

    # elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:



    # Changes IMAGE COLORS with the Adn Processor

    elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
        choosePat = True
        adnProcess = ADNprocessor()
        adnProcess.colorChanger()
        choosePat = False

    # Calls Saved Pepe

    elif event.type == pygame.KEYDOWN and event.key == pygame.K_o:
        choosePat = True
        adnProcess = ADNprocessor()
        adnProcess.callSavedPepes()
        choosePat = False


    #Saves a Pepe as PNG and as Genome
    
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:

        babyPepeName = input("Write Your Baby Pepe Name:")
        #TimeStamp = str(datetime.now())[:19]
        #TimeStampuse = list(TimeStamp)
        #TimeStampuse[16] = "m"
        #TimeStampuse[13] = "h"
        #PrintTimeStamp = "".join(TimeStampuse)
        
                        ###### FIND A WAY TO DUMP ALLSAVED PEPES IN TERMINAL ????
        ## Escreve a Canvas Size de cada BabyPepe na sua pagina apropriada
        CanvasRegistry = open("babypepesCanvassize.py", "r")

        new_file_content = ""
        for line in CanvasRegistry:
          stripped_line = line.strip()
          new_line = stripped_line.replace("}", " ")
          new_file_content += new_line +"\n"
        CanvasRegistry.close()

        CanvasRegistry = open("babypepesCanvassize.py", "w")
        CanvasRegistry.write(new_file_content)
        canvaSize = (largTela,altTela,divLarg,divAlt)
        CanvasRegistry.write(",'")
        CanvasRegistry.write(babyPepeName)
        CanvasRegistry.write("'")
        CanvasRegistry.write(" : ")
        CanvasRegistry.write(str(canvaSize))
        CanvasRegistry.write("}")
        CanvasRegistry.close()


        ## Escreve o ADN de cada BabyPepe na sua pagina apropriada
        AdnRegistry = open("babypepes.py", "r")

        new_file_content = ""
        for line in AdnRegistry:
          stripped_line = line.strip()
          new_line = stripped_line.replace("}", " ")
          new_file_content += new_line +"\n"
        AdnRegistry.close()

        AdnRegistry = open("babypepes.py", "w")
        AdnRegistry.write(new_file_content)

        AdnRegistry.write(",'")
        AdnRegistry.write(babyPepeName)
        AdnRegistry.write("'")
        AdnRegistry.write(" : ")
        AdnRegistry.write(str(ADN))
        AdnRegistry.write("}")
        AdnRegistry.close()
      
        SavedPepe = ADN
        realName = "BabyPepe (" + babyPepeName + ").png"
        pygame.image.save(screen , realName)
        print("You just created a jpg with your Pepe in your local directory named :", realName)
    
    
    # Spacebar to redraw squares

    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        grid.draw()
       
    # Press Arrows for controlling divisions number

    elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        divLarg -= 1
        if divLarg <=5:
            divLarg = 6
        grid.draw()
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        divLarg += 1
        grid.draw()
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
        divAlt -= 1
        if divAlt <= 3:
            divAlt = 4
        grid.draw()
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
        divAlt += 1
        grid.draw()









########
# CRIAR UM GUI
#   - 1 BOTAO PARA INICIALIZAR PYGAME
#   - 2 CAIXAS PARA INSERIR MEDIDAS DA PAREDE
#   - 2 CONTADORES PARA NUMERO DE DIVLARG E DIVALT
#   - 1 CONTADOR PARA NUMERO DE CORES
#       - ARRANJAR UM DISPLAY INTERACTIVO
#       - COLOR PICKER