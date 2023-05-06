import tkinter as tk
from tkinter import ttk
from entry_frame import EntryFrame
from game.game import Game
from game.game_dao import GameDao

class GameFrame(EntryFrame):
    def __init__(self, parent):
        super().__init__(parent)

        #title & buttons
        frm_title = tk.Frame(master=self, borderwidth=1)
        frm_title.rowconfigure(0, minsize=50, weight=1)
        frm_title.columnconfigure(0, minsize=500, weight=2)
        frm_title.columnconfigure([1,2,3], weight=1)
        lbl_title = tk.Label(master=frm_title, text="Games", font=("Courier", 22))
        lbl_title.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        btn_read = tk.Button(master=frm_title, text=" Search ")
        btn_read.grid(row=0, column=1, padx=10, pady=10, sticky="e")
        btn_add = tk.Button(master=frm_title, text=" Generate ")
        btn_add.grid(row=0, column=2, padx=10, pady=10, sticky="e")
        # btn_update = tk.Button(master=frm_title, text=" Update ")
        # btn_update.grid(row=0, column=3, padx=10, pady=10, sticky="e")
        # btn_delete = tk.Button(master=frm_title, text=" Delete ")
        # btn_delete.grid(row=0, column=4, padx=10, pady=10, sticky="e")
        frm_title.pack(fill=tk.BOTH)

        btn_read.bind("<Button-1>", self.handle_read)
        btn_add.bind("<Button-1>", self.handle_generate)
        # btn_update.bind("<Button-1>", self.handle_update)
        # btn_delete.bind("<Button-1>", self.handle_delete)

        #entry panel
        frm_panel = tk.Frame(master=self)
        frm_panel.rowconfigure([0, 1, 2, 3], minsize=20, weight=1)
        frm_panel.columnconfigure([0, 1, 2], minsize=100, weight=1)

        #status
        self.status = tk.StringVar()
        lbl_status = tk.Label(master=frm_panel, textvariable=self.status, fg="#f00", font=("Courier", 16))
        lbl_status.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="w")

        #round
        frm_round = tk.Frame(master=frm_panel)
        lbl_round = tk.Label(master=frm_round, text="Round:", font=("Courier", 14))
        self.roundId = tk.IntVar()
        ent_round = tk.Entry(master=frm_round, textvariable=self.roundId)
        lbl_round.grid(row=0, column=0, sticky="w")
        ent_round.grid(row=1, column=0, sticky="w")
        frm_round.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        #team
        frm_team = tk.Frame(master=frm_panel)
        lbl_team = tk.Label(master=frm_team, text="Team:", font=("Courier", 14))
        self.teamId = tk.IntVar()
        ent_team = tk.Entry(master=frm_team, textvariable=self.teamId)
        lbl_team.grid(row=0, column=0, sticky="w")
        ent_team.grid(row=1, column=0, sticky="w")
        frm_team.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        #games table
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview.Heading', background="lightgrey")
        cols = ("Game ID", "White Player", "Black Player", "Status", "Arbiter")
        colIdx = 1
        self.tree = ttk.Treeview(frm_panel, columns=cols, show="headings", height=20)
        for col in cols:
            self.tree.column("# "+str(colIdx), anchor=tk.W, stretch=tk.NO, width=140)
            self.tree.heading(col, text=col)
            colIdx = colIdx + 1
        self.tree.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        frm_panel.pack(fill=tk.BOTH)

        self.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    def handle_read(self, event):
        pass

    def handle_generate(self, event):
        for row in self.tree.get_children():
            self.tree.delete(row)
        gameDao = GameDao()
        gameDao.generate_games(self.roundId.get(), self.teamId.get())
        self.status.set("Games generated successfully!")
        games = gameDao.get_games(self.roundId.get())
        for game in games:
            self.tree.insert("", "end", values=(game.gameId, game.whitePlayer, game.blackPlayer, game.status, game.arbiter))
        
    def handle_update(self, event):
        pass

    def handle_delete(self, event):
        pass