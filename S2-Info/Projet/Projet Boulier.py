import tkinter as tk

racine=tk.Tk()

canvas1 = tk.Canvas(racine, width=1000, height=450, bg="black", borderwidth=5 )
buttonClear = tk.Button(racine, text="Réinitialiser", bg="red",relief="sunken") #, command=Clear #à faire)
button1_1 = tk.Button(racine, text="test", bg="red")
button1_5 = tk.Button(racine, text="test", bg="red")
button1_6 = tk.Button(racine, text="test", bg="red")
button1_7 = tk.Button(racine, text="test", bg="red")
button1_8 = tk.Button(racine, text="test", bg="red")
button1_9 = tk.Button(racine, text="test", bg="red")
button2_1 = tk.Button(racine, text="test", bg="red")
button2_5 = tk.Button(racine, text="test", bg="red")
button2_6 = tk.Button(racine, text="test", bg="red")
button2_7 = tk.Button(racine, text="test", bg="red")
button2_8 = tk.Button(racine, text="test", bg="red")
button2_9 = tk.Button(racine, text="test", bg="red")
button3_1 = tk.Button(racine, text="test", bg="red")
button3_5 = tk.Button(racine, text="test", bg="red")
button3_6 = tk.Button(racine, text="test", bg="red")
button3_7 = tk.Button(racine, text="test", bg="red")
button3_8 = tk.Button(racine, text="test", bg="red")
button3_9 = tk.Button(racine, text="test", bg="red")
button4_1 = tk.Button(racine, text="test", bg="red")
button4_5 = tk.Button(racine, text="test", bg="red")
button4_6 = tk.Button(racine, text="test", bg="red")
button4_7 = tk.Button(racine, text="test", bg="red")
button4_8 = tk.Button(racine, text="test", bg="red")
button4_9 = tk.Button(racine, text="test", bg="red")
button5_1 = tk.Button(racine, text="test", bg="red")







canvas1.grid(column=1, row=1, rowspan=16, columnspan=8)
buttonClear.grid(column= 0, row=1)
button1_1.grid(column = 1, row=1)
button1_5.grid(column = 1, row=5)
button1_6.grid(column = 1, row=6)
button1_7.grid(column = 1, row=7)
button1_8.grid(column = 1, row=8)
button1_9.grid(column = 1, row=9)
button2_1.grid(column = 2, row=1)
button2_5.grid(column = 2, row=5)
button2_6.grid(column = 2, row=6)
button2_7.grid(column = 2, row=7)
button2_8.grid(column = 2, row=8)
button2_9.grid(column = 2, row=9)
button3_1.grid(column = 3, row=1)
button3_5.grid(column = 3, row=5)
button3_6.grid(column = 3, row=6)
button3_7.grid(column = 3, row=7)
button3_8.grid(column = 3, row=8)
button3_9.grid(column = 3, row=9)
button4_1.grid(column = 4, row=1)
button4_5.grid(column = 4, row=5)




racine.mainloop()