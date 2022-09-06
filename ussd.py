import sys
import time

class USSD:
    def __init__(self):
        self.network = "GLO... THE FAST NETWORK"
        self.pin = "*777#"
        self.login()

    def login(self):
        print(self.network)
        self.user = input("- Enter your USSD code - ")
        if self.user == self.pin:
            print("USSD code running...")
            time.sleep(2)
            self.mainMenu()
        else:
            print("USSD code running...")
            time.sleep(2)
            print("Sorry, the format of the string entered is not correct")
            self.login()

    def mainMenu(self):
        self.user0 = input("""
        1. Register NIN
        2. Data
        3. E-top up
        4. Berekete 10X
        0. Exit

    >>  """)
        if self.user0 == "1":
            print("USSD code running...")
            time.sleep(2)
            self.registerNin()
        elif self.user0 == "2":
            print("USSD code running...")
            time.sleep(2)
            self.data()
        elif self.user0 == "3":
            print("USSD code running...")
            time.sleep(2)
            self.e-topUP()
        elif self.user0 == "4":
            print("USSD code running...")
            time.sleep(2)
            self.berekete10X()
        elif self.user0 == "0":
            time.sleep(1)
            sys.exit()
        else:
            print("USSD code running...")
            time.sleep(2)
            print("Invalid input")
            self.mainMenu()

            
    def registerNin(self):
        self.user1 = input("""
        1. Enter NIN
        2. Check NIN status
        3. Main Menu
        0. Cancel
    >> """)   
        if self.user1 == "1":
            time.sleep(1)
            self.user2 = input("Enter your 11 digit NIN...\n And make sure it is not less or greater than 11 digit \n>> ")   
            if len(self.user2) == 11:
                print("USSD code running...")
                time.sleep(2)
                print("you have successfully submitted your NIN, we will send you an SMS shortly after your NIN has been verified") 
                time.sleep(1)
            elif len(self.user2) < 11:
                time.sleep(2)
                print("Dear Subscriber, you have input an incomplete NIN")
                self.registerNin()
            elif len(self.user2) > 11:
                time.sleep(2)
                print("Dear Subscriber, you have input more than the 11 digit NIN number")
                self.registerNin()
            else:
                time.sleep(1)
                print("Invalid Input") 
                self.registerNin()
        elif self.user1 == "2":
            print("USSD code running...")
            time.sleep(2)
            print("Dear Subscriber you are yet to submit your NIN")
        elif self.user1 == "3":
            print("USSD code running...")
            time.sleep(1)
            self.mainMenu()
        elif self.user1 == "0":
            print("Thanks for choosing GLO")
            time.sleep(1)
            sys.exit()
        else:
            print("WRONG INPUT!")
            self.registerNin()
            
glo = USSD()