# This Code is free to development

import tkinter as tk
from tkinter import colorchooser
import os

app = tk.Tk()
app.geometry("400x210")
app.resizable(False,False)
app.title("Color Pick")
ico_path = os.path.join("color_picker.ico")
app.iconbitmap(ico_path)


def pick_color():
    rgb_color, hex_color = colorchooser.askcolor(title="Pick a Color")
    if hex_color:
        # Show values in labels
        hex_label.config(text=f"Hex: {hex_color}")
        rgb_label.config(text=f"RGB: {tuple(int(v) for v in rgb_color)}")
        color_preview.config(bg=hex_color)

# UI Elements
copyright = tk.Label(app,text="2025 Copyright JBSoftbox")
copyright.pack(pady=5,padx=5)

pick_button = tk.Button(app, text="Pick a Color", command=pick_color)
pick_button.pack(pady=20)

hex_label = tk.Label(app, text="Hex: #------")
hex_label.pack()

rgb_label = tk.Label(app, text="RGB: (---, ---, ---)")
rgb_label.pack()

color_preview = tk.Label(app, text="", width=25, height=30)
color_preview.pack(pady=10)

app.mainloop()
