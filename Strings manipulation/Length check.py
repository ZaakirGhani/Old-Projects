#Length

def L():
    Length = (input("ID: "))
    Length.isnumeric()
    Length_Check(Length)

    i = [Length]
    print(i)
    


def Length_Check(L):
    

    if len(L) > 7 and L.isnumeric() == True:
        print("Success")
    else:
        print("Wrong")
        L = input("Reenter:ew")

def Numeric(N):
    
   

    if N.isnumeric() == True:
        print("ISNUMERIC")
    else:
        print("Wrong")

L()