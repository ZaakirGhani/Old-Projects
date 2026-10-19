#Common Phrases Bank(CPB)
Access_Phrase = "Access Granted!!"
Try_Again_Phrase = "Try Again!!"
Welcome = "Welcome"
Hello = "Hello,"
No_Punctuation_Spaces = "We do not accept punctuations and spaces (Only numbers and letters)."
Enter_USERNAME_Again = "Please enter username again!!"
IncorrectPASS = "Incorrect Password!!"

#Do nothing
Do_Nothing = print("")

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

#Introduction Module(IM)
def Introduction():
    print( HashtagLine_Small, "Telepathetic Questionaire", HashtagLine_Small)
    print("The greatest Questionaire never solved(Wink Wink)!")
    print(ConnectedLine_Large)


#3 Attempt password(The Login Module(TLM))
def Login():
#Name
        #Tool Property(TP): Loop, Asking(input) - Selection - Setting Boundaries (Only words)  
        #Tool Keywords(TK): WHILE, INPUT, IF, ISALPHA()
        while True:
            Name = input("Enter your first name: ")
            if Name.isalpha() == False:
                print("Please enter a valid name.")
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
                Telepathetic_Questionaire()
                break
            else:
                NumPass -= 1
                if NumPass == 2:
                    print(IncorrectPASS, "You have", NumPass, "left to attempt.")
                elif NumPass == 1:
                    print(IncorrectPASS, "You have", NumPass, "left to attempt.")
                elif NumPass == 0:
                    print("You have no more attempts and will be locked out!!") 
                
                

#This is where the questionare begins and intiated into the login.
def Telepathetic_Questionaire():
    print(f"Answer five questions to win a prize {Smile} (HEH HEH HEH!!)") 
    
    #Create the quiz
    The_five_Questions = (
        ("1. Define GDP"),
        ("2. What is the capital of Italy?"),
        ("3. Which civilisation invented pie?"),
        ("4. Who was the father of economics?"),
        ("5. What are the seven layers of the OSI model (To be fair its about networking)")
    )
    #Creating the options or selections
    Five_Questions_Option = (
        ("  A. Gross Domestic product", "  B. General Domestic promotion", "  C. Government Domestic Production", "  D. General Domain Prompt"),
        ("  A. Verona", "  B. Parma", "  C. Cagliari", "  D. Rome"),
        ("  A. Ancient Rome", "  B. Native Americans", "  C. Ancient Egyptian", "  D. Ancient Sumerians"),
        ("  A. Arthur Schopenhauer", "  B. Aristotle", "  C. Adam Smith", "  D. Immanuel Kant"),
        ("  A. Apple, Proton, Size, Transport, Network, Data Link, Physics", "  B. Application, Presentation, Session, Transport, Network, Data Link, Physical", 
        "  C. App, Personal Area Network, System, Transport, Network, Big Data, Phishing", "  D. App, Promotion, Session, Transformation, Netline, Big Data, Power")
    )
    #YOU BETTER NOT BE CHEATING!! If you are, look behind you. . . !!!!):
    Answer_Five_Questions = ("a", "d", "c","c","b")
    #Question Increment
    Q_Num = 0
    #Score Increment
    Q_Score = 0
    #Storing users answers
    Guesses = []
    #printing out the questions and options and selecting if the answers are correct. 
    for FQ in The_five_Questions:
        print(FQ)
        for FOQ in Five_Questions_Option[Q_Num]:
            print(FOQ)
        Guessing = input("Answer the Question(Answer must be lowercased): ")
        Guesses.append(Guessing)
        if Guessing == Answer_Five_Questions[Q_Num]:
            Do_Nothing
            Q_Score+=1
        else:
            Do_Nothing
        Q_Num+= 1 

    #Display score
    print(f"\n{DoubleLine_Break_Large}\nYour Score is: {Q_Score}/{len(The_five_Questions)}!\n")
    #Credits
    try:
        if Q_Score == 5:
            print (f"And the Prize is: . . . You get nothing!!!!!!! HEH HEH")
            print("Stay tuned for more fun Questions")
            Space = input("")
        else:
            print("You have failed to get them all right:( !!!!!!!")
            print("\nStay tuned for more fun Questions")
            Space = input("")
    except ValueError as err:
        print(err)

#Intiation stage!
#Intiate Intro Module(IM)
Introduction()
#Intiate Password Module(TLM)
Login()

