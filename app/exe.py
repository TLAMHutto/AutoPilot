# exe.py
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import drop_down
import notes  # Ensure notes.py doesn't import back into exe.py

def load_directory_structure(parent, path):
    """Recursively load the directory structure."""
    for entry in os.scandir(path):
        if entry.is_dir(follow_symlinks=False):
            node = parent.insert('', 'end', text=entry.name, open=False)
            load_directory_structure(node, entry.path)
        else:
            parent.insert('', 'end', text=entry.name)

def refresh_tree():
    """Refresh the currently displayed directory structure."""
    directory = folder_var.get()
    full_path = os.path.join(os.getenv('DIRECTORY_PATH'), directory)
    if full_path:
        for item in tree.get_children():
            tree.delete(item)
        load_directory_structure(tree, full_path)

def select_folder(event):
    """Handle folder selection from dropdown."""
    refresh_tree()

# Set up the GUI
root = tk.Tk()
root.title("Directory Structure Viewer")

# Setup menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=lambda: filedialog.askopenfilename())
file_menu.add_command(label="IDE", command=lambda: messagebox.showinfo("IDE", "IDE placeholder"))
file_menu.add_command(label="Refresh", command=refresh_tree)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Set up the tree view
tree = ttk.Treeview(root)
tree.pack(fill='both', expand=True)

# Setup dropdown
folder_var, popupMenu = drop_down.setup_dropdown(root, select_folder)

# Start the GUI event loop
root.mainloop()
