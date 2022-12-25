import tkinter as tk
from tkinter import ttk
from contact_book import ContactBook
from database import Database

db = Database()
cbook = ContactBook()


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (StartPage, RegisterPage, ContactBookPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, page):
        return self.frames[page]


class StartPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        login_label = tk.Label(self, text="Login", font=("Arial", 25))
        login_label.place(relx=0.5, rely=0.2, anchor="center")

        self.email_str = tk.StringVar()
        email_label = tk.Label(self, text="Email: ")
        email_label.place(relx=0.3, rely=0.3, anchor="center")
        self.email_entry = tk.Entry(self, textvariable=self.email_str)
        self.email_entry.place(relx=0.5, rely=0.3, anchor="center")

        self.login_password = tk.StringVar()
        password_label = tk.Label(self, text="Password: ")
        password_label.place(relx=0.28, rely=0.4, anchor="center")
        self.password_entry = tk.Entry(self, textvariable=self.login_password)
        self.password_entry.place(relx=0.5, rely=0.4, anchor="center")

        login_button = ttk.Button(self, text="Login",
                                  command=self.verify_user)
        login_button.place(relx=0.5, rely=0.5, anchor="center")

        register_button = ttk.Button(self, text="Register",
                                     command=lambda: [controller.show_frame(RegisterPage)])
        register_button.place(relx=0.5, rely=0.6, anchor="center")

    def verify_user(self):

        if (db.contains_user(self.email_str.get(), self.login_password.get())):
            print("Successfully logged in!")
            contacts_list = db.fetch(self.email_str.get())
            if len(contacts_list) > 0:
                for i in range(len(contacts_list)):
                    cbook.add_contact(
                        contacts_list[i]["name"], contacts_list[i]["phone_number"])
                page = self.controller.get_page(ContactBookPage)
                page.update_list()

            self.controller.show_frame(ContactBookPage)

        else:
            print("Failed to log in! Try again")

    def get_email(self):
        return self.email_str.get()


class RegisterPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        register_label = tk.Label(self, text="Register", font=("Arial", 25))
        register_label.place(relx=0.5, rely=0.2, anchor="center")

        self.email_str = tk.StringVar()
        email_label = tk.Label(self, text="Email: ")
        email_label.place(relx=0.3, rely=0.3, anchor="center")
        self.email_entry = tk.Entry(self, textvariable=self.email_str)
        self.email_entry.place(relx=0.5, rely=0.3, anchor="center")

        self.password_str = tk.StringVar()
        password_label = tk.Label(self, text="Password: ")
        password_label.place(relx=0.28, rely=0.4, anchor="center")
        self.password_entry = tk.Entry(self, textvariable=self.password_str)
        self.password_entry.place(relx=0.5, rely=0.4, anchor="center")

        self.confirm_str = tk.StringVar()
        confirm_label = tk.Label(self, text="Confirm Password: ")
        confirm_label.place(relx=0.24, rely=0.5, anchor="center")
        confirm_entry = tk.Entry(self, textvariable=self.confirm_str)
        confirm_entry.place(relx=0.5, rely=0.5, anchor="center")

        create_button = ttk.Button(
            self, text="Create", command=self.create_account)
        create_button.place(relx=0.5, rely=0.6, anchor="center")

        back_button = ttk.Button(
            self, text="Back", command=lambda: controller.show_frame(StartPage))
        back_button.place(relx=0.5, rely=0.7, anchor="center")

    def create_account(self):
        if (self.confirm_str.get() == self.password_str.get()):
            db.create_user(self.email_str.get(), self.password_str.get())
            print("Successfully created account!")
            # self.email_entry.delete(0, tk.END)
            # self.password_entry.delete(0, tk.END)
            self.controller.show_frame(StartPage)
        else:
            print("Passwords do not match. Please try again.")
            pass


class ContactBookPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.display_label = tk.Label(self, font=("Arial", 25))
        self.display_label.place(relx=0.75, rely=0.19, anchor="center")
        self.info_box = tk.Text(self, height=15, width=40)

        self.search_str = tk.StringVar()
        self.search_entry = tk.Entry(
            self, textvariable=self.search_str, width=30)
        self.search_entry.grid(row=0, column=0, padx=10, pady=10)
        self.has_searched = False

        self.search_btn = tk.Button(self, text="Search", command=self.search)
        self.search_btn.grid(row=0, column=10)

        self.add_btn = tk.Button(self, text="+", command=self.add)
        self.add_btn.grid(row=0, column=11)

        self.remove_btn = tk.Button(self, text="-", command=self.remove)
        self.remove_btn.grid(row=0, column=12)

        self.contacts_list = tk.Listbox(self, height=15, width=30)
        self.contacts_list.place(relx=0.025, rely=0.150)
        self.contacts_list.bind('<<ListboxSelect>>', lambda e: self.get_info())

        self.logout_btn = tk.Button(self, text="Logout", command=self.logout)
        self.logout_btn.grid(row=0, column=13)

    def search(self):
        search_term = self.search_str.get()

        if len(search_term) > 0:
            self.has_searched = True
        else:
            self.has_searched = False

        cbook.get_contacts_by_search(search_term)
        self.contacts_list.delete(0, tk.END)

        for i in range(len(cbook.get_trie().query(search_term))):
            self.contacts_list.insert(
                i, cbook.get_search_result()[i].get("name"))

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
        print("Went here to close add")
        page = self.controller.get_page(StartPage)
        print(page.get_email())
        db.insert(page.get_email(), self.name_str.get(), self.phone_str.get())
        cbook.add_contact(self.name_str.get(), self.phone_str.get())
        self.update_list()
        self.win.destroy()

    def remove(self):
        if self.contacts_list.curselection():

            if self.has_searched:
                list_of_contacts = cbook.get_search_result()
            else:
                list_of_contacts = cbook.get_contacts()

            for key in self.contacts_list.curselection():
                name_to_remove = list_of_contacts[key].get("name")
                phone_number_to_remove = list_of_contacts[key].get(
                    "phone_number")

            self.close_remove(name_to_remove, phone_number_to_remove)

        else:
            print("Need to select before removing")

    def close_remove(self, name_to_remove, phone_number_to_remove):
        page = self.controller.get_page(StartPage)
        db.remove(page.get_email(), name_to_remove, phone_number_to_remove)
        cbook.remove_contact(name_to_remove)
        self.update_list()

        # reset display label & hide info box for that contact when they are removed
        self.display_label.config(text="")
        self.info_box.place_forget()

    def update_list(self):
        self.contacts_list.delete(0, tk.END)

        if (len(cbook.get_contacts()) > 0):
            for i in range(len(cbook.get_trie().query(""))):
                self.contacts_list.insert(
                    i, cbook.get_contacts()[i].get("name"))

    def get_info(self):

        if self.has_searched:
            list_of_contacts = cbook.get_search_result()
        else:
            list_of_contacts = cbook.get_contacts()

        for key in self.contacts_list.curselection():
            name = list_of_contacts[key].get("name")
            phone_num = list_of_contacts[key].get("phone_number")

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

    def logout(self):
        trie_length = len(cbook.get_trie().query(""))
        print(f"before logout: {trie_length}")
        cbook.remove_all_contacts()
        print(f"after logout :{trie_length}")
        self.controller.show_frame(StartPage)


if __name__ == "__main__":
    app = Application()
    app.title("Contact Book")
    app.geometry("600x350")
    app.resizable(width=False, height=False)
    app.mainloop()
