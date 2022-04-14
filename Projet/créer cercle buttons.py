import tkinter as tk

racine=tk.Tk()
racine.title("Projet Boulier")

i=0
y=1
x=1
def Start():
    while i < 136:
        canvas1.create_oval("les attributs jsais plus lequel avec genre x et y")
        if y%8==0:
                x += 1 
        i += 1


canvas1 = tk.Canvas(racine, width=1300, height=700, bg="black", borderwidth=4 )
button1 = tk.Button(racine, text="start", bg="red", command = Start)

canvas1.grid(column=1, row=1, rowspan=9, columnspan=17)
button1.grid(column=0, row=0)


racine.mainloop()


