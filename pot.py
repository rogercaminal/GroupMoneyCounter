import os

class pot(object):
    def __init__(self):
        self.participantList = []
        self.amountList = []
        self.totalAmount = 0.

    def __str__(self):
        strToReturn = ""
        strToReturn += "Pot total: %f\n" % (self.totalAmount)
        for i in range(len(self.participantList)):
            strToReturn += "\t%s - \t%.2f\n" % (self.participantList[i], self.amountList[i])
        strToReturn += "\n"
        return strToReturn

    def addContribution(self, person, amount=0.):
        self.participantList.append(person)
        self.amountList.append(amount)
        self.totalAmount += amount

    def retrieveDict(self):
        dictToRetrieve = {}
        for i in range(len(self.participantList)):
            dictToRetrieve[self.participantList[i]] = self.amountList[i] 
        return dictToRetrieve
