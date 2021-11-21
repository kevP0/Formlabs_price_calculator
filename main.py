from tkinter import *
from tkinter import ttk
from PrintPriceCalculator import *

# Function that prints price
def print_price(lang):
    try:
        layers = float(e1_layers.get())
        hours = float(e2_1_minutes.get())
        minutes = float(e2_hours.get()) + hours * MINUTES_IN_HOUR
        volume_of_print = float(e3_mL.get())
        price = price_calculation(layers, minutes, volume_of_print)
        l9 = Label(root, text = str(price))
        l9.grid(row=8,column=6)
    except:
        print("Fields are empty")
        
    
# Function translates all text to choosen language
def translate_text(self):
    if self == "SLO":
        window_clean()
        window_setup(0)
    else:
        window_clean()
        window_setup(1)
        
        
#Removes all widgets
def window_clean():
    l1.grid_remove()
    l2.grid_remove()
    l2_1.grid_remove()
    l2_2.grid_remove()
    l3.grid_remove()
    l3_1.grid_remove()
    l4.grid_remove()
    l5.grid_remove()
    l6.grid_remove()
    l7.grid_remove()
    l8.grid_remove()

    e1_layers.grid_remove()
    e2_hours.grid_remove()
    e2_1_minutes.grid_remove()
    e3_mL.grid_remove()

    b1.grid_remove()
    
    
# Sets up all widgets
def window_setup(lang):
    # We make all global
    global l1
    global l2
    global l2_1
    global l2_2
    global l3
    global l3_1
    global l4
    global l5
    global l6
    global l7
    global l8
    global e1_layers
    global e2_hours
    global e2_1_minutes
    global e3_mL
    global b1
    #Specify text style    
    T = Text(root, height=5, width=52)

    # Create label
    l1 = Label(root, text = languages[lang][2])
    l2 = Label(root, text = languages[lang][3])
    l2_1 = Label(root, text = languages[lang][10])
    l2_2 = Label(root, text = languages[lang][11])
    l3 = Label(root, text = languages[lang][4])
    l3_1 = Label(root, text = "mL")

    l4 = Label(root, text = " ")
    l5 = Label(root, text = languages[lang][6] + str(round(PRICE_PER_MILLILITER_MODEL_RESIGN, 3)))
    l6 = Label(root, text = languages[lang][7] + str(round(PRICE_PER_MINUTE_OF_PRINTER_WORK, 5)))
    l7 = Label(root, text = languages[lang][8] + str(round(PRICE_PER_LAYER_OF_PRINT, 5)))
    
    l8 = Label(root, text = languages[lang][5])

    # Create entry widgets
    e1_layers = Entry(root)
    e2_hours = Entry(root)
    e2_1_minutes = Entry(root)
    e3_mL = Entry(root)

    # Create button to start calculation
    b1 = ttk.Button(root, text = languages[lang][9], command = lambda: print_price(lang))

    # Add all widgets to screen
    l1.grid(row=1,column=0)
    l2.grid(row=2,column=0)
    l2_1.grid(row=2,column=2)
    l2_2.grid(row=2,column=4)
    l3.grid(row=3,column=0)
    l3_1.grid(row=3,column=2)
    l4.grid(row=4,column=0)
    l5.grid(row=5,column=0)
    l6.grid(row=6,column=0)
    l7.grid(row=7,column=0)
    l8.grid(row=8, column=5)

    e1_layers.grid(row=1,column=1)
    e2_hours.grid(row=2,column=1)
    e2_1_minutes.grid(row=2,column=3)
    e3_mL.grid(row=3,column=1)

    b1.grid(row=4,column=5)
    
  
#MAIN  
# dropdown variables
language = ["SLO", "ENG"]

# holds number for language
# 0 = SLO
# 1 = ENG
lang = 0

root = Tk()
root.title("Form Price Calculator")

# Get screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Addapt window size to screen size
if (screen_width < 1000) or (screen_height < 500):
    window_size = str(screen_width)+"x"+str(scree_height)
else:
    window_size = "1000x500"
root.geometry(window_size)

# We set all text on window
window_setup(lang)

# Create language select dropdown
clicked = StringVar()
clicked.set("SLO")
drop = OptionMenu(root, clicked, *language, command = translate_text)
drop.grid(row=6, column=5)

root.mainloop()