from tkinter import *

window = Tk()

Km=0
def mile_km():
    mile = entry.get()
    mile_input=float(mile)
    Km=mile_input*1.609344
    new_km=round(Km,2)
    print(Km)
    lable3.config(text=f'{new_km}')


#Buttons
button = Button(width=20,text="Calculate", command=mile_km)
button.grid(column=1, row=3)
button.config(padx=20,pady=20)

window.title("Miles to KiloMeter Converter")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

lable=Label(text="is equal to")
lable.grid(column=0,row=1)
lable.config(padx=20,pady=20)

lable2=Label(text="Km")
lable2.grid(column=2,row=1)
lable2.config(padx=20,pady=20)

lable1=Label(text="Miles")
lable1.grid(column=2,row=0)
lable1.config(padx=20,pady=20)


lable3=Label(text="0")
lable3.grid(column=1,row=1)


lable3.config(padx=20,pady=20)

#Entries
entry = Entry(width=10)
#Add some text to begin with

#Gets text in entry


entry.grid(column=1, row=0)






window.mainloop()