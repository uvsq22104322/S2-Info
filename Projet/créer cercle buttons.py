import tkinter as tk

racine=tk.Tk()
racine.title("Projet Boulier")

i=0
y=1
x=1

#1er essai:

#def Start():
#    for i in range(136):
#        canvas1.create_oval(x,y, fill="red")
#        if y%8==0:
#                x += 1
#                y += 1
#        else:
#                y += 1
#        i += 1

#2eme essai

def Start():
        pass



canvas1 = tk.Canvas(racine, width=1300, height=700, bg="black", borderwidth=4 )
button1 = tk.Button(racine, text="start", bg="red", command = Start)

canvas1.grid(column=1, row=1, rowspan=9, columnspan=17)
button1.grid(column=0, row=0)


racine.mainloop()


