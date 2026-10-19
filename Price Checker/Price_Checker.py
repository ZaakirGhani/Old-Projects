#Intiate CSv
import csv

#File name/directory
file = 'RD.csv'

#Function to search prices
def Comparing_Prices():
    #Introducting System
    print("Welecome to TechHaven")
    print("Type 'exit' to exit")
    #Enter ID
    Search = input('Enter ID: ')

    #Open CSV file Database to read
    with open(file, 'r') as Database:

        #Making it a dictionary reader
        reader = csv.DictReader(Database)

        #Iterating reader showing the real value
        for line in reader:
            
            #Establishing ID varible
            ID = line['ID']

            #Original Prices
            AsdaOriginalPrice = float(line['A original price'])
            TechHavenOriginalPrice = float(line['LR original price'])
            CEXOriginalPrices = float(line['P original price'])
            
            #Percentage Discounts
            AsdaDicount = float(line['A Discount'])
            TechHavenDiscount = float(line['LR Discount'])
            CEXDiscount = float(line['P Discount'])
            
            #Calculating Discounts
            A_Discount = AsdaDicount * AsdaOriginalPrice
            Th_Discount = TechHavenDiscount * TechHavenOriginalPrice
            C_Discount = CEXDiscount * CEXOriginalPrices
            
            #Original - Discounts
            AsdaTotalDis = AsdaOriginalPrice - A_Discount
            TechHavenTotalDis = TechHavenOriginalPrice - Th_Discount
            CEXTotalDis = CEXOriginalPrices - C_Discount
            
            #Rounding total Discount
            DiscountAsdaRound = round(AsdaTotalDis,2)
            DiscountTechHavenRound = round(TechHavenTotalDis,2)
            DiscountCEXRound = round(CEXTotalDis,2)

            #Checking if search ID is correct
            if Search == ID:
                #Tech Haven
                print(f'TECH HAVEN\n {line['LR']}\n  TECH HAVEN Original Price: £{(TechHavenOriginalPrice)}\n  TECH HAVEN Discount: £{DiscountTechHavenRound}')
                
                #Asda
                print(f"\nASDA\n {line['A']}\n  ASDA Original Price: £{(AsdaOriginalPrice)}\n  ASDA Discount: £{DiscountAsdaRound}")

                #CEX
                print(f"\nCEX\n {line['P']}\n  CEX Original Price: £{(CEXOriginalPrices)}\n  CEX Discount: £{DiscountCEXRound}")


                #Break so it doesn't iterate
                break
            #When typing exit the functions exit
            elif Search == 'exit':
                exit()
        
        #If search is not correct then say ID is not found
        if Search != ID:
            print("ID not found")
            #Go back menu Function Intiated
            Backto()
                            

#Go back to menu function
def Backto():
    #Enter yes or not if you want to go back
    Back = input("Do you wish to go back(yes or no): ")
    #Condition if yes
    if Back == 'yes':
        #Then go back to menu
        Comparing_Prices()
    #No exit
    elif Back == 'no':
        exit()
    #If invalid input then exit 
    else:
        exit()

#CALLING OUT FUNCTION
Comparing_Prices()