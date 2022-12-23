import tkinter as tk
import tkinter.colorchooser as colorchooser
import pygame
import random
from PepePatterns import PatternStyles
import colorlabel as CL
#import ColorPicker as CP

Filletes = []
FilletesCor = []    
PatColorHolder = []
CorFundoHolder = ["#000000","#000000"]
CorPatternHolder = ["#000000","#000000"]
FinalPepeColors = ["#F5E2AA", "#F2C546", "#DC7648", "#E9B8CE", "#83C1CE", "#5A72EC"]
ADN = []
ShapeComandHolder = ["tt"]
ShapeComandList = ["gr","pq","l","lp","dl","s","cp","t","tp","tgp","zz","vlp","hlp","45","lil","pepes"]
ShapeComandSquaresList = ["c","st","gr","pq","cic","l","lp","dl","s","cp","t","tp","tgp","zz","vlp","hlp","45","lil","sqi","pepes"] ## "c","cic,"st","sqi" PATTERNS MISSING HERE
choosePat = False


#########################################
#########################################
#########################################
#########################################

class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Color Picker")

        # Create the color picker button
        Color1 = FinalPepeColors[0]
        Color2 = FinalPepeColors[1]
        Color3 = FinalPepeColors[2]
        Color4 = FinalPepeColors[3]
        Color5 = FinalPepeColors[4]
        Color6 = FinalPepeColors[5]
        
        self.color1 = Color1
        self.color_picker1 = tk.Button(self, text="Pick Color", command=self.pick_color1)
        self.color_picker1.configure(bg=Color1, fg=Color1)
        self.color_picker1.pack()
        
        self.color2 = Color2
        self.color_picker2 = tk.Button(self, text="Pick Color", command=self.pick_color2)
        self.color_picker2.configure(bg=Color2, fg=Color2)
        self.color_picker2.pack()
        
        self.color3 = Color3
        self.color_picker3 = tk.Button(self, text="Pick Color", command=self.pick_color3)
        self.color_picker3.configure(bg=Color3, fg=Color3)
        self.color_picker3.pack()
        
        self.color4 = Color4
        self.color_picker4 = tk.Button(self, text="Pick Color", command=self.pick_color4)
        self.color_picker4.configure(bg=Color4, fg=Color4)
        self.color_picker4.pack()
        
        self.color5 = Color5
        self.color_picker5 = tk.Button(self, text="Pick Color", command=self.pick_color5)
        self.color_picker5.configure(bg=Color5, fg=Color5)
        self.color_picker5.pack()
        
        self.color6 = Color6
        self.color_picker6 = tk.Button(self, text="Pick Color", command=self.pick_color6)
        self.color_picker6.configure(bg=Color6, fg=Color6)
        self.color_picker6.pack()

        # Create the Print button
        self.print_button = tk.Button(self, text="SAVE", command=self.print_color)

        # Pack the widgets
        # self.color_picker.pack()
        self.print_button.pack()

    def pick_color1(self):
        # Open the color chooser dialog
        color = colorchooser.askcolor(self.color1)[1]
        # Update the color of the color picker button
        self.color_picker1.configure(bg=color, fg=color)
        self.color = color
        
    def pick_color2(self):
        # Open the color chooser dialog
        color = colorchooser.askcolor(self.color2)[1]
        # Update the color of the color picker button
        self.color_picker2.configure(bg=color, fg=color)
        self.color = color

    def pick_color3(self):
        # Open the color chooser dialog
        color = colorchooser.askcolor(self.color3)[1]
        # Update the color of the color picker button
        self.color_picker3.configure(bg=color, fg=color)
        self.color = color
        
    def pick_color4(self):
        # Open the color chooser dialog
        color = colorchooser.askcolor(self.color4)[1]
        # Update the color of the color picker button
        self.color_picker4.configure(bg=color, fg=color)
        self.color = color
        
    def pick_color5(self):
        # Open the color chooser dialog
        color = colorchooser.askcolor(self.color5)[1]
        # Update the color of the color picker button
        self.color_picker5.configure(bg=color, fg=color)
        self.color = color
        
    def pick_color6(self):
        # Open the color chooser dialog
        color = colorchooser.askcolor(self.color6)[1]
        # Update the color of the color picker button
        self.color_picker6.configure(bg=color, fg=color)
        self.color = color
        
    def print_color(self):
        # Print the color of the color picker button
        print(self.color_picker1['bg'])
        print(self.color_picker2['bg'])
        print(self.color_picker3['bg'])
        print(self.color_picker4['bg'])
        print(self.color_picker5['bg'])
        print(self.color_picker6['bg'])
        global FinalPepeColors
        FinalPepeColors = [self.color_picker1['bg'],self.color_picker2['bg'],self.color_picker3['bg'],self.color_picker4['bg'],self.color_picker5['bg'],self.color_picker6['bg']]
        ###update here
        updatecolor = CL.colorlabels.start(window, FinalPepeColors)
        
        
        
        
#########################################
#########################################
#########################################
#########################################

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
        self.divAlt = int((altTela/35)/2)  
        self.divLarg = int((largTela/35)/2)      
        self.screen = pygame.display.set_mode((largTela, altTela))
        pygame.display.set_caption("PEPESMACHINE")


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
        self.divAlt = int((altTela/35)/2)  
        self.divLarg = int((largTela/35)/2) 
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


# Create the main window
window = tk.Tk()
pygame.init()

# Set the window title
window.title("PepeMachine GUI")

# Create a label for the width text box
width_label = tk.Label(text="Width:")
width_label.grid(row=0, column=1, sticky='W')

# Create a text box for the width value
width_text = tk.Entry()
width_text.insert(0, pygame.display.Info().current_w)
width_text.grid(row=0, column=2, sticky='W')

# Create a label for the height text box
height_label = tk.Label(text="Height:")
height_label.grid(row=1, column=1, sticky='W')

# Create a text box for the height value
height_text = tk.Entry()
height_text.insert(0, pygame.display.Info().current_h)
height_text.grid(row=1, column=2, sticky='W')

# Create a button to start the Start PepeFunction
def start_pepe_function():
  # Get the width and height values from the text boxes
  width = int(width_text.get())
  height = int(height_text.get())

  StartPepeFunction(width, height)
  
      
  

start_button = tk.Button(text="Make Pepes", command=start_pepe_function)
start_button.grid(row=2, column=1, sticky='W')


def change_colors():
    colors_window = MainWindow()
    colors_window.mainloop()
    print("Change Colors")


color_button = tk.Button(text="Change Colors", command=change_colors)
color_button.grid(row=2, column=2, sticky='W')

#def update_colors(): 
#    
#    updatecolor = CL.colorlabels.start(window, FinalPepeColors)
#
#
#updcolor_button = tk.Button(text="Update Colors", command=update_colors)
#updcolor_button.grid(row=2, column=3, sticky='W')

# Colors

makecolors = CL.colorlabels.start(window,FinalPepeColors)
#x = 0
#while x < len(FinalPepeColors):
#    color_label = tk.Label(window, bg=FinalPepeColors[x], height=1, width=23)
#    color_label.grid(row=3 + x, column=1, sticky='W')
#    color_label2 = tk.Label(window, bg=FinalPepeColors[x], height=1, width=23)
#    color_label2.grid(row=3 + x, column=2, sticky='W')
#    x = x + 1

# Run the main loop
window.mainloop()
