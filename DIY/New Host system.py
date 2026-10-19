#NewHostsystem
#Import CSV libary
import csv

#CSV path(Database)
file_Directory = 'D.csv'

#MAIN MENU
def Menu():
#Option varibles
    a = 1
    b = 2
    c = 3
    d = 4

#Diplaying options
    print("1.Search Product")
    print("2.Remove Product")
    print("3.Add Product")
    print("4.Exit")
    print("___________________")

#Checking options are correct and inputing option. 
    try:
        Choose = int(input("Select: "))
        if Choose == a:
            print("___________________________")
            Search_Product()
        elif Choose == b:
            print("__________________")
            Remove_Product()
        elif Choose == c:
            print("__________________")
            Add_Product()
        elif Choose == d:
            exit()
        else:
            print("Thats not an option!")
    except(ValueError):
        print(f"Error: Invalid Input!\nInformation: {ValueError}")
            

#SEARCH PRODUCT
def Search_Product():

    print("you can type 'exit' to leave")
    print("_____________________________")
    #To search through csv
    search = input("Search Product Name or ID: ")

    #read throught csv
    with open(file_Directory,'r') as ProductSearch:
        #Establish csv as dictionary
        Reader = csv.DictReader(ProductSearch)
        for line in Reader:
            #Find name or ID to give information or exit
            if search in line['Product ID']:
                print(f"Infomation\nItem: {line['Product Name']}")
                print(f"Location: {line['Location']}")
                print(f"Quantity: {line['Quantity']}")
                print("-----------------------------")
                Enter = input("Press Enter:")
                MenuorExit()
            elif search in line['Product Name'].lower():
                print(f"Infomation\nItem: {line['Product Name']}")
                print(f"Location: {line['Location']}")
                print(f"Quantity: {line['Quantity']}")
                print("-----------------------------")
                Enter = input("Press Enter:")
                MenuorExit()
            elif search == 'exit':
                exit()
            elif search == 'menu':
                    Menu()
                
                
    
#REMOVING QUANTITY OF PRODUCTS
def Remove_Product():
    #List
    Row = []
    print("------------------------------")
    print("you can type 'exit' to leave")
    print("------------------------------")
    
    SelectProduct = input("Select Product: ")

    found = False

    #Read file
    with open (file_Directory, 'r') as ProductData:
        #Establish csv to read dictianary object
        ReadData = csv.DictReader(ProductData)
        #Incrementing CSV line by line 
        for Line in ReadData:
            #Finding User fits Product ID or Name
            if Line['Product ID'] == SelectProduct:
                #If this is the case do the user want to remove it
                Remove = input("Do you wish to remove quantity of this product: ")
                #If you say yes then...
                if Remove == 'yes':
                    #Quantity selected will be out of stock
                    Line['Quantity'] = 'Out Of Stock'
                    found =True
                #If no then...
                elif Remove == 'no':
                    print("___________________")
                    print("Remove Quantity")
                    #Back to remove product
                    Remove_Product()
                 #Exit
                elif Remove == 'exit':
                    exit()
                 #Menu
                elif Remove == 'menu':
                    Menu()
            elif Line['Product Name'].lower() == SelectProduct:
                #If this is the case do the user want to remove it
                Remove = input("Do you wish to remove quantity of this product: ")
                #If you say yes then...
                if Remove == 'yes':
                    #Quantity selected will be out of stock
                    Line['Quantity'] = 'Out Of Stock'
                    found =True
                #If no then...
                elif Remove == 'no':
                    print("___________________")
                    print("Remove Quantity")
                    #Back to remove product
                    Remove_Product()
                #Exit
                elif Remove == 'exit':
                    exit()
                elif Remove == 'menu':
                    Menu()
                    
            elif SelectProduct == 'exit':
                exit()
            elif SelectProduct == 'menu':
                    Menu()
            #Appending or updating new information along with the file
            Row.append(Line)

    if found:
        with open (file_Directory, 'w', newline='') as WritingProduct:
            fieldnames = ['Product ID', 'Product Name', 'Location', 'Quantity']
            WriteData = csv.DictWriter(WritingProduct, fieldnames=fieldnames)
            WriteData.writeheader()
            WriteData.writerows(Row)
        print(f"Successful:\n{SelectProduct}: Out of stock")
        print("===========================")
    else:
        print("Error: incorrect spelling!")
        Remove_Product()

    #Menu or exit
    MenuorExit()



#ADDING NEW PRODUCTS
def Add_Product():
    #Product ID
    ProductID = input("Enter New Product ID(Seven Digits): ")
    #Check if Product ID has seven numbers
    if len(ProductID) == 7 and ProductID.isnumeric() == True:
        pass
    elif ProductID == 'exit':
            exit()
    else:
        print("_________________________")
        print("Invalid length or characters")
        ProductID = input("Reenter(Seven Digit number): ")

    ProductName = input("Enter new Product name: ")
    while True:    
        if ProductName.isalpha() == True:
            break
        elif ProductName == 'exit':
            exit()
        else:
            print("Name can only be in letters")
            ProductName = input("Reenter Name: ")

    Location = input("Enter Location: ")
    
    while True:
            #Make sure length, number and letters. 
        if len(Location) < 4 and Location.isalnum() == True:
                #Break that allows access
            break
        elif Location == 'exit':
                exit()
        else:
            print("_________________________")
            #Reenter
            print("Invalid length or characters(example: Section A1 - A32)")
            Location = input("Reenter Warehouse Location: ")

    
   #Making sure its only numbers
    Quantity = int(input("Enter Quantity: "))


    #Inputs in a list
    ListDataBase = [ProductID,ProductName,Location,Quantity]

    #CSV appending
    with open(file_Directory,'a', newline='') as Appending:
        #CSV set as writer
        Writer = csv.writer(Appending)
        #Writing Input list into csv
        Writer.writerow(ListDataBase)
        print(f"Successful.\n{ListDataBase}")
        print("===========================")

    #Menu or exit
    MenuorExit()



#MENU AND EXIT SCREEN
def MenuorExit():
    print("1.Menu\n2.Exit")
    SelectMENUorEXIT = int(input("Select: "))
    a = 1
    b = 2
    if SelectMENUorEXIT == a:
        print("__________________")
        Menu()
    elif SelectMENUorEXIT == b:
        exit()
    else:
        exit()



#Start with Menu
Menu()