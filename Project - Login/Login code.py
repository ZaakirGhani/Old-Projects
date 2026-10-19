#Intention - to now create a login system that uses a database to search for people using CSV file.

#Common Phrases Bank(CPB)
Access_Phrase = "Access Granted!!"
Try_Again_Phrase = "Try Again!!"
Welcome = "Welcome"
Hello = "Hello,"
No_Punctuation_Spaces = "We do not accept punctuations and spaces (Only numbers and letters)."
Enter_USERNAME_Again = "Please enter username again!!"
IncorrectPASS = "Incorrect Password!!"

#Design
#Brake Spaces Type 1
Line_Break_Large = "------------------------------------------------------------------"
Line_Break_Medium = "----------------------------------"
Line_Break_Small = "--------"
Line_Break_ExtraSmall = "---"
#Break Spaces Type 2
DoubleLine_Break_Large = "============================================================"
DoubleLine_Break_Medium = "=============================="
DoubleLine_Break_Small = "========"
DoubleLine_Break_ExtraSmall = "==="
#Break Spaces Type 3
ConnectedLine_Large = "________________________________________________________________"
ConnectedLine_Medium = "_______________________________"
ConnectedLine_Small = "_________"
ConnectedLine_ExtraSmall = "___"
#Break Spaces Type 4
HashtagLine_Large = "###################################################################"
HashtagLine_Medium ="#################################"
HashtagLine_Small = "#############"
HashtagLine_ExtraSmall = '####'
#Emotion
Smile = ":)"
Sad = ":("


#(The Login Module(TLM))
def Login():
#Name
        #Tool Property(TP): Loop, Asking(input) - Selection - Setting Boundaries (Only words)  
        #Tool Keywords(TK): WHILE, INPUT, IF, ISALPHA()
        while True:
            Name = input("Enter your first name: ").strip().lower()
            if Name.isalpha() == False:
                print("Please enter a valid name.")
            elif Name in ['exit','exi','leave']:
                return
            else:
                print(Welcome, Name.capitalize() + "!")
                break
        

#Username
        #Tool Property(TP): Loop, Asking(input) - Selection - Setting Boundaries (Only numbers/words)  
        #Tool Keywords(TK): WHILE, INPUT, IF, ISALNUM()
        while True:
            Username = input("Enter Username: ")
            if Username.isalnum() == False:
                print(No_Punctuation_Spaces.upper(), Enter_USERNAME_Again.upper())
            else:
                print(Hello, Username + "!")
                break

#Email
        #Tool Property(TP): Loop, Asking(input) - Selection
        #Tool Keywords(TK): WHILE, INPUT, IF, ELIF, ELSE, IN
        while True:
            Email = input("Enter in an email address: ")
            if  "@gmail.com" in Email:
                print(Access_Phrase,'\n' + Email)
                print(Line_Break_Large)
                break
            elif "@hotmail.com" in Email:
                print(Access_Phrase,'\n' +  Email)
                print(Line_Break_Large)
                break
            elif "@outlook.com" in Email:
                print(Access_Phrase,'\n'+  Email)
                print(Line_Break_Large)
                break
            elif "@icloud.com" in Email:
                print(Access_Phrase,'\n'+  Email)
                print(Line_Break_Large)
                break
            elif "@yahoo.com" in Email:
                print(Access_Phrase,'\n'+  Email)
                print(Line_Break_Large)
                break
            else:
                print("Incorrect email address!!")

#Password
        #Tool Property(TP): Loop until 3 tries, Asking(input) - Selection - Input must be linked to first input
        #Tool Keywords(TK): FOR, WHILE, RANGE(), INPUT, IF, ELIF
        
        NumPass = 3
        Length_Check = 8
        while True:
            Password_SET_UP = input("Set up your password (Password must be 8 words or more): ")
            if len(Password_SET_UP) >= Length_Check:
                break
            else:
                print("You have not entered", Length_Check ,"words or more!!")
        #Attempting 3 Password Attempt
        for i in range(3):
            Password = input("Enter New Password: ")
            if Password == Password_SET_UP:
                print(Access_Phrase,  '\n'+ ConnectedLine_Large, "\n" + Welcome, "to the Telepathetic Questionaire!")
                break
            else:
                NumPass -= 1
                if NumPass == 2:
                    print(IncorrectPASS, "You have", NumPass, "left to attempt.")
                elif NumPass == 1:
                    print(IncorrectPASS, "You have", NumPass, "left to attempt.")
                elif NumPass == 0:
                    print("You have no more attempts and will be locked out!!") 

#Intiate login module
Login()