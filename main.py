from tkinter import *
from tkinter.ttk import *

def prediction_make(melting_point, conduct_solid, conduct_liquid):
    print(melting_point, conduct_solid, conduct_liquid)
    melting_point = int(melting_point)
    if conduct_solid == "Yes":
        conduct_solid = True
    else:
        conduct_solid = False

    if conduct_liquid == "Yes":
        conduct_liquid = True
    else:
        conduct_liquid = False
    
    print(melting_point, conduct_solid, conduct_liquid)
    if conduct_solid and conduct_liquid:
        return 3
    elif conduct_liquid and not conduct_solid:
        return 0
    elif not conduct_solid and not conduct_liquid and melting_point < 1000:
        return 1
    else:
        return 2

root = Tk()
root.title("Box")
root.geometry('300x150')

melting_lbl = Label(root, text = "Melting Point = ")
melting_lbl.grid(column = 0, row = 0)
melting_txt = Entry(root, width = 10)
melting_txt.grid(column = 1, row = 0)

conduct_solid_lbl = Label(root, text = "Conducts as solid?")
conduct_solid_combo = Combobox(root)
conduct_solid_combo['values'] = ('Yes', 'No')
conduct_solid_combo.current(1)
conduct_solid_lbl.grid(column = 0, row = 1)
conduct_solid_combo.grid(column = 1, row = 1)

conduct_liquid_lbl = Label(root, text = "Conducts as liquid?")
conduct_liquid_combo = Combobox(root)
conduct_liquid_combo['values'] = ('Yes', 'No')
conduct_liquid_combo.current(1)
conduct_liquid_lbl.grid(column = 0, row = 2)
conduct_liquid_combo.grid(column = 1, row = 2)

prediction_choices = ["Ionic", "Simple Molecular", "Giant Molecular", "Metallic"]
prediction = " "
global index
index = 0

def pressed():
    predict_lbl.configure(text = str(prediction_choices[prediction_make(melting_txt.get(), conduct_solid_combo.get(), conduct_liquid_combo.get())]))


calc_button = Button(root, text = 'Predict', command = pressed)
calc_button.grid(column = 1, row = 3) 

predict_lbl = Label(root, text = str(prediction))
predict_lbl.grid(column = 1, row = 4)

root.mainloop()
