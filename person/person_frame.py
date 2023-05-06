import tkinter as tk
from tkinter import ttk
from person.person import Person
from person.person_dao import PersonDao
from entry_frame import EntryFrame

class PersonFrame(EntryFrame):
    def __init__(self, parent):
        super().__init__(parent)

        #title & buttons
        frm_title = tk.Frame(master=self, borderwidth=1)
        frm_title.rowconfigure(0, minsize=50, weight=1)
        frm_title.columnconfigure(0, minsize=500, weight=2)
        frm_title.columnconfigure([1,2,3], weight=1)
        lbl_title = tk.Label(master=frm_title, text="Person", font=("Courier", 22))
        lbl_title.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        btn_read = tk.Button(master=frm_title, text="   Show   ")
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
        lbl_status = tk.Label(master=frm_panel, fg="#f00", font=("Courier", 16), textvariable=self.status)
        lbl_status.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="w")

        #id field
        frm_id = tk.Frame(master=frm_panel)
        lbl_id = tk.Label(master=frm_id, text="ID:", font=("Courier", 14, "underline"))
        self.id = tk.IntVar()
        ent_id = tk.Entry(master=frm_id, textvariable=self.id)
        lbl_id.grid(row=0, column=0, sticky="w")
        ent_id.grid(row=1, column=0, sticky="w")
        frm_id.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        #firstname
        frm_fname = tk.Frame(master=frm_panel)
        lbl_fname = tk.Label(master=frm_fname, text="Firstname: (*)", font=("Courier", 14))
        self.firstname = tk.StringVar()
        ent_fname = tk.Entry(master=frm_fname, textvariable=self.firstname)
        lbl_fname.grid(row=0, column=0, sticky="w")
        ent_fname.grid(row=1, column=0, sticky="w")
        frm_fname.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        #lastname
        frm_lname = tk.Frame(master=frm_panel)
        lbl_lname = tk.Label(master=frm_lname, text="Lastname: (*)", font=("Courier", 14))
        self.lastname = tk.StringVar()
        ent_lname = tk.Entry(master=frm_lname, textvariable=self.lastname)
        lbl_lname.grid(row=0, column=0, sticky="w")
        ent_lname.grid(row=1, column=0, sticky="w")
        frm_lname.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        #gender
        frm_gender = tk.Frame(master=frm_panel)
        lbl_gender = tk.Label(master=frm_gender, text="Gender: (*)", font=("Courier", 14))
        self.gender = tk.StringVar()
        cmb_gender = ttk.Combobox(master=frm_gender, textvariable=self.gender)
        cmb_gender['values'] = ('Male', 'Female', 'N/A')
        lbl_gender.grid(row=0, column=0, sticky="w")
        cmb_gender.grid(row=1, column=0, sticky="w")
        frm_gender.grid(row=2, column=2, padx=10, pady=10, sticky="w")

        #email
        frm_email = tk.Frame(master=frm_panel)
        lbl_email = tk.Label(master=frm_email, text="Email: (*)", font=("Courier", 14))
        self.email = tk.StringVar()
        ent_email = tk.Entry(master=frm_email, textvariable=self.email)
        lbl_email.grid(row=0, column=0, sticky="w")
        ent_email.grid(row=1, column=0, sticky="w")
        frm_email.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        #phone
        frm_phone = tk.Frame(master=frm_panel)
        lbl_phone = tk.Label(master=frm_phone, text="Phone: (*)", font=("Courier", 14))
        self.phone = tk.StringVar()
        ent_phone = tk.Entry(master=frm_phone, textvariable=self.phone)
        lbl_phone.grid(row=0, column=0, sticky="w")
        ent_phone.grid(row=1, column=0, sticky="w")
        frm_phone.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        #address line 1
        frm_addr1 = tk.Frame(master=frm_panel)
        lbl_addr1 = tk.Label(master=frm_addr1, text="Address Line 1: (*)", font=("Courier", 14))
        self.address1 = tk.StringVar()
        ent_addr1 = tk.Entry(master=frm_addr1, textvariable=self.address1)
        lbl_addr1.grid(row=0, column=0, sticky="w")
        ent_addr1.grid(row=1, column=0, sticky="w")
        frm_addr1.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        #address line 2
        frm_addr2 = tk.Frame(master=frm_panel)
        lbl_addr2 = tk.Label(master=frm_addr2, text="Address Line 2:", font=("Courier", 14))
        self.address2 = tk.StringVar()
        ent_addr2 = tk.Entry(master=frm_addr2, textvariable=self.address2)
        lbl_addr2.grid(row=0, column=0, sticky="w")
        ent_addr2.grid(row=1, column=0, sticky="w")
        frm_addr2.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        #city
        frm_city = tk.Frame(master=frm_panel)
        lbl_city = tk.Label(master=frm_city, text="City: (*)", font=("Courier", 14))
        self.city = tk.StringVar()
        ent_city = tk.Entry(master=frm_city, textvariable=self.city)
        lbl_city.grid(row=0, column=0, sticky="w")
        ent_city.grid(row=1, column=0, sticky="w")
        frm_city.grid(row=5, column=0, padx=10, pady=10, sticky="w")

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
        frm_state.grid(row=5, column=1, padx=10, pady=10, sticky="w")

        #zip
        frm_zip = tk.Frame(master=frm_panel)
        lbl_zip = tk.Label(master=frm_zip, text="Zip:", font=("Courier", 14))
        self.zip = tk.IntVar()
        ent_zip = tk.Entry(master=frm_zip, textvariable=self.zip)
        lbl_zip.grid(row=0, column=0, sticky="w")
        ent_zip.grid(row=1, column=0, sticky="w")
        frm_zip.grid(row=5, column=2, padx=10, pady=10, sticky="w")

        #person table
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview.Heading', background="lightgrey")
        cols = ("Person ID", "Firstname", "Lastname", "Gender", "Email", "Phone", "Address Line 1", "Address Line 2", "City", "State", "Zip")
        colIdx = 1
        self.tree = ttk.Treeview(frm_panel, columns=cols, show="headings", height=20)
        for col in cols:
            self.tree.column("# "+str(colIdx), anchor=tk.W, stretch=tk.NO, width=138)
            self.tree.heading(col, text=col)
            colIdx = colIdx + 1
        self.tree.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky="w")
        self.tree.bind("<ButtonRelease-1>", self.click_person)

        frm_panel.pack(fill=tk.BOTH)

    # def set_entry_text(entry, text):
    #     entry.delete(0, tk.END)
    #     entry.insert(0, text)
        
    def get_person(self):
        person = Person(self.id.get(), self.firstname.get(), self.lastname.get(), self.gender.get(), 
                        self.email.get(), self.phone.get(), self.address1.get(), self.address2.get(),
                        self.city.get(), self.state.get(), self.zip.get())
        return person
        
    def click_person(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            person = item["values"]
            self.id.set(person[0])
            self.firstname.set(person[1])
            self.lastname.set(person[2])
            self.gender.set(person[3])
            self.email.set(person[4])
            self.phone.set(person[5])
            self.address1.set(person[6])
            self.address2.set(person[7])
            self.city.set(person[8])
            self.state.set(person[9])
            self.zip.set(person[10])

    def handle_read(self, event):
        for row in self.tree.get_children():
            self.tree.delete(row)
        personDao = PersonDao()
        persons = personDao.get_persons()
        for person in persons:
            self.tree.insert("", "end", values=(person.personId, person.firstName, person.lastName, person.gender, person.emailAddress,
                                                person.phoneNumber, person.addressLine1, person.addressLine2, person.city, person.state, person.zip))

    def handle_read_old(self, event):
        personDao = PersonDao()
        person = personDao.read_person(self.id.get())
        # print("id selected is ", self.id.get())
        self.firstname.set(person.firstName)
        self.lastname.set(person.lastName)
        self.gender.set(person.gender)
        self.email.set(person.emailAddress)
        self.phone.set(person.phoneNumber)
        self.address1.set(person.addressLine1)
        self.address2.set(person.addressLine2)
        self.city.set(person.city)
        self.state.set(person.state)
        self.zip.set(person.zip)

    def handle_add(self, event):
        person = self.get_person()
        personDao = PersonDao()
        personDao.insert_person(person)
        self.id.set(person.personId)
        self.status.set("Person added successfully!")
        self.handle_read(event)


    def handle_update(self, event):
        person = self.get_person()
        personDao = PersonDao()
        personDao.update_person(person)
        self.status.set("Person updated successfully!")
        self.handle_read(event)

    def handle_delete(self, event):
        personDao = PersonDao()
        personId = self.id.get()
        person = personDao.delete_person(personId)
        self.id.set(0)
        self.firstname.set("")
        self.lastname.set("")
        self.gender.set("")
        self.email.set("")
        self.phone.set("")
        self.address1.set("")
        self.address2.set("")
        self.city.set("")
        self.state.set("")
        self.zip.set(0)
        self.status.set("Person deleted successfully for ID: %s!" % personId)
        self.handle_read(event)