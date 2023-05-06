import tkinter as tk
from tkinter import ttk
from entry_frame import EntryFrame
from team.team_member import TeamMember
from team.team_member_dao import TeamMemberDao

class TeamMemberFrame(EntryFrame):
    def __init__(self, parent):
        super().__init__(parent)

        #title & buttons
        frm_title = tk.Frame(master=self, borderwidth=1)
        frm_title.rowconfigure(0, minsize=50, weight=1)
        frm_title.columnconfigure(0, minsize=500, weight=2)
        frm_title.columnconfigure([1,2,3], weight=1)
        lbl_title = tk.Label(master=frm_title, text="Team Member", font=("Courier", 22))
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

        #team id field
        frm_team_id = tk.Frame(master=frm_panel)
        lbl_team_id = tk.Label(master=frm_team_id, text="Team ID:", font=("Courier", 14, "underline"))
        self.teamId = tk.IntVar()
        ent_team_id = tk.Entry(master=frm_team_id, textvariable=self.teamId)
        lbl_team_id.grid(row=0, column=0, sticky="w")
        ent_team_id.grid(row=1, column=0, sticky="w")
        frm_team_id.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        #person id field
        frm_person_id = tk.Frame(master=frm_panel)
        lbl_person_id = tk.Label(master=frm_person_id, text="Worker Person ID:", font=("Courier", 14, "underline"))
        self.personId = tk.IntVar()
        ent_person_id = tk.Entry(master=frm_person_id, textvariable=self.personId)
        lbl_person_id.grid(row=0, column=0, sticky="w")
        ent_person_id.grid(row=1, column=0, sticky="w")
        frm_person_id.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        #role field
        frm_role = tk.Frame(master=frm_panel)
        lbl_role = tk.Label(master=frm_role, text="Role: (*)", font=("Courier", 14))
        self.roleCd = tk.StringVar()
        cmb_role = ttk.Combobox(master=frm_role, textvariable=self.roleCd)
        cmb_role['values'] = ('Leader', 'Assistant Leader', 'Member')
        lbl_role.grid(row=0, column=0, sticky="w")
        cmb_role.grid(row=1, column=0, sticky="w")
        frm_role.grid(row=1, column=3, padx=10, pady=10, sticky="w")

        frm_panel.pack(fill=tk.BOTH)

        self.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    def get_team_member(self):
        teamMember = TeamMember(self.teamId.get(), self.personId.get(), self.roleCd.get())
        return teamMember
        
    def handle_read(self, event):
        teamMemberDao = TeamMemberDao()
        teamMember = teamMemberDao.read_team_member(self.teamId.get(), self.personId.get())
        self.roleCd.set(teamMember.roleCd)

    def handle_add(self, event):
        teamMember = self.get_team_member()
        teamMemberDao = TeamMemberDao()
        teamMemberDao.insert_team_member(teamMember)
        self.teamId.set(teamMember.teamId)
        self.personId.set(teamMember.personId)
        self.status.set("Team member added successfully!")


    def handle_update(self, event):
        teamMember = self.get_team_member()
        teamMemberDao = TeamMemberDao()
        teamMemberDao.update_team_member(teamMember)
        self.status.set("Team member updated successfully!")

    def handle_delete(self, event):
        teamMemberDao = TeamMemberDao()
        teamId = self.teamId.get()
        personId = self.personId.get()
        teamMemberDao.delete_team_member(teamId, personId)
        self.teamId.set(0)
        self.personId.set(0)
        self.roleCd.set("")
        self.status.set("Team member deleted successfully for team ID %s and person ID %s!" % teamId % personId)
