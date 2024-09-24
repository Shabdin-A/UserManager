from tkinter import Tk, Button, Label, END
from tkinter.ttk import Treeview
from user import User
user_list = [
    User("ki", "no", 1),
    User("yo", "mo", 2),
    User('bo', "lo", 3),
]


window = Tk()
window.title("Treeview Application")

window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(0, weight=1)


header_label = Label(window, text="TreeView Application")
header_label.grid(row=0, column=0, pady=10, padx=10)

insert_button = Button(window, text="Insert")
insert_button.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")

update_button = Button(window, text="update")
update_button.grid(row=1, column=0, pady=(0, 10), padx=10)


def delete_user():
    selected_items= table.selection()
    for item in selected_items:
        remove(item)

    load_table()


def remove(natinalcode):
    for user in user_list:
        if user.nationalcode == natinalcode:
            user_list.remove(user)




delete_button = Button(window, text="delete", command=delete_user)
delete_button.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="w")


table = Treeview(window, columns=("firstname", "lastname"))
table.grid(row=2, column= 0, pady=(0,10), padx=10, sticky="nsew")


table.heading("#0", text="NO")
table.heading("#1", text="First Name")
table.heading("#2", text="Last Name")

item_list = []

def load_table():
    for item in item_list:
        table.delete(item)

    item_list.clear(item)

    row_number = 1
    for user in user_list:
        item=table.insert("", END, iid=user.nationalcode, text=str(row_number), values=(user.firstname, user.lastname))
        item_list.append(item)
        row_number += 1

load_table()

table.column("#0", width=70, anchor="w")
table.column("#0", anchor="w")
table.column("#0", anchor="w")





window.mainloop()
