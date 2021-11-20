# Constants
# Dollar to eur rate
DOLLAR_TO_EUR = 0.98
# Euro to dollar rate
EUR_TO_DOLLAR = 1.13
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60
MILLILITERS_IN_LITER = 1000
# Prices are in Euro
PRICE_1L_MODEL_RESIGN = 165
PRICE_NEW_FORM_3B = 5640
PRICE_NEW_RESIGN_TANK = 165
# Data is in minutes
LIFETIME_RESIGN_TANK = 36000
# Data represents cycles
LIFETIME_PRINTER_PARTS = 2000000

# Calculations
# Price for milliliter of resign
PRICE_PER_MILLILITER_MODEL_RESIGN = PRICE_1L_MODEL_RESIGN / MILLILITERS_IN_LITER

# Price for second of printer work
PRICE_PER_MINUTE_OF_PRINTER_WORK = PRICE_NEW_RESIGN_TANK / (LIFETIME_RESIGN_TANK)

# Price for layer of print
PRICE_PER_LAYER_OF_PRINT = PRICE_NEW_FORM_3B / LIFETIME_PRINTER_PARTS

# All defined languages
languages = [[
        "SLO",
        "POZDRAVLJENI V KALKULATORJU STROSKOV ZA FORMLABS TISKALNIKE\n",
        "Vnesite stevilo plasti: ",
        "Vnesite cas printanja (ure in minute locite s piko): ",
        "Vnesite volumen izdelka v mililitrih: ",
        "Cena printanja je "
    ],
    [
        "ENG",
        "WELCOME TO FORMLABS PRINTER EXPENSES CALCULATOR\n",
        "Enter number of layers: ",
        "Enter print time (seperate hours and minutes with dot): ",
        "Enter print volume in mililiters: ",
        "Print price is "
    ]]
# Function that calculates price of print
def price_calculation(layers, print_time, volume_of_print):
    price = layers * PRICE_PER_LAYER_OF_PRINT
    price += print_time * PRICE_PER_MINUTE_OF_PRINTER_WORK
    price += volume_of_print * PRICE_PER_MILLILITER_MODEL_RESIGN 
    return round(price, 2)

# Function to collect all needed inputs
def collect_inputs(lang):
    global layers
    global print_time 
    global volume_of_print
    # Selected language is slovenian
    if lang == languages[0][0]:
        layers = input(languages[0][2])
        print_time = input(languages[0][3])
        volume_of_print = input(languages[0][4])
    # Language is not supported so default english
    else:
        layers = input(languages[1][2])
        print_time = input(languages[1][3])
        volume_of_print = input(languages[1][4])

# Print of appliction name
def print_app_name(lang):
    line ="____________________________________________________________"
    print(line)
    if lang == languages[0][0]:
        print(languages[0][1] + line + "\n")
    else:
        print(languages[1][1] + line + "\n")

# Calculates time in minutes       
def time_str_to_minutes(print_time):
    # convert string to minutes and hours
    time = print_time.split(".")
    # Check if one or two conditions were entered
    if len(time) == 2:
        return int(time[0]) * MINUTES_IN_HOUR + int(time[1])
    return int(time[0]) * MINUTES_IN_HOUR

# Prints calculated price    
def print_price(lang, cena):
    # Selected language is slovenian
    if lang == languages[0][0]:
        output = languages[0][5] + " " + str(cena)
    else:
        output = languages[1][5] + " " + str(cena)  
    print(output)      

print("Price for milliliter of model resign: " + str(PRICE_PER_MILLILITER_MODEL_RESIGN))
print("Price for minute of print: " + str(PRICE_PER_MINUTE_OF_PRINTER_WORK))
print("Price for layer of print: " + str(PRICE_PER_LAYER_OF_PRINT))

#Languange selection
lang = input("Choose languge (SLO or ENG): ").upper()

print_app_name(lang)
collect_inputs(lang)
minutes = time_str_to_minutes(print_time)
cena = price_calculation(float(layers), float(minutes), float(volume_of_print))
print_price(lang, cena)

