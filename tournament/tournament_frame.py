import tkinter as tk
from tkinter import ttk
from entry_frame import EntryFrame
from tournament.tournament import Tournament
from tournament.tournament_dao import TournamentDao
from round.round import Round
from round.round_dao import RoundDao
from game.game_view import GameView
from game.game_dao import GameDao
from team.team import Team
from team.team_dao import TeamDao

class TournamentFrame(EntryFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.id = 0

        #title & buttons
        frm_title = tk.Frame(master=self, borderwidth=1)
        frm_title.rowconfigure(0, minsize=50, weight=1)
        frm_title.columnconfigure(0, minsize=500, weight=2)
        frm_title.columnconfigure([1,2,3], weight=1)
        lbl_title = tk.Label(master=frm_title, text="Tournament", font=("Courier", 22))
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
        frm_panel.rowconfigure([0, 1, 2], minsize=20, weight=1)
        frm_panel.columnconfigure([0, 1, 2], minsize=100, weight=1)

        #status
        self.status = tk.StringVar()
        lbl_status = tk.Label(master=frm_panel, textvariable=self.status, fg="#f00", font=("Courier", 16))
        lbl_status.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="w")

        #id field
        # frm_id = tk.Frame(master=frm_panel)
        # lbl_id = tk.Label(master=frm_id, text="ID:", font=("Courier", 14, "underline"))
        # self.id = tk.IntVar()
        # ent_id = tk.Entry(master=frm_id, textvariable=self.id)
        # lbl_id.grid(row=0, column=0, sticky="w")
        # ent_id.grid(row=1, column=0, sticky="w")
        # frm_id.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        #name
        frm_name = tk.Frame(master=frm_panel)
        lbl_name = tk.Label(master=frm_name, text="Tournament Name: (*)", font=("Courier", 14))
        self.tournamentName = tk.StringVar()
        ent_name = tk.Entry(master=frm_name, textvariable=self.tournamentName)
        lbl_name.grid(row=0, column=0, sticky="w")
        ent_name.grid(row=1, column=0, sticky="w")
        frm_name.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        #address line 1
        frm_addr1 = tk.Frame(master=frm_panel)
        lbl_addr1 = tk.Label(master=frm_addr1, text="Address Line 1: (*)", font=("Courier", 14))
        self.addressLine1 = tk.StringVar()
        ent_addr1 = tk.Entry(master=frm_addr1, textvariable=self.addressLine1)
        lbl_addr1.grid(row=0, column=0, sticky="w")
        ent_addr1.grid(row=1, column=0, sticky="w")
        frm_addr1.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        #address line 2
        frm_addr2 = tk.Frame(master=frm_panel)
        lbl_addr2 = tk.Label(master=frm_addr2, text="Address Line 2:", font=("Courier", 14))
        self.addressLine2 = tk.StringVar()
        ent_addr2 = tk.Entry(master=frm_addr2, textvariable=self.addressLine2)
        lbl_addr2.grid(row=0, column=0, sticky="w")
        ent_addr2.grid(row=1, column=0, sticky="w")
        frm_addr2.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        #city
        frm_city = tk.Frame(master=frm_panel)
        lbl_city = tk.Label(master=frm_city, text="City: (*)", font=("Courier", 14))
        self.city = tk.StringVar()
        ent_city = tk.Entry(master=frm_city, textvariable=self.city)
        lbl_city.grid(row=0, column=0, sticky="w")
        ent_city.grid(row=1, column=0, sticky="w")
        frm_city.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        #state
        frm_state = tk.Frame(master=frm_panel)
        lbl_state = tk.Label(master=frm_state, text="State: (*)", font=("Courier", 14))
        self.state = tk.StringVar()
        state_file = open("states.csv")
        states = []
        for rec in state_file:
            states.append(rec)
        cmb_state = ttk.Combobox(master=frm_state, textvariable=self.state, values=states)
        lbl_state.grid(row=0, column=0, sticky="w")
        cmb_state.grid(row=1, column=0, sticky="w")
        frm_state.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        #zip
        frm_zip = tk.Frame(master=frm_panel)
        lbl_zip = tk.Label(master=frm_zip, text="Zip:", font=("Courier", 14))
        self.zip = tk.StringVar()
        ent_zip = tk.Entry(master=frm_zip, textvariable=self.zip)
        lbl_zip.grid(row=0, column=0, sticky="w")
        ent_zip.grid(row=1, column=0, sticky="w")
        frm_zip.grid(row=2, column=2, padx=10, pady=10, sticky="w")

        #tournament table
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview.Heading', background="lightgrey")
        cols = ("Tournament ID", "Tournament Name", "Address Line 1", "Address Line 2", "City", "State", "Zip")
        colIdx = 1
        self.tree = ttk.Treeview(frm_panel, columns=cols, show="headings", height=5)
        for col in cols:
            self.tree.column("# "+str(colIdx), anchor=tk.W, stretch=tk.NO, width=140)
            self.tree.heading(col, text=col)
            colIdx = colIdx + 1
        self.tree.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky="w")
        self.tree.bind("<ButtonRelease-1>", self.click_tournament)

        frm_panel.pack(fill=tk.BOTH)

        separator = ttk.Separator(self, orient="horizontal")
        separator.pack(fill=tk.X)

        #round panel
        frm_round_panel = tk.Frame(master=self)
        frm_round_panel.rowconfigure([0, 1, 2], minsize=20, weight=1)
        frm_round_panel.columnconfigure([0, 1], minsize=100, weight=1)

        self.roundId = 0
        
        lbl_round_title = tk.Label(master=frm_round_panel, text="Rounds", font=("Courier", 22))
        lbl_round_title.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        frm_round_buttons = tk.Frame(master=frm_round_panel, borderwidth=1)
        frm_round_buttons.rowconfigure(0, minsize=50, weight=1)
        frm_round_buttons.columnconfigure([0,1,2,3], weight=1)
        btn_add_round = tk.Button(master=frm_round_buttons, text="   Add   ")
        btn_add_round.grid(row=0, column=0, padx=10, pady=10)
        btn_update_round = tk.Button(master=frm_round_buttons, text=" Update ")
        btn_update_round.grid(row=0, column=1, padx=10, pady=10)
        btn_delete_round = tk.Button(master=frm_round_buttons, text=" Delete ")
        btn_delete_round.grid(row=0, column=2, padx=10, pady=10)
        frm_round_buttons.grid(row=0, column=1, padx=10, pady=10, sticky="e")


        btn_add_round.bind("<Button-1>", self.handle_add_round)
        btn_update_round.bind("<Button-1>", self.handle_update_round)
        btn_delete_round.bind("<Button-1>", self.handle_delete_round)

        #start time
        frm_start_time = tk.Frame(master=frm_round_panel)
        lbl_start_time = tk.Label(master=frm_start_time, text="Start Time: (*)", font=("Courier", 14))
        self.startTime = tk.StringVar()
        ent_start_time = tk.Entry(master=frm_start_time, textvariable=self.startTime)
        lbl_start_time.grid(row=0, column=0, sticky="w")
        ent_start_time.grid(row=1, column=0, sticky="w")
        frm_start_time.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        #rating level
        frm_rating_level = tk.Frame(master=frm_round_panel)
        lbl_rating_level = tk.Label(master=frm_rating_level, text="Rating Level: (*)", font=("Courier", 14))
        self.ratingLevel = tk.IntVar()
        ent_rating_level = tk.Entry(master=frm_rating_level, textvariable=self.ratingLevel)
        lbl_rating_level.grid(row=0, column=0, sticky="w")
        ent_rating_level.grid(row=1, column=0, sticky="w")
        frm_rating_level.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        #round table
        rcols = ("Round ID", "Start Date Time", "Rating Level")
        rcolIdx = 1
        self.round_tree = ttk.Treeview(frm_round_panel, columns=rcols, show="headings", height=8)
        for rcol in rcols:
            self.round_tree.column("# "+str(rcolIdx), anchor=tk.W, stretch=tk.NO, width=180)
            self.round_tree.heading(rcol, text=rcol)
            rcolIdx = rcolIdx + 1
        self.round_tree.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        self.round_tree.bind("<ButtonRelease-1>", self.click_round)

        frm_round_panel.pack(fill=tk.X)

        separator1 = ttk.Separator(self, orient="horizontal")
        separator1.pack(fill=tk.X)

        #game panel
        frm_game_panel = tk.Frame(master=self)
        frm_game_panel.rowconfigure([0, 1], minsize=20, weight=1)
        frm_game_panel.columnconfigure([0, 1, 2], minsize=100, weight=1)        

        lbl_game_title = tk.Label(master=frm_game_panel, text="Games", font=("Courier", 22))
        lbl_game_title.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        #team
        frm_team = tk.Frame(master=frm_game_panel)
        lbl_team = tk.Label(master=frm_team, text="Arbiter Team:", font=("Courier", 14))
        self.teamId = tk.StringVar()
        teamList = []
        teams = self.get_teams()
        for team in teams:
            teamList.append(str(team.teamId)+" - "+team.teamName)
        cmb_team = ttk.Combobox(master=frm_team, textvariable=self.teamId, values=teamList)
        lbl_team.grid(row=0, column=0, sticky="e")
        cmb_team.grid(row=0, column=1, sticky="w")
        frm_team.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        btn_generate_games = tk.Button(master=frm_game_panel, text=" Generate Games ")
        btn_generate_games.grid(row=0, column=2, padx=10, pady=10, sticky="w")
        btn_generate_games.bind("<Button-1>", self.handle_generate_game)

        #game table
        gcols = ("Game ID", "White Player", "Black Player", "Status", "Arbiter")
        gcolIdx = 1
        self.game_tree = ttk.Treeview(frm_game_panel, columns=gcols, show="headings", height=15)
        for gcol in gcols:
            self.game_tree.column("# "+str(gcolIdx), anchor=tk.W, stretch=tk.NO, width=180)
            self.game_tree.heading(gcol, text=gcol)
            gcolIdx = gcolIdx + 1
        self.game_tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="w")

        frm_game_panel.pack(fill=tk.X)

        self.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    def get_tournament(self):
        tournament = Tournament(self.id, self.tournamentName.get(), self.addressLine1.get(), self.addressLine2.get(), self.city.get(), self.state.get(), self.zip.get())
        return tournament
        
    def handle_read(self, event):
        for row in self.tree.get_children():
            self.tree.delete(row)
        tournamentDao = TournamentDao()
        tournaments = tournamentDao.get_tournaments()
        for tournament in tournaments:
            self.tree.insert("", "end", values=(tournament.tournamentId, tournament.tournamentName, tournament.addressLine1, tournament.addressLine2, tournament.city, tournament.state, tournament.zip))

    def handle_read_old(self, event):
        tournamentDao = TournamentDao()
        tournament = tournamentDao.read_tournament(self.id.get())
        self.id = tournament.tournamentId
        self.tournamentName.set(tournament.tournamentName)
        self.addressLine1.set(tournament.addressLine1)
        self.addressLine2.set(tournament.addressLine2)
        self.city.set(tournament.city)
        self.state.set(tournament.state)
        self.zip.set(tournament.zip)

    def handle_add(self, event):
        tournament = self.get_tournament()
        tournamentDao = TournamentDao()
        tournamentDao.insert_tournament(tournament)
        self.id = tournament.tournamentId
        self.status.set("Tournament added successfully!")
        self.handle_read(event)

    def handle_update(self, event):
        tournament = self.get_tournament()
        tournamentDao = TournamentDao()
        tournamentDao.update_tournament(tournament)
        self.status.set("Tournament updated successfully!")
        self.handle_read(event)

    def handle_delete(self, event):
        tournamentDao = TournamentDao()
        tournamentId = self.id
        tournamentDao.delete_tournament(tournamentId)
        self.id = 0
        self.tournamentName.set("")
        self.addressLine1.set("")
        self.addressLine2.set("")
        self.city.set("")
        self.state.set("")
        self.zip.set("")
        self.status.set("Tournament deleted successfully for ID: %s!" % tournamentId)
        self.handle_read(event)

    def click_tournament(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            tournament = item["values"]
            self.id = tournament[0]
            self.tournamentName.set(tournament[1])
            self.addressLine1.set(tournament[2])
            self.addressLine2.set(tournament[3])
            self.city.set(tournament[4])
            self.state.set(tournament[5])
            self.zip.set(tournament[6])
        self.handle_read_round(event)

    def get_round(self):
        round = Round(self.roundId, self.id, self.startTime.get(), self.ratingLevel.get())
        return round
        
    def handle_read_round(self, event):
        for row in self.round_tree.get_children():
            self.round_tree.delete(row)
        roundDao = RoundDao()
        rounds = roundDao.get_rounds(self.id)
        for round in rounds:
            self.round_tree.insert("", "end", values=(round.roundId, round.startTime, round.ratingLevel))

    def handle_add_round(self, event):
        round = self.get_round()
        roundDao = RoundDao()
        roundDao.insert_round(round)
        self.roundId = round.roundId
        self.status.set("Round added successfully!")
        self.handle_read_round(event)

    def handle_update_round(self, event):
        round = self.get_round()
        roundDao = RoundDao()
        roundDao.update_round(round)
        self.status.set("Round updated successfully!")
        self.handle_read_round(event)

    def handle_delete_round(self, event):
        roundDao = RoundDao()
        roundDao.delete_round(self.roundId)
        self.roundId = 0
        self.startTime.set("")
        self.ratingLevel.set(0)
        self.status.set("Round deleted successfully for ID: %s!" % self.roundId)
        self.handle_read_round(event)

    def click_round(self, event):
        for selected_item in self.round_tree.selection():
            item = self.round_tree.item(selected_item)
            round = item["values"]
            self.roundId = round[0]
            self.startTime.set(round[1])
            self.ratingLevel.set(round[2])
        self.handle_read_game(event)

    def handle_read_game(self, event):
        for row in self.game_tree.get_children():
            self.game_tree.delete(row)
        gameDao = GameDao()
        games = gameDao.get_games(self.roundId)
        for game in games:
            self.game_tree.insert("", "end", values=(game.gameId, game.whitePlayer, game.blackPlayer, game.status, game.arbiter))

    def handle_generate_game(self, event):
        teamId = self.teamId.get().split(" - ")[0]
        gameDao = GameDao()
        gameDao.generate_games(self.roundId, teamId)
        self.status.set("Games generated successfully!")
        self.handle_read_game(event)

    def get_teams(self):
        teamDao = TeamDao()
        teams = teamDao.get_teams()
        return teams;
