import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import cantools
import parse_dbc_extract_signal

def load_dbc_file():
    file_path = filedialog.askopenfilename(filetypes=[("DBC files", "*.dbc")])
    if file_path:
        try:
            dbc = cantools.db.load_file(file_path)
            node_group_messages = parse_dbc_extract_signal.group_messages_by_sender(dbc)
            display_dbc_tree(node_group_messages)
        except Exception as e:
            messagebox.showerror("Error", f"Error loading DBC file: {e}")

def display_dbc_tree(sender_messages):
    tree.delete(*tree.get_children())
    for sender,messages in sender_messages.items():
        sender_node = tree.insert("", "end", text=f"SenderNode: {sender}")
        for message in messages:
            message_node = tree.insert(sender_node, "end", text=f"Message: {message.name}")
            for sig in message.signals:
                signal_node = tree.insert(message_node, "end", text=f"Signal: {sig.name}")
                tree.insert(signal_node, "end", text=f"Start Bit: {sig.start}")
                tree.insert(signal_node, "end", text=f"Length: {sig.length} bits")

# Create the main application window
root = tk.Tk()
root.title("DBC Viewer")

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Add a button to load DBC file
load_button = tk.Button(button_frame, text="Load DBC File", command=load_dbc_file)
load_button.pack(side="left", padx=5)

# Create a frame for the treeview
tree_frame = tk.Frame(root)
tree_frame.pack(expand=True, fill="both", padx=10, pady=5)

# Create a treeview widget to display the DBC tree
tree = ttk.Treeview(tree_frame)
tree.pack(side="left", fill="both", expand=True)

# Add scrollbar to the treeview
tree_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
tree_scroll.pack(side="right", fill="y")
tree.configure(yscrollcommand=tree_scroll.set)

root.mainloop()