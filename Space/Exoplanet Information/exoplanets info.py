#CSV
import csv
#Panda
import pandas as pd
#Random
import random
#String
import string

#GLOBAL VARIABLE: CSV FILE
File = 'Exo planet.csv'

#DISPLAY: Goal
print("GOAL: the goal is to make database of knowledge over exoplanets and perhaps stars")

#MENU FUNCTION
def Menu():
    #DISPLAY
    #Menu Info
    print("__________________________\n Welcome and select. . .\n- Exoplanets Section")

    #ITERATION
    while True:
        #INPUT: Inputing Menu
        MenuSelection = input("Select: ").lower().strip()
        #SELECTION: Validating if INPUT fits Information.
        if MenuSelection in ["exoplanet", "exoplanets", "exo", "1","exoplanets section", 'exoplanet section']:
            #CALLING FUNCTION: If INPUT is correct go to the CALLED FUNTION.
            Exoplanets()
            #END LOOP
            break
        #IF INPUT IS EXIT. . .
        elif MenuSelection in ['exit', 'leave', 'exi']:
            #EXIT PROGRAM
            exit()
        #NOT MET: DISPLAY NOT FOUND THEN LOOP
        else:
            print("------------------\nNot found!")

            


#EXOPLANET FUNCTION
def Exoplanets():
    #DISPLAY: EXOPLANET MENU
    print("_______________________\nSelect: \n- Add new information\n- Remove information\n- Read Information\n- Back up Data")

    #INPUT: INPUT ExoPlanet Menu
    Select = input("Select: ").lower().strip()

    #SELECTION: Checking the two menu fits in the INPUT [Select]
    if Select in ['add', 'add new infomation', 'add new', 'a', '1', 'add info', 'add information', 'add new information']:
        #IF ADD: Go to CALLING FUNCTION[Append()]
        Append()
    #ANOTHER CONDITION: IF REMOVE IS TYPED
    elif Select in ['remove', 'remove info', 'remove information', 'r', '2']:
        #CALLING REMOVE FUNCTION: Go to REMOVE FUNCTION
        Remove()
    elif Select in ['read', '3', 'read information']:
        ReadPlanets()
    elif Select in ['back','back up', 'back up data', '4']:
            Save()
    elif Select in ['exit', 'leave', 'exi']:
        exit()
    #IF NOT MET...
    else:
        #DISPLAY: NOT FOUND
        print("----------------\nNot found!")
        

#APPEND FUNCTION
def Append():
    #OPENING CSV FILE TO APPEND
    with open(File, 'a',newline='') as AppendPlanet:
        #SETTING APPEND TO WRITING
        Appending = csv.writer(AppendPlanet)
        
        #LOOP: Loops Input if wanting to redo.
        while True:
            #INPUT EXOPLANET: Add new EXOPLANET
            Exoplanets = input("_______________\nEnter Exoplanet: ").strip().lower()
            #SELECTION: IF REDO IS TYPED FROM INPUT THEN CONTINUE 
            if Exoplanets in ['retype', 'red', '1', 'redo']:
                #CONTINUE: CONTINUES to the next iteration such as going back to Exoplanet and skiping everything
                continue
            #ANOTHER CONDITION IS IF WHEN YOU TYPE EXIT
            elif Exoplanets in ['exit', 'leave', 'leav', 'exi', '2']:
                #RETURNS Nothing so it exits with nothing
                return
            elif Exoplanets in ['menu','3']:
                Menu()
                
            #INPUT DESCRIPTION: Add new DESCRITPTION
            Description = input("Enter Description: ").strip().lower()
            #SELECTION: IF REDO IS TYPED FROM INPUT THEN CONTINUE 
            if Description in ['retype', 'red', '1', 'redo']:
                #CONTINUE: CONTINUES to the next iteration such as going back to Exoplanet and skiping everything
                continue
            #ANOTHER CONDITION IS IF WHEN YOU TYPE EXIT
            elif Description in ['exit', 'leave', 'leav', 'exi', '2']:
                #RETURNS Nothing so it exits with nothing
                return
            
            #INPUT TYPE: Add new TYPE of planet
            Type = input("Enter Type of planet(Like gas or super earth): ").strip().lower()
            #SELECTION: IF REDO IS TYPED FROM INPUT THEN CONTINUE 
            if Type in ['retype', 'red', '1', 'redo']:
                #CONTINUE: CONTINUES to the next iteration such as going back to Exoplanet and skiping everything
                continue
            #ANOTHER CONDITION IS IF WHEN YOU TYPE EXIT
            elif Type in ['exit', 'leave', 'leav', 'exi', '2']:
                #RETURNS Nothing so it exits with nothing
                return
                
            else:
                #LIST: ORGANISE THE INPUT IN A LIST
                AppendList = [Exoplanets,Description,Type]
                #WRITE THE LIST INTO THE CSV
                Appending.writerow(AppendList)
                #DISPLAY: The LIST
                print(f"Here is what is added: {AppendList}")
                #EXIT LOOP
                break

        #INPUT: ASK if you want to redo the FUNCTION again or EXIT
        Redo = input("Do you wish to Exit, Add More or Menu?: ").lower().strip()
        
        if Redo in ['more', 'add', 'add more', '2']:
            Append()
        elif Redo in ['exit', 'leave', 'leav', 'exi', '1']:
            return
        elif Redo in ['menu', 'm', '3']:
            Menu()

        



#REMOVE FUNCTION
def Remove():
    #Open File as read mode
    with open(File,'r') as ChoosingColumn:
        #Set Dictreader
        Reading = csv.DictReader(ChoosingColumn)
        #Fieldnames as reading
        fieldnames = Reading.fieldnames
        #Display Column Exoplanets
        print("Column: Exoplanets")
        #Row turned into list
        rows = list(Reading)
        #input Choosing Column 
        ChoosingColumn = input("Choose Column: ").strip().lower()
        #Exit
        if ChoosingColumn in ['exit', 'leave', 'exi']:
            return
        #Menu
        elif ChoosingColumn in 'menu':
            Menu()
        

        #Picking a line
        PickLine = input("Pick Line: ").strip().lower()
        if PickLine in ['exit', 'leave', 'exi']:
            return
        elif ChoosingColumn in 'menu':
            Menu()

        with open(File,'w',newline='') as Writing:
            Write = csv.DictWriter(Writing,fieldnames=fieldnames)
            
            Write.writeheader()
            for line in rows:
                if PickLine == line.get(ChoosingColumn,''):
                    print("Removed")
                else:
                    Write.writerow(line)


#READ PLANETS
def ReadPlanets():
    print("- Search\n- View all")

    with open('Exo planet.csv', 'r') as C:
        read = csv.DictReader(C)
        Row = list(read)
        i = 1

        # Master 
        Wish = input("Which do you wish: ").strip().lower()
        if Wish in ['exit', 'exi', 'ex']:
            exit()
        elif Wish in 'menu':
            Menu()

        # SELECTION
        # Search
        if Wish in ['search', '1']:
            Search = input("Search: ").strip().lower()
            if Search in ['exit', 'ex', 'exi']:
                exit()
            elif Search in 'menu':
                Menu()

            for line in Row:
                if Search in line['Exoplanets'].lower():
                    print(f"___________________________________\nExoplanet: {line['Exoplanets']}")
                    print(f"_____________________________________________________________________________________________________\nDescription: {line['Description']}")
                    print(f"__________________________\nType: {line['Type']}")

        # View
        elif Wish in ['view', 'view all', '2']:
            for Rows in Row:
                print(f"____________________________________________\n{i}. {Rows}")
                i += 1

        
            





#SAVE FUNCTION
def Save():
        while True:
            try:
                Choice  = input("__________________________________________\nDo you wish to RANDOMISE or CREATE the saved name(Or create Text file): ").strip().lower()
                if Choice in ['create', 'create the saved name', 'create saved name','create names','create name']:
                    CreateName = input("What type of name: ")
                    with open(File,'r') as Old:
                        Read = csv.DictReader(Old)
                        f =[]
                        for line in Read:
                            f.append(line)
                            

                    with open(f'{CreateName}.csv','x',newline='') as create:
                        fieldnames = ['Exoplanets','Description','Type']
                        write = csv.DictWriter(create,fieldnames=fieldnames)
                        write.writeheader()
                        write.writerows(f)
                    break
                
                elif Choice in 'randomise':
                    with open(File,'r') as Old:
                        Read = csv.DictReader(Old)
                        f =[]
                        for line in Read:
                            f.append(line)
                    New_File = random.uniform(1,1000)

                    with open(f'{New_File}_SaveData.csv','x',newline='') as RandomFloat:
                        fieldnames = ['Exoplanets','Description','Type']
                        write = csv.DictWriter(RandomFloat,fieldnames=fieldnames)
                        write.writeheader()
                        write.writerows(f)
                        print(f"Successfully changed to {New_File}_SaveData.csv")
                    break

                elif Choice in 'random':
                    List=['Great Planets','Exoplanet', 'EXO','EXOPLANETS','Exo', 'Planets', 'Nasa Database','Saved Database']
                    
                    Value = random.choice(List)

                    with open(f'{Value}_SaveData.csv','x',newline='') as Rand:
                        fieldnames = ['Exoplanets','Description','Type']
                        write = csv.DictWriter(Rand,fieldnames=fieldnames)
                        write.writeheader()
                        write.writerows(f)
                        print(f"Successfully changed to {Value}_SaveData.csv")
                    break

                elif Choice in ['txt','text','text file']:
                    Createorenter = input("Random or Create: ").strip().lower()
                    if Createorenter in ['random', '1']:
                        with open(File,'r') as Old:
                            Read = csv.DictReader(Old)
                            f =[]
                            for line in Read:
                                f.append(line)
                                
                        Il =  random.uniform(1,90)
                        with open(f'{Il}_SavedData.txt','x') as Txt:
                            fieldnames = ['Exoplanets','Description','Type']
                            wrtin = csv.DictWriter(Txt,delimiter=',',fieldnames=fieldnames)
                            wrtin.writeheader()
                            wrtin.writerows(f)
                            print(f"___________________\nSuccessful\nName: {Il}_SavedData.txt")
                            break
                    elif Createorenter in ['create','2']:
                        with open(File,'r') as Old:
                            Read = csv.DictReader(Old)
                            f =[]
                            for line in Read:
                                f.append(line)
                            Creating = input("Create Name: ")
                            with open(f'{Creating}.txt','x') as Txt:
                                fieldnames = ['Exoplanets','Description','Type']
                                wrtin = csv.DictWriter(Txt,delimiter=',',fieldnames=fieldnames)
                                wrtin.writeheader()
                                wrtin.writerows(f)
                                print(f"___________________\nSuccessful\nName: {Creating}.txt")
                                break
                else:
                    print("No file was made.")
            except(FileExistsError):
                print(f"Error: {FileExistsError}")


#Start
Menu()

