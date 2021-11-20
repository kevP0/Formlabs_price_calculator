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

# Function that calculates price of print
def price_calculation(layers, print_time, volume_of_print):
    price = layers * PRICE_PER_LAYER_OF_PRINT
    price += print_time * PRICE_PER_MINUTE_OF_PRINTER_WORK
    price += volume_of_print * PRICE_PER_MILLILITER_MODEL_RESIGN 
    return round(price, 2)

print("Price for milliliter of model resign: " + str(PRICE_PER_MILLILITER_MODEL_RESIGN))
print("Price for minute of print: " + str(PRICE_PER_MINUTE_OF_PRINTER_WORK))
print("Price for layer of print: " + str(PRICE_PER_LAYER_OF_PRINT))

print("POZDRAVLJENI V KALKULATRJU CENE ZA FORM 3B\n")
print("------------------------------------------\n")

layers = input("Vnesite stevilo plasti: ")
print_time = input("Vnesite cas printanja ure in minute locite s piko: ")
volume_of_print = input("Vnesite volumen izdelka v mililitrih: ")
# convert string to minutes and hours
time = print_time.split(".")
# Check if one or two conditions were entered
if len(time) == 1:
    minutes = int(time[0]) * MINUTES_IN_HOUR + int(time[1])
else:
    minutes = int(time[0]) * MINUTES_IN_HOUR
cena = price_calculation(float(layers), float(minutes), float(volume_of_print))
print("Koncna cena: " + str(cena))

