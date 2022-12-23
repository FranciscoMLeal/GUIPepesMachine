import tkinter as tk

class colorlabels():
    def start(window, FinalPepeColors):
        color_label0 = tk.Label(window, bg=FinalPepeColors[0], height=1, width=23)
        color_label0.grid(row=3 + 0, column=1, sticky='W')
        color_label02 = tk.Label(window, bg=FinalPepeColors[0], height=1, width=23)
        color_label02.grid(row=3 + 0, column=2, sticky='W')

        color_label1 = tk.Label(window, bg=FinalPepeColors[1], height=1, width=23)
        color_label1.grid(row=3 + 1, column=1, sticky='W')
        color_label12 = tk.Label(window, bg=FinalPepeColors[1], height=1, width=23)
        color_label12.grid(row=3 + 1, column=2, sticky='W')

        color_label2 = tk.Label(window, bg=FinalPepeColors[2], height=1, width=23)
        color_label2.grid(row=3 + 2, column=1, sticky='W')
        color_label22 = tk.Label(window, bg=FinalPepeColors[2], height=1, width=23)
        color_label22.grid(row=3 + 2, column=2, sticky='W')

        color_label3 = tk.Label(window, bg=FinalPepeColors[3], height=1, width=23)
        color_label3.grid(row=3 + 3, column=1, sticky='W')
        color_label32 = tk.Label(window, bg=FinalPepeColors[3], height=1, width=23)
        color_label32.grid(row=3 + 3, column=2, sticky='W')

        color_label4 = tk.Label(window, bg=FinalPepeColors[4], height=1, width=23)
        color_label4.grid(row=3 + 4, column=1, sticky='W')
        color_label42 = tk.Label(window, bg=FinalPepeColors[4], height=1, width=23)
        color_label42.grid(row=3 + 4, column=2, sticky='W')

        color_label5 = tk.Label(window, bg=FinalPepeColors[5], height=1, width=23)
        color_label5.grid(row=3 + 5, column=1, sticky='W')
        color_label52 = tk.Label(window, bg=FinalPepeColors[5], height=1, width=23)
        color_label52.grid(row=3 + 5, column=2, sticky='W')
        
    def update(window, colorlabel1, colorlabel2, newcolor):
        colorlabel1.configure(bg=newcolor)
        colorlabel2.configure(bg=newcolor)