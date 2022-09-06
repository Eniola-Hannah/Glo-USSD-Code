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
        
    def data():
        self.user3 = input("""
            1. Buy Data Plan
            2. Gift Data Plan
            3. Share Data Plan
            4. Check Data Balance
            0. Exit
        >> """)
        if self.user3 == "1":
            print("ussd code running...")
            time.sleep(2)
             self.input =  input("""
                1. Proceed(Auto-Renew)
                2. Proceed(One-Off)
            > """)
            if (self.input == "1") or (self.input == "2"):
                time.sleep(1)
                self.buyData()
            self.buyData()
        elif self.user3 == "2":
            print("ussd code running...")
            time.sleep(2)
            self.giftData()
        elif self.user3 == "3":
            print("ussd code running...")
            time.sleep(2)
            self.shareData()
        elif self.user3 == "4":
            print("ussd code running...")
            time.sleep(2)
            print("Dear Customer, your plan has expired and you do not have a data plan. To buy a data plan and continue browsing visit http://hsi.glo.com or dial *777#.")
            sys.exit()
        elif self.user3 == "0":
            print("Thank you for choosing Glo")
            sys.exit()
    
    def buyData(self):
        self.user4 = input("""
            1. Mini plans
            2. Monthly Plans
            3. Mega Plans
            4. Super Mega Plans
            0. Exit
        >> """)
        if self.user4 == "1":
            print("ussd code running...")
            time.sleep(2)
            self.miniPlan()
        elif self.user9 == "2":
            print("ussd code running...")
            time.sleep(2)
            self.monthlyPlan()
        elif self.user9 == "3":
            print("ussd code running...")
            time.sleep(2)
            self.megaPlan()
        elif self.user9 == "4":
            print("ussd code running...")
            time.sleep(2)
            self.superMegaPlan()
        elif self.user9 == "0"
            print("Thank you for choosing Glo")
            time.sleep(2)
            sys.exit()
        else:
            print("Invalid Input")
            self.buyData()

    def giftData(self):
        self.user9 = input("""
        Select a Gift to plan;
            1. Mini plans
            2. Monthly Plans
            3. Mega Plans
            4. Super Mega Plans
            0. Exit
        > """)
        if self.user9 == "1":
            print("ussd code running...")
            time.sleep(2)
            self.miniPlan()
        elif self.user9 == "2":
            print("ussd code running...")
            time.sleep(2)
            self.monthlyPlan()
        elif self.user9 == "3":
            print("ussd code running...")
            time.sleep(2)
            self.megaPlan()
        elif self.user9 == "4":
            print("ussd code running...")
            time.sleep(2)
            self.superMegaPlan()
        elif self.user9 == "0"
            print("Thank you for choosing Glo")
            time.sleep(2)
            sys.exit()
        else:
            print("Invalid Input")
            self.giftData()
        
    def shareData(self):
        self.userInput3 = input("""
            1. Share,
            2. Unshare,
        > """)
        if self.userInput3 == "1":
            print("Please enter subscriber\'s number:")
            self.userInput4 = input("-->  ")
            if len(self.userInput4) == 11:
                print("Your request for Data sharing has been sent")
            elif len(self.userInput4) < 11:
                print("You have input an incomplete number")
            elif len(self.userInput4) > 11:
                print("You have input more than 11 digit number")
            else:
                print("Invalid Input")
        elif self.userInput3 == "2":
            print("Please enter subscriber\'s number:")
            self.userInput5 = input("-->  ")
            if len(self.userInput5) == 11:
                print("Your request to unshare Data has been sent")
            elif len(self.userInput5) < 11:
                print("You have input an incomplete number")
            elif len(self.userInput5) > 11:
                print("You have input more than 11 digit number")
            else:
                print("Invalid Input") 
        else:
            print("WRONG INPUT")
            self.shareData()

    def miniPlan(self):
        self.user5 = input("""
            1. N100=150MB 1 Day incl 35MB nite
            2. N200=350mb 2 Days incl 110MB nite
            3. N500=1.8GB 14 Days incl 1gb nite
            4. N50=50MB 1 Day incl 5MB nite
            0. Cancel
        >> """)
        if self.user5 == "1":
            print("ussd code running...")
            time.sleep(2)
            print("CONGRATS!, you have succefully subscribed to N100 data plan giving 150MB (115MB+35MB night) valid for 1 day.")
        elif self.user5 == "2":
            print("ussd code running...")
            time.sleep(2)
            print("CONGRATS!, you have succefully subscribed to N200 data plan giving 350MB (350MB+110MB night) valid for 2 day.")
        elif self.user5 == "3":
            print("ussd code running...")
            time.sleep(2)
            print("CONGRATS!, you have succefully subscribed to N500 data plan giving 1.8GB (1.8GB+1GB night) valid for 14 day.")
        elif self.user5 == "4":
            print("ussd code running...")
            time.sleep(2)
            print("CONGRATS!, you have succefully subscribed to N50 data plan giving 50MB (50MB+5MB night) valid for 1 day.")
        elif self.user5 == "0":
            print("Thank you for choosing Glo")
            time.sleep(1)
            sys.exit()
        else:
            print("WRONG INPUT!")
            self.miniPlan()



glo = USSD()