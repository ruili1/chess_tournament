import tkinter as tk
from home_frame import HomeFrame
from person.person_frame import PersonFrame
from player.player_frame import PlayerFrame
from worker.worker_frame import WorkerFrame
from team.team_frame import TeamFrame
from team.team_member_frame import TeamMemberFrame
from tournament.tournament_frame import TournamentFrame
from round.round_frame import RoundFrame
from game.game_frame import GameFrame

class MainWindow():
    def __init__(self, master):
        mainframe = tk.Frame(master)
        mainframe.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.index=0

        self.frameList = [HomeFrame(mainframe), PersonFrame(mainframe), PlayerFrame(mainframe), 
                          WorkerFrame(mainframe), TeamFrame(mainframe), TournamentFrame(mainframe)]
        for i in range(1, len(self.frameList)):
            self.frameList[i].forget()

    def showFrame(self, newIndex):
        self.frameList[self.index].forget()
        self.index = newIndex
        self.frameList[self.index].tkraise()
        self.frameList[self.index].pack(padx=10, pady=10, expand=True, fill=tk.BOTH)