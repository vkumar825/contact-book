import tkinter as tk
from tkinter import ttk
from contact_book import ContactBook

class Application(tk.Tk):
	
	def __init__(self, *args, **kwargs):
		
		tk.Tk.__init__(self, *args, **kwargs)
	
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)
		self.frames = {}

		for F in (StartPage, RegisterPage, ContactBookPage):

			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()


class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		email_str = tk.StringVar()
		email_label = tk.Label(self, text ="Email: ")
		email_label.place(relx=0.3, rely=0.3, anchor="center")
		email_entry = tk.Entry(self, textvariable=email_str)
		email_entry.place(relx=0.5, rely=0.3, anchor="center")

		password_str = tk.StringVar()
		password_label = tk.Label(self, text ="Password: ")
		password_label.place(relx=0.28, rely=0.4, anchor="center")
		password_entry = tk.Entry(self, textvariable=password_str)
		password_entry.place(relx=0.5, rely=0.4, anchor="center")

		login_button = ttk.Button(self, text ="Login",
		command = lambda : controller.show_frame(ContactBookPage))
		login_button.place(relx=0.5, rely=0.5, anchor="center")

		register_button = ttk.Button(self, text ="Register",
		command = lambda : controller.show_frame(RegisterPage))
		register_button.place(relx=0.5, rely=0.6, anchor="center")
		

class RegisterPage(tk.Frame):
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		name_str = tk.StringVar()
		name_label = tk.Label(self, text ="Name: ")
		name_label.place(relx=0.3, rely=0.2, anchor="center")
		name_entry = tk.Entry(self, textvariable=name_str)
		name_entry.place(relx=0.5, rely=0.2, anchor="center")

		email_str = tk.StringVar()
		email_label = tk.Label(self, text ="Email: ")
		email_label.place(relx=0.3, rely=0.3, anchor="center")
		email_entry = tk.Entry(self, textvariable=email_str)
		email_entry.place(relx=0.5, rely=0.3, anchor="center")

		password_str = tk.StringVar()
		password_label = tk.Label(self, text ="Password: ")
		password_label.place(relx=0.28, rely=0.4, anchor="center")
		password_entry = tk.Entry(self, textvariable=password_str)
		password_entry.place(relx=0.5, rely=0.4, anchor="center")

		confirm_str = tk.StringVar()
		confirm_label = tk.Label(self, text ="Confirm Password: ")
		confirm_label.place(relx=0.24, rely=0.5, anchor="center")
		confirm_entry = tk.Entry(self, textvariable=confirm_str)
		confirm_entry.place(relx=0.5, rely=0.5, anchor="center")

		create_button = ttk.Button(self, text ="Create",
		command = lambda : [controller.show_frame(ContactBookPage), self.validate_account()])
		create_button.place(relx=0.5, rely=0.6, anchor="center")

	def validate_account(self):
		print("Successfully created account!")


class ContactBookPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		self.cbook = ContactBook()
		self.display_label = tk.Label(self,font=("Arial", 25))
		self.display_label.place(relx=0.75, rely=0.19, anchor="center")
		self.info_box = tk.Text(self, height=15, width=40)

		self.search_str = tk.StringVar()
		self.search_entry = tk.Entry(self, textvariable=self.search_str, width=30)
		self.search_entry.grid(row=0, column=0, padx=10, pady=10)

		self.search_btn = tk.Button(self, text="Search", command=self.search)
		self.search_btn.grid(row=0, column=10)

		self.add_btn = tk.Button(self, text="+", command=self.add)
		self.add_btn.grid(row=0, column=11)

		self.remove_btn = tk.Button(self, text="-", command=self.remove)
		self.remove_btn.grid(row=0, column=12)

		self.contacts_list = tk.Listbox(self, height=15, width=30)
		self.contacts_list.place(relx=0.025, rely=0.150)

		self.contacts_list.bind('<<ListboxSelect>>', lambda e: self.get_info())


	def search(self):
		search_term = self.search_str.get()
		print(search_term)

		self.cbook.get_contacts_by_search(search_term)

		self.contacts_list.delete(0, tk.END)

		for i in range(len(self.cbook.get_trie().query(search_term))):
			self.contacts_list.insert(i, self.cbook.get_search_result().get(i).get("name"))


	def add(self):
		self.win = tk.Toplevel()
		self.win.title("Add Contact")
		self.win.geometry("300x300")
		self.win.anchor("center")

		self.name_label = tk.Label(self.win, text="Name")
		self.name_label.grid(row=0, column=0)
		self.name_str = tk.StringVar()
		self.name_entry = tk.Entry(self.win, textvariable=self.name_str)
		self.name_entry.grid(row=1, column=0)

		self.phone_label = tk.Label(self.win, text="Phone Number")
		self.phone_label.grid(row=2, column=0)
		self.phone_str = tk.StringVar()
		self.phone_entry = tk.Entry(self.win, textvariable=self.phone_str)
		self.phone_entry.grid(row=3, column=0)

		close_btn = ttk.Button(self.win, text="Add", command=self.close_add)
		close_btn.grid(row=4, column=0)

	def close_add(self):
		print(f"added {self.name_str.get()} with phone number {self.phone_str.get()}")
		self.cbook.add_contact(self.name_str.get(), self.phone_str.get())
		self.update_list()
		self.win.destroy()

	def remove(self):
		self.cbook.get_ordered_contacts()
		ordered_contacts = self.cbook.get_contacts()

		for key in self.contacts_list.curselection():
			self.name_to_remove = ordered_contacts.get(key).get("name")

		print(f"name to remove: {self.name_to_remove}")
		self.close_remove()

	def close_remove(self):
		print(f"removed {self.name_to_remove}")
		self.cbook.remove_contact(self.name_to_remove)
		self.update_list()

		# reset display label & hide info box for that contact when they are removed
		self.display_label.config(text="")
		self.info_box.place_forget()

	def update_list(self):
		self.contacts_list.delete(0, tk.END)

		if (len(self.cbook.get_contacts()) > 0):
			self.cbook.get_ordered_contacts()
			for i in range(len(self.cbook.get_trie().query(""))):
				self.contacts_list.insert(i, self.cbook.get_contacts().get(i).get("name"))

	def get_info(self):
		
		self.info_box.config(state="normal")
		self.info_box.delete("1.0", tk.END)

		self.cbook.get_ordered_contacts()
		ordered_contacts = self.cbook.get_contacts()

		for key in self.contacts_list.curselection():
			name = ordered_contacts.get(key).get("name")
			phone_num = ordered_contacts.get(key).get("phone_number")

		# update display label for that contact name
		self.display_label.config(text=name)

		# clear previous contact info before displaying the current info
		self.info_box.config(state="normal")
		self.info_box.delete("1.0", tk.END)

		self.info_box.place(relx=0.73, rely=0.59, anchor="center")
		self.info_box.insert(tk.INSERT, "Name: ", "")
		self.info_box.insert(tk.END, name + "\n")
		self.info_box.insert(tk.INSERT, "Phone Number: ", "")
		self.info_box.insert(tk.END, phone_num + "\n")
		self.info_box.config(state="disabled")


	
if __name__ == "__main__":
    app = Application()
    app.title("Contact Book")
    app.geometry("600x350")
    app.resizable(width=False, height=False)
    app.mainloop()
