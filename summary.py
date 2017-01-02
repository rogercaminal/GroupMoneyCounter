import os, sys, pot, expense, config, summary

class summary(object):

    def __init__(self, pot, expensemanager, expenseDict, debug):
        self.pot = pot
        self.expensemanager = expensemanager
        self.expenseDict = expenseDict
        self.debug = debug

        self.dictPot      = self.pot.retrieveDict()
        self.dictExpenses = self.expensemanager.retrieveDict()[0]
        self.dictPaid     = self.expensemanager.retrieveDict()[1]
    
        self.peopleParticipating = list(set(self.dictPot.keys() + self.dictExpenses.keys()))
        self.peopleParticipating.sort()

    def printTotals(self):

        print str("PERSONA").ljust(15),
        print str("POT").ljust(15),
        print str("PAGAT").ljust(15),
        print str("CONSUMIT").ljust(15),
        print str("QUANTITAT NETA").ljust(15)
        for person in self.peopleParticipating:
            print str(person).ljust(15),
            print str("%.2f" % (self.dictPot[person])).ljust(15),
            print str("%.2f" % (self.dictPaid[person])).ljust(15),
            print str("%.2f" % (self.dictExpenses[person])).ljust(15),
            print str("%+.2f" % (self.dictPot[person] + self.dictPaid[person] - self.dictExpenses[person])).ljust(15)
    
        if (self.debug):
    #        print "\n\n====================================================\n"
    #        print self.pot
            print "\n\n====================================================\n"
            listOfExpenses = self.expenseDict.keys()
            listOfExpenses.sort()
            for e in listOfExpenses:
                print self.expenseDict[e]
    #        print "\n\n====================================================\n"
    #        print self.expensemanager


    def printCorrespondences(self):
        positive = []
        negative = []
        for person in self.peopleParticipating:
            money = self.dictPot[person] + self.dictPaid[person] - self.dictExpenses[person]
            if money>0:
                positive.append([person, money])
            else:
                negative.append([person, money])
    
        for n in negative:
            for p in positive:
                if p[1]>0.01 and abs(n[1])>0.01:
                    payment = 0
                    if abs(n[1])>=abs(p[1]):
                        payment = p[1]
                        n[1] += p[1]
                        p[1] = 0
                        print "%s pays %s %.2f euros." % (n[0], p[0], payment)
                    elif abs(n[1])<abs(p[1]):
                        payment = abs(n[1])
                        p[1] += n[1]
                        n[1] = 0
                        print "%s pays %s %.2f euros." % (n[0], p[0], payment)
