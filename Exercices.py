from tkinter import*

isc=Tk()
isc.geometry("600x600")

lbl1=Label(isc,text="FORMULAIRE")
lbl1.place(x=280,y=40)

lbl2=Label(isc,text="MATRICULE")
lbl2.place(x=40,y=150)

lbl3=Label(isc,text="NOM")
lbl3.place(x=40,y=210)

lbl4=Label(isc,text="POST NOM")
lbl4.place(x=40,y=270)

lbl5=Label(isc,text="PRENOM")
lbl5.place(x=40,y=330)

lbl6=Label(isc,text="SEXE")
lbl6.place(x=40,y=390)

enter1=Entry(isc)
enter1.place(x=300,y=150)

enter2=Entry(isc)
enter2.place(x=300,y=210)

enter3=Entry(isc)
enter3.place(x=300,y=270)

enter4=Entry(isc)
enter4.place(x=300,y=330)

enter5=Entry(isc)
enter5.place(x=300,y=390)

bou1=Button(isc,text="SAVE")
bou1.place(x=150,y=490)

bou2=Button(isc,text="SAVE")
bou2.place(x=350,y=490)


isc.mainloop()
