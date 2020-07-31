import Rental
import Movie

class Customer:
    def __init__(self, name):
        self.Name = name
        self.Rentals = []

    def addRental(self, arg):
        self.Rentals.append(arg)

    def getName(self):
        return self.Name

    def statement(self):
        totalAmount = 0
        frequentRenterPoints = 0
        result = "Rental Record for " + self.getName() + "\n"
        for each in self.Rentals:
            thisAmount = 0

            # determine amounts for each line
            if each.Movie.PriceCode == Movie.REGULAR:
                thisAmount += 2
                if (each.DaysRented > 2): 
                    thisAmount += (each.DaysRented - 2) * 1.5
            elif each.Movie.PriceCode == Movie.NEW_RELEASE:
                thisAmount += each.DaysRented * 3
            elif each.Movie.PriceCode == Movie.CHILDRENS:
                thisAmount += 1.5
                if (each.DaysRented > 3): 
                    thisAmount += (each.DaysRented - 3) * 1.5

            # add frequent renter points
            frequentRenterPoints += 1

            # add bonus for a two day new release rental
            if ((each.Movie.PriceCode == Movie.NEW_RELEASE) and each.DaysRented > 1):
                frequentRenterPoints += 1

            # show figures for this rental
            result += "\t" + each.Movie.Title + "\t" + thisAmount.ToString() + "\n"
            totalAmount += thisAmount
        
        # add footer lines
        result += "Amount owed is " + str(totalAmount) + "\n"
        result += "You earned " + str(frequentRenterPoints) + " frequent renter points"
        return result
