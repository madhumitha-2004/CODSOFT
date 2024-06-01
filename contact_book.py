import tkinter as tk
from tkinter import messagebox

# Global contact list
contacts = []

# Function to add contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()

    if not name or not phone or not email:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    contacts.append({"name": name, "phone": phone, "email": email})
    messagebox.showinfo("Success", "Contact added successfully!")
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Function to view contacts
def view_contacts():
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']} - {contact['email']}")

# Function to search contact
def search_contact():
    query = entry_search.get()
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query.lower() in contact['phone'].lower() or query.lower() in contact['email'].lower():
            listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']} - {contact['email']}")

# Function to delete contact
def delete_contact():
    selected_contact = listbox_contacts.curselection()
    if not selected_contact:
        messagebox.showwarning("Selection Error", "Please select a contact to delete")
        return
    index = selected_contact[0]
    del contacts[index]
    view_contacts()
    messagebox.showinfo("Success", "Contact deleted successfully!")

# Function to update contact
def update_contact():
    selected_contact = listbox_contacts.curselection()
    if not selected_contact:
        messagebox.showwarning("Selection Error", "Please select a contact to update")
        return
    index = selected_contact[0]
    
    new_name = entry_name.get()
    new_phone = entry_phone.get()
    new_email = entry_email.get()

    if not new_name or not new_phone or not new_email:
        messagebox.showwarning("Input Error", "All fields are required for update!")
        return
    
    contacts[index] = {"name": new_name, "phone": new_phone, "email": new_email}
    view_contacts()
    messagebox.showinfo("Success", "Contact updated successfully!")

# Setup main window
root = tk.Tk()
root.title("Contact Book")

# Labels and Entries for adding/updating contact
tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=5, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=5, pady=5)

# Buttons for operations
btn_add = tk.Button(root, text="Add Contact",bg="blue",fg="white", command=add_contact)
btn_add.grid(row=3, column=0, padx=5, pady=5)

btn_update = tk.Button(root, text="Update Contact",bg="blue",fg="white",command=update_contact)
btn_update.grid(row=3, column=1, padx=5, pady=5)

btn_delete = tk.Button(root, text="Delete Contact",bg="red",fg="white", command=delete_contact)
btn_delete.grid(row=4, column=0, padx=5, pady=5)

btn_view = tk.Button(root, text="View Contacts",bg="blue",fg="white", command=view_contacts)
btn_view.grid(row=4, column=1, padx=5, pady=5)

# Search functionality
tk.Label(root, text="Search:").grid(row=5, column=0, padx=5, pady=5)
entry_search = tk.Entry(root)
entry_search.grid(row=5, column=1, padx=5, pady=5)

btn_search = tk.Button(root, text="Search Contact",bg="blue",fg="white", command=search_contact)
btn_search.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Listbox to display contacts
listbox_contacts = tk.Listbox(root, width=50)
listbox_contacts.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

# Run the main event loop
root.mainloop()
