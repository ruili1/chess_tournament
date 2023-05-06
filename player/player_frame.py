import tkinter as tk
from tkinter import ttk
from entry_frame import EntryFrame
from player.player import Player
from player.player_dao import PlayerDao
from person.person import Person
from person.person_dao import PersonDao

class PlayerFrame(EntryFrame):
    def __init__(self, parent):
        super().__init__(parent)

        #title & buttons
        frm_title = tk.Frame(master=self, borderwidth=1)
        frm_title.rowconfigure(0, minsize=50, weight=1)
        frm_title.columnconfigure(0, minsize=500, weight=2)
        frm_title.columnconfigure([1,2,3], weight=1)
        lbl_title = tk.Label(master=frm_title, text="Player", font=("Courier", 22))
        lbl_title.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        btn_read = tk.Button(master=frm_title, text=" Show ")
        btn_read.grid(row=0, column=1, padx=10, pady=10)
        btn_add = tk.Button(master=frm_title, text="   Add   ")
        btn_add.grid(row=0, column=2, padx=10, pady=10)
        btn_update = tk.Button(master=frm_title, text=" Update ")
        btn_update.grid(row=0, column=3, padx=10, pady=10)
        btn_delete = tk.Button(master=frm_title, text=" Delete ")
        btn_delete.grid(row=0, column=4, padx=10, pady=10)
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
        frm_id.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        #rating
        frm_rating = tk.Frame(master=frm_panel)
        lbl_rating = tk.Label(master=frm_rating, text="Rating: (*)", font=("Courier", 14))
        self.rating = tk.IntVar()
        ent_rating = tk.Entry(master=frm_rating, textvariable=self.rating)
        lbl_rating.grid(row=0, column=0, sticky="w")
        ent_rating.grid(row=1, column=0, sticky="w")
        frm_rating.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        #rating_level
        frm_rating_level = tk.Frame(master=frm_panel)
        lbl_rating_level = tk.Label(master=frm_rating_level, text="Rating Lvel:", font=("Courier", 14))
        self.ratingLevel = tk.IntVar()
        ent_rating_level = tk.Entry(master=frm_rating_level, textvariable=self.ratingLevel)
        lbl_rating_level.grid(row=0, column=0, sticky="w")
        ent_rating_level.grid(row=1, column=0, sticky="w")
        frm_rating_level.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        #person table
        frm_person = tk.Frame(master=frm_panel)
        lbl_name = tk.Label(master=frm_person, text="Search Person by Name:", font=("Courier", 14))
        self.name = tk.StringVar()
        ent_name = tk.Entry(master=frm_person, textvariable=self.name)
        btn_search = tk.Button(master=frm_person, text=" Search ")
        lbl_name.grid(row=0, column=0, sticky="w", columnspan=2)
        ent_name.grid(row=1, column=0, sticky="w")
        btn_search.grid(row=1, column=1, sticky="w")
        btn_search.bind("<Button-1>", self.handle_search_person)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview.Heading', background="lightgrey")
        cols = ("Person ID", "Firstname", "Lastname", "Email")
        colIdx = 1
        self.person_tree = ttk.Treeview(frm_person, columns=cols, show="headings", height=20)
        for col in cols:
            self.person_tree.column("# "+str(colIdx), anchor=tk.W, stretch=tk.NO, width=138)
            self.person_tree.heading(col, text=col)
            colIdx = colIdx + 1
        self.person_tree.grid(row=2, column=0, columnspan=2, sticky="ew")
        self.person_tree.bind("<ButtonRelease-1>", self.click_person)
        frm_person.grid(row=2, column=3, rowspan=3, padx=10, pady=10, sticky="we")

        #player table
        pcols = ("Person ID", "Rating", "Rating Level")
        pcolIdx = 1
        self.player_tree = ttk.Treeview(frm_panel, columns=pcols, show="headings", height=20)
        for col in pcols:
            self.player_tree.column("# "+str(pcolIdx), anchor=tk.W, stretch=tk.NO, width=138)
            self.player_tree.heading(col, text=col)
            pcolIdx = pcolIdx + 1
        self.player_tree.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        self.player_tree.bind("<ButtonRelease-1>", self.click_player)

        frm_panel.pack(fill=tk.BOTH)

        self.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    def get_player(self):
        player = Player(self.id.get(), self.rating.get(), self.ratingLevel.get())
        return player
        
    def click_person(self, event):
        for selected_item in self.person_tree.selection():
            item = self.person_tree.item(selected_item)
            person = item["values"]
            self.id.set(person[0])

    def click_player(self, event):
        for selected_item in self.player_tree.selection():
            item = self.player_tree.item(selected_item)
            player = item["values"]
            self.id.set(player[0])
            self.rating.set(player[1])
            self.ratingLevel.set(player[2])

    def handle_read(self, event):
        for row in self.player_tree.get_children():
            self.player_tree.delete(row)
        playerDao = PlayerDao()
        players = playerDao.get_players()
        for player in players:
            self.player_tree.insert("", "end", values=(player.personId, player.rating, player.ratingLevel))
        
    def handle_read_old(self, event):
        playerDao = PlayerDao()
        player = playerDao.read_player(self.id.get())
        self.id.set(player.personId)
        self.rating.set(player.rating)
        self.ratingLevel.set(player.ratingLevel)

    def handle_search_person(self, event):
        for row in self.person_tree.get_children():
            self.person_tree.delete(row)
        personDao = PersonDao()
        persons = personDao.get_persons_by_name(self.name.get())
        for person in persons:
            self.person_tree.insert("", "end", values=(person.personId, person.firstName, person.lastName, person.emailAddress))
            
    def handle_add(self, event):
        player = self.get_player()
        playerDao = PlayerDao()
        playerDao.insert_player(player)
        self.id.set(player.personId)
        self.status.set("Player added successfully!")
        self.handle_read(event)

    def handle_update(self, event):
        player = self.get_player()
        playerDao = PlayerDao()
        playerDao.update_player(player)
        self.status.set("Player updated successfully!")
        self.handle_read(event)

    def handle_delete(self, event):
        playerDao = PlayerDao()
        personId = self.id.get()
        playerDao.delete_player(personId)
        self.id.set(0)
        self.rating.set(0)
        self.ratingLevel.set(0)
        self.status.set("Player deleted successfully for ID: %s!" % personId)
        self.handle_read(event)