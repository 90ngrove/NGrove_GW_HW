# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases
Pecan =0
AppleCrisp =0
Bean =0
Banoffee=0
BlackBun =0
Blueberry =0
Buko =0
Burek =0
Tamale =0
Steak =0
# Pie List
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

# Display initial message
print("Welcome to the House of Pies! Here are our pies:")

# While we are still shopping...
while shopping == "y":

    # Show pie selection prompt

    print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
          " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
          " (9) Tamale, (10) Steak ")
    pie_choice = int(input("Which pie would you like? Please enter a number."))
    if pie_list[int(pie_choice) - 1] == "Pecan":
        Pecan = Pecan+1
    elif pie_list[int(pie_choice) - 1] == "Apple Crisp":
        AppleCrisp = AppleCrisp+1
    elif pie_list[int(pie_choice) - 1] == "Bean":
        Bean = Bean+1
    elif pie_list[int(pie_choice) - 1] == "Banoffee":
        Banoffee = Banoffee+1
    elif pie_list[int(pie_choice) - 1] == "Black Bun":
        BlackBun = BlackBun+1
    elif pie_list[int(pie_choice) - 1] == "Blueberry":
        Blueberry = Blueberry+1
    elif pie_list[int(pie_choice) - 1] == "Buko":
        Buko = Buko+1
    elif pie_list[int(pie_choice) - 1] == "Burek":
        Burek = Burek+1
    elif pie_list[int(pie_choice) - 1] == "Tamale":
        Tamale = Tamale+1
    elif pie_list[int(pie_choice) - 1] == "Steak":
        Steak = Steak+1


    print("Great! We'll have that " + pie_list[int(pie_choice) - 1] + " right out for you.")
    
    # Provide exit option
    shopping = input("Would you like to make another purchase: (y)es or (n)o? ")

print("You ordered: ")
print (str(Pecan) +" Pecan")
print (str(AppleCrisp) +" Apple Crisp")
print (str(Bean) +" Bean")
print (str(Banoffee) +" Banoffee")
print (str(BlackBun) +" BlackBun")
print (str(Blueberry) +" Blueberry")
print (str(Buko) +" Buko")
print (str(Burek) +" Burek")
print (str(Tamale) +" Tamale")
print (str(Steak) +" Steak")
