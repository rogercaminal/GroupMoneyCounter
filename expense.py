import os

class expense(object):
    def __init__(self):
        self.name = ""            # Name of the expense

        self.payerList = []       # Names of the people that paied
        self.splittedPaid = []    # In case several people pay, the total amount that each one paied.
        self.totalPaid = 0.       # Total amount paid.

        self.beneficiaryList = [] # Names of the people that receives the benefit

        self.dividedExpense = []  # Total value of the expense divided by the total number of participants

        self.totalParticipants = 0
        self.pricePerParticipant = 0.


    def __str__(self):
        strToReturn = ""
        strToReturn += "Nom: %s\n" % (self.name)
        strToReturn += "Valor total: %.2f\n" % (self.totalPaid)
        strToReturn += "# participants: %d\n" % (self.totalParticipants)
        strToReturn += "Quantitat a pagar per participant: %.2f\n" % (self.pricePerParticipant)
        strToReturn += "Llista de pagadors:\n"
        for i in range(len(self.payerList)):
            strToReturn += "%s - %.2f\n" % (self.payerList[i], self.splittedPaid[i])
        strToReturn += "Llista de beneficiaris (+ el pagador):\n"
        for i in range(len(self.beneficiaryList)):
            strToReturn += "%s\n" % (self.beneficiaryList[i])
        strToReturn += "\n"
        return strToReturn

    def setExpenseName(self, name):
        self.name = name

    def addPayerAndAmount(self, payerName, amount):
        self.payerList.append(payerName)
        self.splittedPaid.append(amount)
        self.totalPaid += amount
        self.totalParticipants += 1

    def addBeneficiary(self, beneficiaryName):
        self.beneficiaryList.append(beneficiaryName)
        self.totalParticipants += 1

    def computePricePerParticipant(self):
        self.pricePerParticipant = self.totalPaid/self.totalParticipants




class expenseManager(object):
    def __init__(self, expensesDict):
        self.expensesDict = expensesDict # Dictionary with all the expenses
        self.personTotalSpent = {}
        self.personTotalPaid = {}


    def __str__(self):
        strToReturn = ""
        strToReturn += "R E S U M   G A S T O S\n"
        for person in self.personTotalSpent.keys():
            strToReturn += "%s\t-\t%.2f\n" % (person, self.personTotalSpent[person])
        strToReturn += "\n"
        return strToReturn

    def compute(self):
        for exp in self.expensesDict.keys():
            for i in range(len(self.expensesDict[exp].payerList)):
                if self.expensesDict[exp].payerList[i] not in self.personTotalSpent.keys():
                    self.personTotalSpent[self.expensesDict[exp].payerList[i]] = self.expensesDict[exp].pricePerParticipant
                else:
                    self.personTotalSpent[self.expensesDict[exp].payerList[i]] += self.expensesDict[exp].pricePerParticipant

                if self.expensesDict[exp].payerList[i] not in self.personTotalPaid.keys():
                    self.personTotalPaid[self.expensesDict[exp].payerList[i]] = self.expensesDict[exp].splittedPaid[i]
                else:
                    self.personTotalPaid[self.expensesDict[exp].payerList[i]] += self.expensesDict[exp].splittedPaid[i]

            for i in range(len(self.expensesDict[exp].beneficiaryList)):
                if self.expensesDict[exp].beneficiaryList[i] not in self.personTotalSpent.keys():
                    self.personTotalSpent[self.expensesDict[exp].beneficiaryList[i]] = self.expensesDict[exp].pricePerParticipant
                else:
                    self.personTotalSpent[self.expensesDict[exp].beneficiaryList[i]] += self.expensesDict[exp].pricePerParticipant

                if self.expensesDict[exp].beneficiaryList[i] not in self.personTotalPaid.keys():
                    self.personTotalPaid[self.expensesDict[exp].beneficiaryList[i]] = 0.
                else:
                    self.personTotalPaid[self.expensesDict[exp].beneficiaryList[i]] += 0.

    def retrieveDict(self):
        return [self.personTotalSpent, self.personTotalPaid]
