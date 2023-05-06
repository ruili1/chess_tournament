import tkinter as tk
from PIL import ImageTk, Image
from entry_frame import EntryFrame

class HomeFrame(EntryFrame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text = "Welcome to Chess Tournament Management", font=("Courier", 22)).pack(padx=10, pady=10)
        canvas = tk.Canvas(self, width=300, height=300)
        canvas.pack(expand=True, fill=tk.BOTH)
        img = ImageTk.PhotoImage(Image.open("13710.jpg"))
        canvas.create_image(20, 20, anchor=tk.CENTER, image=img)
        self.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)