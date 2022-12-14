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
            time.sleep(1)
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
            self.e_topUP()
        elif self.user0 == "4":
            print("USSD code running...")
            time.sleep(2)
            self.berekete10X()
        elif self.user0 == "0":
            time.sleep(1)
            sys.exit()
        else:
            time.sleep(1)
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
        
    def data(self):
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
            else:
                print("Invalid")
                self.data()
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
        else:
            print("Invalid")
            self.data()
    
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
        elif self.user4 == "2":
            print("ussd code running...")
            time.sleep(2)
            self.monthlyPlan()
        elif self.user4 == "3":
            print("ussd code running...")
            time.sleep(2)
            self.megaPlan()
        elif self.user4 == "4":
            print("ussd code running...")
            time.sleep(2)
            self.superMegaPlan()
        elif self.user4 == "0":
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
        elif self.user9 == "0":
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
                self.shareData()
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
                self.shareData()
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

    def monthlyPlan(self):
        self.user6 = input("""
            1. N1000 = 3.9GB 30Days incl 2GB nite
            2. N1500 = 7.5GB 30Days incl 4GB nite
            3. N2000 = 9.2GB 30Days incl 4GB
            4. N2500 = 10.8GB 30Days incl 4GB nite
            0. Cancel
        >> """)
        if self.user6 == "1":
            print("ussd code running...")
            time.sleep(2)
            print("CONGRATS!, you have succefully subscribed to N1000 data plan giving 3.9GB (3.9GB+1GB night) valid for 30 day.")
        elif self.user6 == "2":
            print("ussd code running...")
            time.sleep(2)
            print("CONGRATS!, you have succefully subscribed to N1500 data plan giving 7.5GB (7.5GB+4GB night) valid for 30 day.")
        elif self.user6 == "3":
            print("ussd code running...")
            time.sleep(2)
            print("CONGRATS!, you have succefully subscribed to N4000 data plan giving 9.2GB (9.2GB+4GB night) valid for 30 day.")
        elif self.user6 == "4":
            print("ussd code running...")
            time.sleep(2)
            print("CONGRATS!, you have succefully subscribed to N2500 data plan giving 10.8GB (10.8GB+4GB night) valid for 30 day.")
        elif self.user6 == "0":
            print("Thank you for choosing Glo")
            time.sleep(1) 
            sys.exit()
        else:
            print("WRONG INPUT!")
            self.monthlyPlan()

    def megaPlan(self):
        self.user7 = input("""
            1. N10000 = 50GB 30Days incl 4GB nite
            2. N15000 = 7.5GB 30Days incl 7GB nite
            3. N18000 = 119GB 30Days incl 10GB nite
            4. N20000 = 138GB 30Days incl 12GB nite
            0. Cancel
        >> """)
        if self.user7 == "1":
            print("ussd code running...")
            time.sleep(2)
            print("CONGRATULATIONS!, you have succefully subscribed to N10000 data plan giving 50GB (50GB+4GB night) valid for 30 day.")
        elif self.user7 == "2":
            print("ussd code running...")
            time.sleep(2)
            print("CONGRATULATIONS!, you have succefully subscribed to N15000 data plan giving 75GB (75GB+7GB night) valid for 30 day.")
        elif self.user7 == "3":
            print("ussd code running...")
            time.sleep(2) 
            print("CONGRATULATIONS!, you have succefully subscribed to N18000 data plan giving 119GB (119GB+10GB night) valid for 30 day.")
        elif self.user7 == "4":
            print("ussd code running...")
            time.sleep(2)
            print("CONGRATULATIONS!, you have succefully subscribed to N20000 data plan giving 138GB (138GB+12GB night) valid for 30 day.")
        elif self.user7 == "0":
            print("Thank you for choosing Glo")
            time.sleep(1)
            sys.exit()
        else:
            print("WRONG INPUT!")
            self.megaPlan() 
        
    def superMegaPlan(self):
        self.user8 = input("""
            1. N30000 = 225GB 30Days
            2. N36000 = 300GB 30Days
            3. N50000 = 425GB 90Days
            4. N60000 = 525GB 120Days
            0. Cancel
        >> """)
        if (self.user8 == "1") or (self.user8 == "2") or (self.user8 == "3") or (self.user8 == "4"):
            print("ussd code running...")
            time.sleep(2)
            print("SORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow data. To Borrow Data now, just dial *321#")
            sys.exit()
        elif user0 == "0":
            print("Thank you for choosing Glo")
            time.sleep(1)
            sys.exit()
        else:
            print("Invalid Input") 
            self.superMegaPlan()  

    def e_topUP(self):
        self.enter8 = input("""
            Welcome to Glo e-services
                Please select an option

                (1) Airtime
                (2) Data
            >""")
        if self.enter8 == "1":
            print("ussd code running...")
            time.sleep(2)
            self.e_Airtime()
        elif self.enter8 == "2":
            print("ussd code running...")
            time.sleep(2)
            self.e_Data()
        else:
            print("invalid input")
            time.sleep(2)
            self.e_topUP()


    def e_Airtime(self):
        self.enter9 = input("""
            AIRTIME
        (1) 5X recharge
        (2) Regular Recharge
        > """)
        if self.enter9 == "1":
            print("ussd code running...")
            time.sleep(3)
            self.enter00 = input("""
                1. N120,
                2. N220,
                3. N320,
                4. N420,
                0. Cancel

                >> """)
            if (self.enter00 == "1") or (self.enter00 == "2") or (self.enter00 == "3") or (self.enter00 == "4"):
                print("ussd code running...")
                time.sleep(3)
                print("Your request is being processed, we will send you an SMS shortly")
                time.sleep(1)
                sys.exit()
            elif self.enter == "0":
                time.sleep(2)
                print("Thanks for choosing GLO")
                sys.exit()
            else:
                time.sleep(1)
                ("Invalid Input")
                self.e_Airtime()
        elif self.enter9 == "2":
            time.sleep(2)
            self.enter11 = input("""
            1. Self,
            2. Third party
        >> """)
            if self.enter11 == "1":
                time.sleep(2)
                print("Please Enter Amount:")
                self.enter22 = input("-- ")
                if len(self.enter22) >= 2:
                    print("ussd code running...")
                    time.sleep(3)
                    print("Your request is being processed, we will send you an SMS shortly \nThank you for using Glo e-services, the simplest way to recharge and buy data for family, friends and yourself")
                    sys.exit()
                else:
                    print("Invalid input")
                    self.e_Airtime()
            elif self.enter11 == "2":
                time.sleep(2)
                self.enter33 = input("""
                    Please enter phone number: 
                    Glo line only
                    >> """)
                if len(self.enter33) == 11:
                    time.sleep(2)
                    print("Enter Amount")
                    self.enter44 = input("--  ")
                    if len(self.enter44) >= 2:
                        print("ussd code running...")
                        time.sleep(3)
                        print("Your request is being processed, we will send you an SMS shortly  \nThank you for using Glo e-services, thesimplest way to recharge and buy data for family, friends and yourself")
                        sys.exit()
                    else:
                        time.sleep(1)
                        print("Invalid amount")
                        self.e_Airtime()
                else:
                    time.sleep(1)
                    print("Invalid input")
                    self.e_Airtime()
            else:
                time.sleep(1)
                print("Invalid input")
                self.e_Airtime()
        else:
            time.sleep(1)
            print("Invalid input")
            self.e_Airtime()


    def e_Data(self):
        self.userInput = input("""
           DATA PLAN PURCHASE
            1. Self,
            2. Third party
            00. cancel
        > """)
        if self.userInput == "1":
            self.userInput0 = input("""
            1. N100 = 105MB 1Day incl 15MB nite,
            2. N200 = 350MB 2Day incl 110MB nite,
            3. N500 = 1.05GB 14Day incl 25M0B nite,
            4. N1000 = 2.5GB
            0. Cancel
            > """)
            if (self.userInput0 == "1") or (self.userInput0 == "2") or (self.userInput0 == "3") or (self.userInput0 == "4"):
                print("ussd code running...")
                time.sleep(2)
                print("Your request is being processed, we will send you an SMS shortly  \nThank you for using Glo e-services")
                sys.exit()
            elif  self.userInput0 == "0":
                print("Thank you for using Glo e-services")
                time.sleep(1)
                sys.exit()
        elif self.userInput == "2":
            print("ussd code runnig...")
            time.sleep(3)
            print("Please enter phone number: \nGlo line only Please")
            self.userInput1 = input("--  ")
            if len(self.userInput1) == 11:
                print("Enter Amount")
                self.userInput2 = input("--  ")
                if len(self.userInput2) >= 2:
                    print("ussd code running...")
                    time.sleep(3)
                    print("Your request is being processed, we will send you an SMS shortly  \nThank you for using Glo e-services, the simplest way to recharge and buy data for family, friends and yourself")
                else:
                    print("ussd code running...")
                    time.sleep(2)
                    print("Invalid input")
                    self.e_Data()
            else:
                print("ussd code running...")
                time.sleep(2)
                print("WRONG INPUT")
                self.e_Data()
        elif self.userInput == "00":
            print("Thank you for using Glo e-services, the simplest way to recharge and buy data for family, friends and yourself")
            sys.exit()
        else:
            print("WRONG INPUT")
            self.e_Data()

    def berekete10X(self):
        self.userInput6 = input("""
            1. Migrate Now
            2. Back
            0. Cancel
        > """)
        if self.userInput6 == "1":
            print("ussd code running...")
            time.sleep(2)
            print("Dear Customer, you have been migrated from GLO_BEREKETE to BEREKETE_10X")
            sys.exit()
        elif self.userInput6 == "2":
            time.sleep(1)
            self.mainMenu()
        elif self.userInput6 == "0":
            time.sleep(1)
            print("Thank you for using Glo")
            sys.exit()
      

glo = USSD()