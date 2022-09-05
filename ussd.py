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
        