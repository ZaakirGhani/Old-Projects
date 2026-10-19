import csv

def remove_product():
    SelectProduct = input("Select Name: ")
    #list
    rows = []

    # Read the CSV file
    with open('CSV.csv', 'r') as D:
        #Intiating csv reader but dictianary
        Read = csv.DictReader(D)
        #incrementing dictianary reader 
        for line in Read:
            #If user input is equal to select csv name in its file
            if line['Name'] == SelectProduct:
                #If this this is true then input if you want to remove face
                Remove = input("Do you wish to remove: ")
                #if user input yes then do:
                if Remove == "yes":
                    #Change face to out of stock
                    line['face'] = 'Out of Stock'
            #Appending all dictionary reader so that it will overwrite only what is needed to overwrite
            rows.append(line)

    # Write the updated rows back to the CSV file
    with open('CSV.csv', 'w', newline='') as DW:
        #Intiating the header
        fieldnames = ['Name', 'face']  # Define the field names directly
        #creating a dictianory writer
        WRITING = csv.DictWriter(DW, fieldnames=fieldnames)
        #When overwritten rewrite the fieldnames 
        WRITING.writeheader()
        #rewrite the all the rows except of append and change selected face out of stock
        WRITING.writerows(rows)
        
    print(f"Successful update: {rows}.")

remove_product()