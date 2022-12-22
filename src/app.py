import tkinter as tk
from tkinter import ttk

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

		search_str = tk.StringVar()
		search = tk.Entry(self, textvariable=search_str, width=30)
		search.grid(row=0, column=0, padx=10, pady=10)

		search_btn = tk.Button(self, text="Search")
		search_btn.grid(row=0, column=10)

		add_btn = tk.Button(self, text="+")
		add_btn.grid(row=0, column=11)

		remove_btn = tk.Button(self, text="-")
		remove_btn.grid(row=0, column=12)

		contacts_list = tk.Listbox(self, height=15, width=30)
		contacts_list.place(relx=0.025, rely=0.150)

		placeholder_name = tk.Label(self, text ="John Doe",font=("Arial", 25))
		placeholder_name.place(relx=0.75, rely=0.19, anchor="center")

		email = "doe@mail.com"
		phone_num = "741-283-1922"

		info_box = tk.Text(self, height=10, width=30)
		info_box.insert(tk.INSERT, "Email: ", "")
		info_box.insert(tk.END, email + "\n")
		info_box.insert(tk.INSERT, "Phone Number: ", "")
		info_box.insert(tk.END, phone_num + "\n")
		info_box.config(state="disabled")
		info_box.place(relx=0.75, rely=0.45, anchor="center")

		

if __name__ == "__main__":
    app = Application()
    app.title("Contact Book")
    app.geometry("600x350")
    app.resizable(width=False, height=False)
    app.mainloop()
