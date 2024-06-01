import tkinter as tk
from tkinter import messagebox, simpledialog

# Global list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        update_task_listbox()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

# Function to update the listbox with current tasks
def update_task_listbox():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        listbox_tasks.insert(tk.END, task)

# Function to delete a task
def delete_task():
    selected_task_index = listbox_tasks.curselection()
    if selected_task_index:
        task = listbox_tasks.get(selected_task_index)
        tasks.remove(task)
        update_task_listbox()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete")

# Function to update a task
def update_task():
    selected_task_index = listbox_tasks.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        new_task = simpledialog.askstring("Update Task", "Enter the new task:")
        if new_task:
            tasks[task_index] = new_task
            update_task_listbox()
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to update")

# Setup main window
root = tk.Tk()
root.title("To-Do List")

# Input field and button for adding a task
entry_task = tk.Entry(root, width=40)
entry_task.grid(row=0, column=0, padx=5, pady=5)

btn_add_task = tk.Button(root, text="Add Task", command=add_task)
btn_add_task.grid(row=0, column=1, padx=5, pady=5)

# Listbox to display tasks
listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Buttons for updating and deleting tasks
btn_update_task = tk.Button(root, text="Update Task", command=update_task)
btn_update_task.grid(row=2, column=0, padx=5, pady=5)

btn_delete_task = tk.Button(root, text="Delete Task", command=delete_task)
btn_delete_task.grid(row=2, column=1, padx=5, pady=5)

# Run the main event loop
root.mainloop()
