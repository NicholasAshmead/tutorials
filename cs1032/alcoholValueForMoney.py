def __alcoholPerPence(alcoholPercent, volume, price):
    # alcoholPercent is a percentage, in the form 0.5 for 50%
    # volume is in millilitres
    # price is in pence, so £3.99 is 399
    # returns the number of millilitres of alcohol per pence
    return (alcoholPercent * volume) / price

def __valueSanitiser(alcoholPercent, volume, price):
    if not(alcoholPercent < 1 and alcoholPercent > 0):
        alcoholPercent /= 100
        if alcoholPercent > 1 or alcoholPercent < 0:
            return False
    if not(volume > 0):
        return False
    if not(price > 0):
        return False
    return __alcoholPerPence(alcoholPercent, volume, price)

def alcoholValueForMoney(alcoholPercent, volume, price):
    return __valueSanitiser(alcoholPercent, volume, price)

#print(alcoholValueForMoney(0.05, 3960, 1045))

import argparse
parser = argparse.ArgumentParser(description="Calculate the alcohol value for money of a drink")
parser.add_argument("alcoholPercent", type=float, help="The percentage of alcohol in the drink")
parser.add_argument("volume", type=int, help="The volume of the drink in millilitres")
parser.add_argument("price", type=int, help="The price of the drink in pence")
args = parser.parse_args()

print(alcoholValueForMoney(args.alcoholPercent, args.volume, args.price))