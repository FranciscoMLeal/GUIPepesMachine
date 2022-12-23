import tkinter as tk
import tkinter.colorchooser as colorchooser


FinalPepeColors = ["#F5E2AA", "#F2C546", "#DC7648", "#E9B8CE", "#83C1CE", "#5A72EC"]

Color1 = FinalPepeColors[0]
Color2 = FinalPepeColors[1]
Color3 = FinalPepeColors[2]
Color4 = FinalPepeColors[3]
Color5 = FinalPepeColors[4]
Color6 = FinalPepeColors[5]

class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Color Picker")

        # Create the color picker button
        
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
        self.print_button = tk.Button(self, text="Print Color", command=self.print_color)

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

# Create the main window and run the Tkinter event loop
# main_window = MainWindow()
# main_window.mainloop()
