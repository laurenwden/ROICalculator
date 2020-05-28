class ROI():
    def __init_(self, rent, expenses, investment, mortgage, management, maintenance,downPayment,closingCosts,improvements):
        self.rent = rent
        self.expenses = expenses
        self.investment = investment
        self.mortgage = mortgage
        self.management = management
        self.maintenance = maintenance
        self.downPayment = downPayment
        self.closingCosts = closingCosts
        self.improvements = improvements

    # method to receive user input for potential rental income
    def income(self):
        while True:
            self.rent = input("\nWhat is the expected monthly rent for this property in dollars?")
            if self.rent.lower() == 'quit':
                break
            if not self.rent.isdigit():
                print("Please enter a valid dollar amount.")
                continue
            else:
                return int(self.rent)
                
            
# methods to record and calculate recurring monthly expenses from the user's input 

    #mortage payment
    def monthlyMortgage(self):
        while True:
            self.mortgage = input("\nWhat is the expected monthly mortgage payment? Enter '0' if expected is 0.")
            if self.mortgage.lower() == 'quit':
                break
            elif not self.mortgage.isdigit():
                print("Please enter a valid dollar amount.")
                continue
            else:
                return int(self.mortgage)

    #property management fees
    def monthlyManagement(self):
        while True:
            self.management = input("\nWhat percentage of the monthly rent will be paid to a property management company (as a number)? Enter '0' if expected is 0.")
            if self.management.lower() == 'quit':
                break
            elif not self.management.isdigit():
                print("Please enter a valid dollar amount.")
                continue
            else:
                return int(self.rent) * int(self.management) / 100

    #monthly maintenance fees    
    def monthlyMaintenance(self):
        while True: 
            self.maintenance = input("\nWhat are the expected average monthly maintenance fees? Enter '0' if expected is 0.")
            if self.maintenance.lower() == 'quit':
                break
            elif not self.maintenance.isdigit():
                print("Please enter a valid dollar amount.")
                continue
            else:
                return int(self.maintenance)

# methods to record money invested through purchase and improvements

    #money to be used for downpayment
    def moneyDown(self):
        while True:
            self.downPayment = input(
                "\nHow much money will need to be spent on a down payment?")
            if self.downPayment.lower() == 'quit':
                break
            elif not self.downPayment.isdigit():
                print("Please enter a valid dollar amount.")
                continue
            else:
                return int(self.downPayment)

    #closing costs
    def closing(self):
        while True:
            self.closingCosts = input(
                "\nHow much money will need to be spent on closing costs?")
            if self.closingCosts.lower() == 'quit':
                break
            elif not self.closingCosts.isdigit():
                print("Please enter a valid dollar amount.")
                continue
            else:
                return int(self.closingCosts)

    #money to be spent for improvements to the property
    def renovations(self):
        while True:
            self.improvements=input(
                "\nHow much money will need to be spent on improvements?")
            if self.improvements.lower() == 'quit':
                break
            elif not self.improvements.isdigit():
                print("Please enter a valid dollar amount.")
                continue
            else:
                return int(self.improvements)

    #calculates potential return on investment into a percentage and prints to the user
    def potentialROI(self):
        self.expenses = int(self.mortgage) + int(self.management) + int(self.maintenance)
        self.investment = int(self.downPayment) + int(self.closingCosts) + int(self.improvements)
        print(
            f"Your ROI is {round((int(self.rent) - self.expenses)*12 / self.investment * 100,2)}%.")


#method to instantiate class depending on user input
def calculateReturn():
    potentialReturn = ROI()

    while True:
        response = input(
            "\n*Ready to find out if your property is a worthwhile investment? Type 'yes' to continue or 'quit' at anytime to quit.")
        if response.lower() == 'yes':
            potentialReturn.income()
            potentialReturn.monthlyMortgage()
            potentialReturn.monthlyManagement()
            potentialReturn.monthlyMaintenance()
            potentialReturn.moneyDown()
            potentialReturn.closing()
            potentialReturn.renovations()
            potentialReturn.potentialROI()
            break
        elif response.lower() == 'quit':
            break


calculateReturn()
