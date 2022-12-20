import tkinter as tk

def on_hover(event):
  # Change the text of the label to "Hovered" when the mouse hovers over the label
  label.config(text="Hovered")

def on_click(event):
  # Change the text of the label to "Clicked" when the label is clicked
  label.config(text="Clicked")

# Create the main window
root = tk.Tk()

# Create the label and bind the mouse events to the callback functions
label = tk.Label(root, text="Label")
label.bind("<Enter>", on_hover)
label.bind("<Button-1>", on_click)

# Pack the label into the main window and run the main loop
label.pack()
root.mainloop()
