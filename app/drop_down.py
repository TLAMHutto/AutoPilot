# drop_down.py
import tkinter as tk
from tkinter import ttk
import os
import notes  # Ensure this import does not lead back to exe.py

def setup_dropdown(root, callback):
    """Sets up a dropdown for folder selection and binds it to a callback."""
    folder_var = tk.StringVar(root)
    folders = notes.load_folders_from_env()
    folder_var.set(folders[0] if folders else 'No folders found')
    popupMenu = ttk.Combobox(root, textvariable=folder_var, values=folders)
    popupMenu.pack()
    popupMenu.bind('<<ComboboxSelected>>', callback)
    return folder_var, popupMenu
