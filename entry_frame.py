import tkinter as tk

class EntryFrame(tk.Frame):
    def set_entry_text(entry, text):
        entry.delete(0, tk.END)
        entry.insert(0, text)
