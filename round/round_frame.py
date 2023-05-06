import tkinter as tk
from tkinter import ttk
from entry_frame import EntryFrame
from round.round import Round
from round.round_dao import RoundDao

class RoundFrame(EntryFrame):
    def __init__(self, parent):
        super().__init__(parent)

        #title & buttons
        frm_title = tk.Frame(master=self, borderwidth=1)
        frm_title.rowconfigure(0, minsize=50, weight=1)
        frm_title.columnconfigure(0, minsize=500, weight=2)
        frm_title.columnconfigure([1,2,3], weight=1)
        lbl_title = tk.Label(master=frm_title, text="Round", font=("Courier", 22))
        lbl_title.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        btn_read = tk.Button(master=frm_title, text=" Search ")
        btn_read.grid(row=0, column=1, padx=10, pady=10, sticky="e")
        btn_add = tk.Button(master=frm_title, text="   Add   ")
        btn_add.grid(row=0, column=2, padx=10, pady=10, sticky="e")
        btn_update = tk.Button(master=frm_title, text=" Update ")
        btn_update.grid(row=0, column=3, padx=10, pady=10, sticky="e")
        btn_delete = tk.Button(master=frm_title, text=" Delete ")
        btn_delete.grid(row=0, column=4, padx=10, pady=10, sticky="e")
        frm_title.pack(fill=tk.BOTH)

        btn_read.bind("<Button-1>", self.handle_read)
        btn_add.bind("<Button-1>", self.handle_add)
        btn_update.bind("<Button-1>", self.handle_update)
        btn_delete.bind("<Button-1>", self.handle_delete)

        #entry panel
        frm_panel = tk.Frame(master=self)
        frm_panel.rowconfigure([0, 1, 2, 3], minsize=20, weight=1)
        frm_panel.columnconfigure([0, 1, 2], minsize=100, weight=1)

        #status
        self.status = tk.StringVar()
        lbl_status = tk.Label(master=frm_panel, textvariable=self.status, fg="#f00", font=("Courier", 16))
        lbl_status.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="w")

        #id field
        frm_id = tk.Frame(master=frm_panel)
        lbl_id = tk.Label(master=frm_id, text="ID:", font=("Courier", 14, "underline"))
        self.id = tk.IntVar()
        ent_id = tk.Entry(master=frm_id, textvariable=self.id)
        lbl_id.grid(row=0, column=0, sticky="w")
        ent_id.grid(row=1, column=0, sticky="w")
        frm_id.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        #tournament
        frm_tournament = tk.Frame(master=frm_panel)
        lbl_tournament = tk.Label(master=frm_tournament, text="Tournament:", font=("Courier", 14))
        self.tournamentId = tk.IntVar()
        ent_tournament = tk.Entry(master=frm_tournament, textvariable=self.tournamentId)
        lbl_tournament.grid(row=0, column=0, sticky="w")
        ent_tournament.grid(row=1, column=0, sticky="w")
        frm_tournament.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        #start time
        frm_start_time = tk.Frame(master=frm_panel)
        lbl_start_time = tk.Label(master=frm_start_time, text="Start Time: (*)", font=("Courier", 14))
        self.startTime = tk.StringVar()
        ent_start_time = tk.Entry(master=frm_start_time, textvariable=self.startTime)
        lbl_start_time.grid(row=0, column=0, sticky="w")
        ent_start_time.grid(row=1, column=0, sticky="w")
        frm_start_time.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        #rating level
        frm_rating_level = tk.Frame(master=frm_panel)
        lbl_rating_level = tk.Label(master=frm_rating_level, text="Rating Level: (*)", font=("Courier", 14))
        self.ratingLevel = tk.IntVar()
        ent_rating_level = tk.Entry(master=frm_rating_level, textvariable=self.ratingLevel)
        lbl_rating_level.grid(row=0, column=0, sticky="w")
        ent_rating_level.grid(row=1, column=0, sticky="w")
        frm_rating_level.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        
        frm_panel.pack(fill=tk.BOTH)

        self.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    def get_round(self):
        round = Round(self.id.get(), self.tournamentId.get(), self.startTime.get(), self.ratingLevel.get())
        return round
        
    def handle_read(self, event):
        roundDao = RoundDao()
        round = roundDao.read_round(self.id.get())
        self.id.set(round.roundId)
        self.tournamentId.set(round.tournamentId)
        self.startTime.set(round.startTime)
        self.ratingLevel.set(round.ratingLevel)

    def handle_add(self, event):
        round = self.get_round()
        roundDao = RoundDao()
        roundDao.insert_round(round)
        self.id.set(round.roundId)
        self.status.set("Round added successfully!")


    def handle_update(self, event):
        round = self.get_round()
        roundDao = RoundDao()
        roundDao.update_round(round)
        self.status.set("Round updated successfully!")

    def handle_delete(self, event):
        roundDao = RoundDao()
        roundId = self.id.get()
        roundDao.delete_round(roundId)
        self.id.set(0)
        self.tournamentId.set(0)
        self.startTime.set("")
        self.ratingLevel.set(0)
        self.status.set("Round deleted successfully for ID: %s!" % roundId)