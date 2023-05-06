import tkinter as tk
from tkinter import ttk
from entry_frame import EntryFrame
from team.team import Team
from team.team_dao import TeamDao
from team.team_member import TeamMember
from team.team_member_view import TeamMemberView
from team.team_member_dao import TeamMemberDao
from worker.worker_dao import WorkerDao
from worker.worker_view import WorkerView

class TeamFrame(EntryFrame):
    def __init__(self, parent):
        super().__init__(parent)

        #title & buttons
        frm_title = tk.Frame(master=self, borderwidth=1)
        frm_title.rowconfigure(0, minsize=50, weight=1)
        # frm_title.columnconfigure(0, minsize=500, weight=2)
        frm_title.columnconfigure([1,2,3], weight=1)
        lbl_title = tk.Label(master=frm_title, text="Team", font=("Courier", 22))
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

        #tournament panel
        frm_panel = tk.Frame(master=self)
        frm_panel.rowconfigure([0, 1, 2, 3], minsize=20, weight=1)
        frm_panel.columnconfigure([0, 1], minsize=100, weight=1)

        #status
        self.status = tk.StringVar()
        lbl_status = tk.Label(master=frm_panel, textvariable=self.status, fg="#f00", font=("Courier", 16))
        lbl_status.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        #id field
        frm_id = tk.Frame(master=frm_panel)
        lbl_id = tk.Label(master=frm_id, text="ID:", font=("Courier", 14, "underline"))
        self.id = tk.IntVar()
        ent_id = tk.Entry(master=frm_id, textvariable=self.id)
        lbl_id.grid(row=0, column=0, sticky="w")
        ent_id.grid(row=1, column=0, sticky="w")
        frm_id.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        #name
        frm_name = tk.Frame(master=frm_panel)
        lbl_name = tk.Label(master=frm_name, text="Team Name: (*)", font=("Courier", 14))
        self.teamName = tk.StringVar()
        ent_name = tk.Entry(master=frm_name, textvariable=self.teamName)
        lbl_name.grid(row=0, column=0, sticky="w")
        ent_name.grid(row=1, column=0, sticky="w")
        frm_name.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        #description
        frm_desc = tk.Frame(master=frm_panel)
        lbl_desc = tk.Label(master=frm_desc, text="Team Description: (*)", font=("Courier", 14))
        self.teamDesc = tk.StringVar()
        ent_desc = tk.Entry(master=frm_desc, textvariable=self.teamDesc)
        lbl_desc.grid(row=0, column=0, sticky="w")
        ent_desc.grid(row=1, column=0, sticky="w")
        frm_desc.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        #team table
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview.Heading', background="lightgrey")
        cols = ("Team ID", "Team Name", "Team Description")
        colIdx = 1
        self.team_tree = ttk.Treeview(frm_panel, columns=cols, show="headings", height=10)
        for col in cols:
            self.team_tree.column("# "+str(colIdx), anchor=tk.W, stretch=tk.NO, width=200)
            self.team_tree.heading(col, text=col)
            colIdx = colIdx + 1
        self.team_tree.grid(row=1, column=1, rowspan=3, padx=10, pady=10, sticky="w")
        self.team_tree.bind("<ButtonRelease-1>", self.click_team)

        frm_panel.pack(fill=tk.BOTH)

        separator = ttk.Separator(self, orient="horizontal")
        separator.pack(fill=tk.X)

        frm_member_panel = tk.Frame(master=self)
        frm_member_panel.rowconfigure([0, 1, 2, 3], minsize=20, weight=1)
        frm_member_panel.columnconfigure([0, 1, 2], minsize=100, weight=1)

        #member label
        lbl_member_title = tk.Label(master=frm_member_panel, text="Members", font=("Courier", 22))
        lbl_member_title.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="w")

        #person id field
        frm_person_id = tk.Frame(master=frm_member_panel)
        lbl_person_id = tk.Label(master=frm_person_id, text="Worker Person ID:", font=("Courier", 14, "underline"))
        self.personId = tk.IntVar()
        ent_person_id = tk.Entry(master=frm_person_id, textvariable=self.personId)
        lbl_person_id.grid(row=0, column=0, sticky="w")
        ent_person_id.grid(row=1, column=0, sticky="w")
        frm_person_id.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        #role field
        frm_role = tk.Frame(master=frm_member_panel)
        lbl_role = tk.Label(master=frm_role, text="Role: (*)", font=("Courier", 14))
        self.roleCd = tk.StringVar()
        cmb_role = ttk.Combobox(master=frm_role, textvariable=self.roleCd)
        cmb_role['values'] = ('Leader', 'Assistant Leader', 'Member')
        lbl_role.grid(row=0, column=0, sticky="w")
        cmb_role.grid(row=1, column=0, sticky="w")
        frm_role.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        #member buttons
        frm_member_buttons = tk.Frame(master=frm_member_panel)
        frm_member_buttons.rowconfigure([0, 1, 2], minsize=50, weight=1)
        frm_member_buttons.columnconfigure(1, weight=1)

        btn_member_add = tk.Button(master=frm_member_buttons, text="   Add   ")
        btn_member_add.grid(row=0, column=0, padx=10, pady=10)
        btn_member_update = tk.Button(master=frm_member_buttons, text=" Update ")
        btn_member_update.grid(row=1, column=0, padx=10, pady=10)
        btn_member_delete = tk.Button(master=frm_member_buttons, text=" Delete ")
        btn_member_delete.grid(row=2, column=0, padx=10, pady=10)

        btn_member_add.bind("<Button-1>", self.handle_add_member)
        btn_member_update.bind("<Button-1>", self.handle_update_member)
        btn_member_delete.bind("<Button-1>", self.handle_delete_member)

        frm_member_buttons.grid(row=1, column=1, rowspan=2, padx=10, pady=10)

        #member table
        mcols = ("Team ID", "Person ID", "Firstname", "Lastname", "Role", "Skills")
        mcolIdx = 1
        self.member_tree = ttk.Treeview(frm_member_panel, columns=mcols, show="headings", height=20)
        for mcol in mcols:
            self.member_tree.column("# "+str(mcolIdx), anchor=tk.W, stretch=tk.NO, width=140)
            self.member_tree.heading(mcol, text=mcol)
            mcolIdx = mcolIdx + 1
        self.member_tree.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        self.member_tree.bind("<ButtonRelease-1>", self.click_member)

        #worker table
        frm_worker = tk.Frame(master=frm_member_panel)
        lbl_worker_skill = tk.Label(master=frm_worker, text="Search Worker by Skill:", font=("Courier", 14))
        self.workerSkill = tk.StringVar()
        ent_worker_skill = tk.Entry(master=frm_worker, textvariable=self.workerSkill)
        btn_search = tk.Button(master=frm_worker, text=" Search ")
        lbl_worker_skill.grid(row=0, column=0, sticky="w", columnspan=2)
        ent_worker_skill.grid(row=1, column=0, sticky="w")
        btn_search.grid(row=1, column=1, sticky="w")
        btn_search.bind("<Button-1>", self.handle_search_worker)
        wcols = ("Person ID", "Firstname", "Lastname", "Skills")
        wcolIdx = 1
        self.worker_tree = ttk.Treeview(frm_worker, columns=wcols, show="headings", height=20)
        for wcol in wcols:
            self.worker_tree.column("# "+str(wcolIdx), anchor=tk.W, stretch=tk.NO, width=140)
            self.worker_tree.heading(wcol, text=wcol)
            wcolIdx = wcolIdx + 1
        self.worker_tree.grid(row=3, column=0, columnspan=2, sticky="ew")
        self.worker_tree.bind("<ButtonRelease-1>", self.click_worker)
        frm_worker.grid(row=1, column=3, rowspan=3, padx=10, pady=10, sticky="we")

        frm_member_panel.pack(fill=tk.BOTH)

        self.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    def get_team(self):
        team = Team(self.id.get(), self.teamName.get(), self.teamDesc.get())
        return team

    def click_team(self, event):
        for selected_item in self.team_tree.selection():
            item = self.team_tree.item(selected_item)
            team = item["values"]
            self.id.set(team[0])
            self.teamName.set(team[1])
            self.teamDesc.set(team[2])
        self.handle_member_read(event)
    
    def handle_read(self, event):
        for row in self.team_tree.get_children():
            self.team_tree.delete(row)
        teamDao = TeamDao()
        teams = teamDao.get_teams()
        for team in teams:
            self.team_tree.insert("", "end", values=(team.teamId, team.teamName, team.teamDesc))

    def handle_read_old(self, event):
        teamDao = TeamDao()
        team = teamDao.read_team(self.id.get())
        self.id.set(team.teamId)
        self.teamName.set(team.teamName)
        self.teamDesc.set(team.teamDesc)

    def handle_add(self, event):
        team = self.get_team()
        teamDao = TeamDao()
        teamDao.insert_team(team)
        self.id.set(team.teamId)
        self.status.set("Team added successfully!")
        self.handle_read(event)

    def handle_update(self, event):
        team = self.get_team()
        teamDao = TeamDao()
        teamDao.update_team(team)
        self.status.set("Team updated successfully!")
        self.handle_read(event)

    def handle_delete(self, event):
        teamDao = TeamDao()
        teamId = self.id.get()
        teamDao.delete_team(teamId)
        self.id.set(0)
        self.teamName.set("")
        self.teamDesc.set("")
        self.status.set("Team deleted successfully for ID: %s!" % teamId)
        self.handle_read(event)

    def handle_member_read(self, event):
        for row in self.member_tree.get_children():
            self.member_tree.delete(row)
        teamMemberDao = TeamMemberDao()
        teamMembers = teamMemberDao.get_team_members(self.id.get())
        for teamMember in teamMembers:
            self.member_tree.insert("", "end", values=(teamMember.teamId, teamMember.personId, teamMember.firstName, 
                                                       teamMember.lastName, teamMember.role, teamMember.skills))

    def click_member(self, event):
        for selected_item in self.member_tree.selection():
            item = self.member_tree.item(selected_item)
            member = item["values"]
            self.personId.set(member[1])
            self.roleCd.set(member[4])

    def get_team_member(self):
        teamMember = TeamMember(self.id.get(), self.personId.get(), self.roleCd.get())
        return teamMember
    
    def click_worker(self, event):
        for selected_item in self.worker_tree.selection():
            item = self.worker_tree.item(selected_item)
            worker = item["values"]
            self.personId.set(worker[0])
            self.roleCd.set("")

    def handle_search_worker(self, event):
        for row in self.worker_tree.get_children():
            self.worker_tree.delete(row)
        workerDao = WorkerDao()
        workers = workerDao.get_worker_by_skill(self.workerSkill.get())
        for worker in workers:
            self.worker_tree.insert("", "end", values=(worker.personId, worker.firstName, worker.lastName, worker.skillDesc))

    def handle_add_member(self, event):
        teamMember = self.get_team_member()
        teamMemberDao = TeamMemberDao()
        teamMemberDao.insert_team_member(teamMember)
        self.id.set(teamMember.teamId)
        self.personId.set(teamMember.personId)
        self.status.set("Team member added successfully!")
        self.handle_member_read(event)

    def handle_update_member(self, event):
        teamMember = self.get_team_member()
        teamMemberDao = TeamMemberDao()
        teamMemberDao.update_team_member(teamMember)
        self.status.set("Team member updated successfully!")
        self.handle_member_read(event)

    def handle_delete_member(self, event):
        teamMemberDao = TeamMemberDao()
        teamId = self.id.get()
        personId = self.personId.get()
        teamMemberDao.delete_team_member(teamId, personId)
        self.personId.set(0)
        self.roleCd.set("")
        self.status.set("Team member deleted successfully for person ID %s!" % personId)
        self.handle_member_read(event)
