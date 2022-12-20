import tkinter as tk
import tkinter.colorchooser as colorchooser
import pygame
import random
from PepePatterns import PatternStyles

Filletes = []
FilletesCor = []    
PatColorHolder = []
CorFundoHolder = ["#000000","#000000"]
CorPatternHolder = ["#000000","#000000"]
FinalPepeColors = ["#F5E2AA", "#F2C546", "#DC7648", "#E9B8CE", "#83C1CE", "#5A72EC", "#3164A6", "#D65267", "#0C0103"]
ADN = []
ShapeComandHolder = ["tt"]
ShapeComandList = ["gr","pq","l","lp","dl","s","cp","t","tp","tgp","zz","vlp","hlp","45","lil","pepes"]
ShapeComandSquaresList = ["c","st","gr","pq","cic","l","lp","dl","s","cp","t","tp","tgp","zz","vlp","hlp","45","lil","sqi","pepes"] ## "c","cic,"st","sqi" PATTERNS MISSING HERE
choosePat = False


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
    def __init__(self,CorFundo,CorPattern,PepeQuad1,PepeQuad2,ShapeComand,largTela,altTela):
        self.CorFundo = CorFundo
        self.CorPattern = CorPattern
        self.FirstX,self.FirstY = PepeQuad1
        self.SecX,self.SecY = PepeQuad2
        self.ShapeComand = ShapeComand
        self.altTela = altTela
        self.largTela = largTela
        self.divAlt = int((altTela/20)/2)  
        self.divLarg = int((largTela/20)/2)      
        self.screen = pygame.display.set_mode((largTela, altTela))

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
            
        self.RealDirectionX = self.SizeX * (self.largTela/self.divLarg)
        self.RealDirectionY = self.SizeY * (self.altTela/self.divAlt)

        ### Transforms Square Fillettes Patterns in circles and Stairs
        if self.SizeX == self.SizeY and choosePat == False:
            self.ShapeComand = random.choice(ShapeComandSquaresList)
            while self.ShapeComand == ShapeComandHolder[-1]:
                self.ShapeComand = random.choice(ShapeComandSquaresList)
        Filletes.append((self.FirstX,self.FirstY,self.RealDirectionX,self.RealDirectionY))

        pygame.draw.rect(self.screen,self.CorFundo,((self.largTela/self.divLarg)*self.FirstX,((self.altTela/self.divAlt)*self.FirstY),self.RealDirectionX,self.RealDirectionY))
        pygame.display.flip()
        self.DrawPattern()



    ####READS SHAPECOMAND AND DRAWS PATTERNS

    def DrawPattern(self):
        patternEssencials = []
        patternEssencials = [self.divLarg,self.divAlt,self.largTela,self.altTela,self.screen]
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
    def __init__(self,largTela,altTela):
        self.altTela = altTela
        self.largTela = largTela
        self.divAlt = int((altTela/20)/2)  
        self.divLarg = int((largTela/20)/2) 
        self.RandomNum = [2,3,4,5]
        self.Xpoints = []
        self.start()
        
    def start(self):
        x = 0
        while x < self.divLarg:
            self.Xpoints.append(x)
            NewNum = random.choice(self.RandomNum) ### PEPESAI COULD MESS AROUND HERE
            x = x + NewNum
        self.Xpoints.append(self.divLarg) # adds last point of grid
        self.rowNumber = len(self.Xpoints)
        
        a = 0
        while a < self.rowNumber-1:
            a = a + 1
            self.Ypoints = []
            y = 0
            while y < self.divAlt:
                self.Ypoints.append(y)
                pygame.display.flip
                NewNum = random.choice(self.RandomNum) ### PEPESAI COULD MESS AROUND HERE
                if y + NewNum > self.divAlt:   ### condition for not going out of the canvas in y direction
                    NewNum = self.divAlt - y
                NewPepe = PepeAI()
                newPepitos = PepeDrawer(NewPepe.colorFundo,NewPepe.colorPattern,(self.Xpoints[a-1],y),(self.Xpoints[a],y+NewNum),NewPepe.ShapeComand,self.largTela,self.altTela)
                newPepitos.startbyFilette()
                ADN.append((NewPepe.colorFundo,NewPepe.colorPattern,(self.Xpoints[a-1],y),(self.Xpoints[a],y+NewNum),newPepitos.ShapeComand))
                ### Save Here The Pepe Reference Coordinates
                ###
                y = y + NewNum
            print(self.Xpoints,self.Ypoints) 


class GridGenerator:    
    def __init__(self,largTela,altTela):
        self.background_colour = (255,255,255)
        self.screen = pygame.display.set_mode((largTela, altTela))
        self.name = pygame.display.set_caption('RLBB')
        self.screen.fill(self.background_colour)
        self.altTela = altTela
        self.largTela = largTela
        self.divAlt = int((altTela/20)/2)  
        self.divLarg = int((largTela/20)/2) 
        

    def draw(self):    
        for y in range(self.divAlt):
            for x in range(self.divLarg):
                self.PatColor = random.choice(FinalPepeColors)
                imaa = pygame.draw.rect(self.screen,self.PatColor,((self.largTela/self.divLarg)*x,((self.altTela/self.divAlt)*y),self.largTela/self.divLarg,self.altTela/self.divAlt))
                x+=1
            x=0
            y+=1
        pygame.display.flip()   



# Create the main window
window = tk.Tk()

# Set the window title
window.title("PepeMachine GUI")

# Create a label for the width text box
width_label = tk.Label(text="Width:")
width_label.pack()

# Create a text box for the width value
width_text = tk.Entry()
width_text.insert(0, "500")
width_text.pack()

# Create a label for the height text box
height_label = tk.Label(text="Height:")
height_label.pack()

# Create a text box for the height value
height_text = tk.Entry()
height_text.insert(0, "500")
height_text.pack()

# Create a button to start the StartPepeFunction
def start_pepe_function():
  # Get the width and height values from the text boxes
  width = int(width_text.get())
  height = int(height_text.get())

  StartPepeFunction(width, height)
  

start_button = tk.Button(text="Start", command=start_pepe_function)
start_button.pack()

# Colors
x = 0
while x < len(FinalPepeColors):
    color_label = tk.Label(window, bg=FinalPepeColors[x], height=1, width=22)
    x = x + 1
    color_label.pack()






# Create a label for the controller
#controller_label = tk.Label(text="Number of colors:")
#controller_label.pack()

# Create a drop-down menu for the controller
# The options are the numbers from 5 to 15
#controller_options = [str(i) for i in range(5, 16)]
#controller_var = tk.StringVar(window)
#controller_var.set(controller_options[0])  # Set the default option
#controller_menu = tk.OptionMenu(window, controller_var, *controller_options)
#controller_menu.pack()





#def choose_color(color_label):
#  # Open the color picker and get the chosen color
#  chosen_color = colorchooser.askcolor()[1]
#
#  # Set the background color of the color label to the chosen color
#  color_label.config(bg=chosen_color)
#
#
#
#
#
#
#def start_colors():
#    colornumb = int(controller_var.get())
#    x = 0
#    color_window = tk.Toplevel()
#
#  # Create the color picker buttons and color labels
#    while x < colornumb:
#        button1 = tk.Button(color_window, text=FinalPepeColors[x], command=lambda: choose_color(label1))
#        label1 = tk.Label(color_window, width=5, height=5)
#        button1.pack()
#        label1.pack()
#        x = x + 1
    
    #button1 = tk.Button(color_window, text="Choose Color 1", command=lambda: choose_color(label1))
    #label1 = tk.Label(color_window, width=5, height=5)
    #button2 = tk.Button(color_window, text="Choose Color 2", command=lambda: choose_color(label2))
    #label2 = tk.Label(color_window, width=5, height=5)
    #button3 = tk.Button(color_window, text="Choose Color 3", command=lambda: choose_color(label3))
    #label3 = tk.Label(color_window, width=5, height=5)
    #
    #button1.pack()
    #label1.pack()
    #button2.pack()
    #label2.pack()
    #button3.pack()
    #label3.pack()

#start_colors_button = tk.Button(text="Start Colors", command=start_colors)
#start_colors_button.pack()


# Run the main loop
window.mainloop()
