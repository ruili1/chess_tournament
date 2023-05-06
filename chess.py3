import tkinter as tk
from main_window import MainWindow

def donothing():
    x = 0

root = tk.Tk()

root.title("Chess Tournament Management Systme")
#window.iconbitmap("..\chess.svg")
root.geometry("1600x1200")

window = MainWindow(root)

# main menu
menubar = tk.Menu(root)
fileMenu = tk.Menu(menubar, tearoff=0)
fileMenu.add_command(label="Home", command=lambda:window.showFrame(0))
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=fileMenu)

peopleMenu = tk.Menu(menubar, tearoff=0)
peopleMenu.add_command(label="Person", command=lambda:window.showFrame(1))
peopleMenu.add_command(label="Player", command=lambda:window.showFrame(2))
peopleMenu.add_command(label="Worker", comman=lambda:window.showFrame(3))
peopleMenu.add_command(label="Team", command=lambda:window.showFrame(4))
menubar.add_cascade(label="People", menu=peopleMenu)

gameMenu = tk.Menu(menubar, tearoff=0)
gameMenu.add_command(label="Tournament", command=lambda:window.showFrame(5))
# gameMenu.add_command(label="Round", command=lambda:window.showFrame(6))
# gameMenu.add_command(label="Game", command=lambda:window.showFrame(7))
menubar.add_cascade(label="Tournament", menu=gameMenu)

helpMenu = tk.Menu(menubar, tearoff=0)
helpMenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpMenu)

root.config(menu=menubar)       

#bottom
frm_bottom = tk.Frame(master=root)
frm_bottom.rowconfigure(0, minsize=50, weight=1)
lbl_cpright = tk.Label(master=frm_bottom, text="@Copyright Rui Li 2023 - 2024", justify=tk.RIGHT)
lbl_cpright.grid(row=0, column=0, sticky="e")
frm_bottom.pack(fill=tk.BOTH)

root.mainloop()

