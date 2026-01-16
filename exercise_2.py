#Name: Irish B. De Guzman
#Date: October 25, 2025
#Title: Exercise 2 - Receipt

def run_exercise_2():
    print("<<<<<<<<<<<<<<<< FINE DINING SNACK BAR >>>>>>>>>>>>>>>\n\n\t\t\t\b\b\bMenu for Today\n")
    print("Hot Dog\t\t\t\t\t\bPhp 45.50\nHamburger\t\t\t\t\t\b\b\b\b\b35.75\nFrench Fries\t\t\t\t\t\b\b\b\b\b25.85\nMilk Shake\t\t\t\t\t\b\b\b\b\b15.75\n")
    print("--------------------------------------------------------")
    #input the quantity per item
    hotdog = int(input("Enter quantity of Hot Dog: "))
    hamburger = int(input("Enter quantity of Hamburger: "))
    frenchFries = int(input("Enter quantity of French Fries: "))
    milkShake = int(input("Enter quantity of Milk Shake: "))

    #multiplies the price and quantity per item
    total_hotdog = 45.50 * hotdog
    total_hamburger = 35.75 * hamburger
    total_frenchFries = 25.85 * frenchFries
    total_milkShake = 15.75 * milkShake

    #rounds off the total price per item to the nearest hundreths
    roundedTotalHotdog = round(total_hotdog, 2)
    roundedTotalHamburger = round(total_hamburger, 2)
    roundedTotalFrenchFries = round(total_frenchFries, 2)
    roundedTotalMilkShake = round(total_milkShake, 2)

    #calculates the gross price
    grossPrice = roundedTotalHotdog + roundedTotalHamburger + roundedTotalFrenchFries + roundedTotalMilkShake

    #rounds off the gross price to the nearest hundreths
    roundedGrossPrice = round(grossPrice, 2)

    #calculates the VAT
    vat = roundedGrossPrice * 0.2

    #rounds off the VAT to the nearest hundreths
    roundedVat = round(vat, 2)

    #calculates the total price
    totalPrice = roundedGrossPrice + roundedVat

    #rounds off the total price to the nearest hundreths   
    roundedTotalPrice = round(totalPrice, 2)

    #calculates the total number of items sold
    numberOfItemsSold = hotdog + hamburger + frenchFries + milkShake
    print("\n\n<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

    #outputs the quantity and price per item
    print(f"Hotdog\t\t\tPhp 45.50 x {hotdog} = Php {roundedTotalHotdog}")
    print(f"Hamburger\t\tPhp 35.75 x {hamburger} = Php {roundedTotalHamburger}")
    print(f"French Fries\t\tPhp 25.85 x {frenchFries} = Php {roundedTotalFrenchFries}")
    print(f"Milk Shake\t\tPhp 15.75 x {milkShake} = Php {roundedTotalMilkShake} \n\n")

    #outputs the gross price
    print(f"Gross Price\t\t\t\t\b\b\b = Php {roundedGrossPrice}")

    #outputs the VAT
    print(f"(w/VAT)\t\t\t\t\t\b\b\b = Php {roundedVat}")

    #outputs the total price
    print(f"Total Price\t\t\t\t\b\b\b = Php {roundedTotalPrice}\n")

    #inputs the amount tendered
    amountTendered = float(input("Enter amount tendered: "))

    #calculates the change
    change = amountTendered - totalPrice

    #rounds off the change to nearest hundreths
    roundedChange = round(change, 2)

    #outputs the amount tendered
    print(f"Amount Tendered\t\t\t\t\b\b\b = Php {amountTendered}")

    #outputs the change
    print(f"Your change is\t\t\t\t\b\b\b = Php {roundedChange}")

    print("\t\t\t\t\t\b\bvvvvvvvvvvvv")

    #outputs the total number of items sold
    print(f"Number of items sold: {numberOfItemsSold} items\n")

    print("************** THANK YOU AND COME AGAIN **************")