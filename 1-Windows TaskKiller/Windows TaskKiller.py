import psutil
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Running Processes")

# Set the background color to black
root.configure(bg="black")

# Create the scroll bar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create the list box
listbox = tk.Listbox(root, width=100, yscrollcommand=scrollbar.set, bg="black", fg="yellow")
listbox.pack(padx=30, pady=10)

listbox.delete(0, tk.END)
processes = psutil.process_iter()
for process in processes:
    listbox.insert(tk.END, process.name())

# Configure the scroll bar
scrollbar.config(command=listbox.yview)

# Define a function to update the list of running processes
def update_processes():
    listbox.delete(0, tk.END)
    processes = psutil.process_iter()
    for process in processes:
        listbox.insert(tk.END, process.name())

# Add a "Refresh" button using ttk
refresh_button = ttk.Button(root, text="Refresh", command=update_processes)
refresh_button.pack(side=tk.RIGHT)

# Define a function to kill the selected process
def kill_process():
    try:
        selection = listbox.curselection()
        if selection:
            process_name = listbox.get(selection[0])
            for process in psutil.process_iter():
                if process.name() == process_name:
                    process.kill()
            listbox.delete(selection[0])
            messagebox.showerror("Successful", str(process_name), " Killed succesfully")
        else:
            messagebox.showerror("Error", "No process selected")
    except PermissionError:
            messagebox.showerror("Unkillable", "Access Denied")
    except:
        messagebox.showerror("Unkillable", "Access Denied")

# Add a "Kill" button using ttk
kill_button = ttk.Button(root, text="Kill", command=kill_process)
kill_button.pack(side=tk.LEFT)

# Make the window unresizable
root.resizable(width=False, height=False)

# Start the main loop
root.mainloop()
