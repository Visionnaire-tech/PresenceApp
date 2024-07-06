from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk
from time import strftime


def save():
    nom = enter2.get()
    prenom = enter3.get()
    poste = enter4.get()
    moreinfo = enter5.get()

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    val = "CREATE TABLE IF NOT EXISTS  controle(ID INTEGER PRIMARY KEY AUTOINCREMENT,nom TEXT NOT NULL,prenom TEXT NOT NULL,poste TEXT NOT NULL,moreinfo TEXT NOT NULL)"
    cur.execute(val)

    req2 = "INSERT INTO controle(nom,prenom,poste,moreinfo)  values(?,?,?,?)"
    cur.execute(req2, (nom, prenom, poste, moreinfo))
    conn.commit()

    select = cur.execute("SELECT*FROM controle order by id desc")
    select = list(select)
    tree.insert('', END, values=select[0])

    enter2.delete(0, END)
    enter3.delete(0, END)
    enter4.delete(0, END)
    enter5.delete(0, END)
    conn.close()
    messagebox.showinfo("Save", "Votrez enregistrement a  été bien effectuer ")


def sup():
    idSelect = tree.item(tree.selection())['values'][0]
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    delete = cur.execute("delete from controle where id ={}".format(idSelect))
    conn.commit()
    tree.delete(tree.selection())


def TreeActionSelect(event):
    idSelect = tree.item(tree.selection())['values'][0]
    nameSelect = tree.item(tree.selection())['values'][1]
    prenomSelect = tree.item(tree.selection())['values'][2]
    posteSelect = tree.item(tree.selection())['values'][3]
    moreInfoSelect = tree.item(tree.selection())['values'][4]

    lid = Label(isc, text='ID :' + str(idSelect))
    lid.place(x=600, y=200)
    lname = Label(isc, text='Name :' + str(nameSelect))
    lname.place(x=600, y=250)
    lprenom = Label(isc, text='Prénom :' + str(prenomSelect))
    lprenom.place(x=600, y=300)
    lposte = Label(isc, text='Poste :' + str(posteSelect))
    lposte.place(x=600, y=350)
    Tmore = Text(isc)
    Tmore.place(x=600, y=400, width=250, height=190)
    Tmore.insert(END, 'More Info : ' + moreInfoSelect)


def SearchByName(event):
    for x in tree.get_children():
        tree.delete(x)
    nom = entrySearchByName.get()
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    select = cur.execute("SELECT*FROM controle where nom=(?)", (nom,))
    conn.commit()
    for row in select:
        tree.insert('', END, values=row)
    conn.close()


def update_time():
    current_time = strftime('%H:%M:%S')
    time_label.config(text=current_time)
    isc.after(1000, update_time)


isc = Tk()
isc.title(" KUMIKU BENGWA TYCHIQUE")

isc.geometry("900x600")
isc.resizable(False, False)

fr = Frame(isc, width=900, height=100, bg="#6f7833", highlightbackground="yellow", highlightthickness=3).place(x=0, y=0)

fr = Frame(isc, width=900, height=10, bg="#6f7833").place(x=0, y=130)

txt = Label(fr, text=" TECHNOLOGY PRESENCE", bg="#6f7833", font=("Bauhaus 93", 20))
txt.place(x=250, y=40)

time_label = Label(fr, font=('Helvetica', 25), fg='black', bg="#6f7833")
time_label.place(x=750, y=20)

txt = Label(isc, text="Nom")
txt.place(x=50, y=145)

txt = Label(isc, text="PRENOM")
txt.place(x=50, y=200)

txt = Label(isc, text="POSTE")
txt.place(x=50, y=260)

txt = Label(isc, text="INFO_MORE")
txt.place(x=50, y=320)

enter2 = Entry(isc)
enter2.place(x=250, y=145)

enter3 = Entry(isc)
enter3.place(x=250, y=200)

enter4 = Entry(isc)
enter4.place(x=250, y=260)
enter5 = Entry(isc)
enter5.place(x=250, y=320)

lbSearchByName = Label(isc, text="Recherche Nom", font=("Bauhaus 93", 12)).place(x=500, y=105, width=200)
entrySearchByName = Entry(isc)
entrySearchByName.bind("<Return>", SearchByName)
entrySearchByName.place(x=700, y=107, width=165)

bou = Button(isc, text="SAVE", command=save)
bou.place(x=420, y=200, width=80)

bou = Button(isc, text="DELETE", command=sup)
bou.place(x=420, y=240, width=80)

bou = Button(isc, text="QUIT APPS", command=isc.destroy)
bou.place(x=420, y=280, width=80)

tree = ttk.Treeview(isc, columns=(1, 2, 3, 4), heigh=5, show="headings")
tree.place(x=5, y=400, width=500, height=200)
tree.bind("<<TreeviewSelect>>", TreeActionSelect)

tree.heading(1, text="ID")
tree.heading(2, text="NOM")
tree.heading(3, text="PRENOM")
tree.heading(4, text="POSTE")

tree.column(1, width=20)
tree.column(2, width=70)
tree.column(3, width=70)
tree.column(4, width=70)

conn = sqlite3.connect("database.db")
cur = conn.cursor()

req = "CREATE TABLE IF NOT EXISTS controle(ID INTEGER PRIMARY KEY AUTOINCREMENT,nom TEXT NOT NULL,prenom TEXT NOT NULL,poste TEXT NOT NULL,moreinfo TEXT NOT NULL)"
cur.execute(req)

select = cur.execute("select * from controle")
for row in select:
    tree.insert('', END, values=row)

update_time()

isc.mainloop()