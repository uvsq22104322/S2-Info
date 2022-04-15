import tkinter as tk

DIM_BOULIER = (17,9)
WIDTH = 1300
HEIGHT = 700
ecart_width = WIDTH/DIM_BOULIER[0]
ecart_height = HEIGHT/DIM_BOULIER[1]
boules = []

def clic(event):
    x, y = event.x, event.y
    print("Clic en",x,",",y)
    print(canvas1.find_closest(x,y)," est l'objet cliqué.")



racine=tk.Tk()
racine.title("Projet Boulier")

canvas1 = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg="black", borderwidth=4 )

#Création des boules

def Start():
    for x in range(DIM_BOULIER[0]):
        for y in range(DIM_BOULIER[1]):
            if y == 1 or y == 3:
                canvas1.create_oval(x*ecart_width,y*ecart_height,x*ecart_width+ecart_width,y*ecart_height+ecart_height,fill="gray",tags="boules")
            elif y == 2:
                if y == 2 and x%3 == 1 :
                    canvas1.create_oval(x*ecart_width,y*ecart_height,x*ecart_width+ecart_width,y*ecart_height+ecart_height,fill="white")
                else :
                    canvas1.create_oval(x*ecart_width,y*ecart_height,x*ecart_width+ecart_width,y*ecart_height+ecart_height,fill="black")
            else:
                canvas1.create_oval(x*ecart_width,y*ecart_height,x*ecart_width+ecart_width,y*ecart_height+ecart_height,fill="red",tags="boules")
#        boules = boules.append()

#def Clear():
#    list = racine.grid()
#    for l in list:
#        l.destroy()

button1 = tk.Button(racine, text="start", bg="red", command = Start)
#button2 = tk.Canvas(racine, text="Clear", bg="red") #command = Clear

canvas1.grid(column=1, row=1, rowspan=9, columnspan=17)
button1.grid(column=0, row=0)
#button2.grid(column=0, row=1)
canvas1.tag_bind("boules","<Button-1>",clic)

racine.mainloop()