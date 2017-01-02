import os, sys, pot, expense, config

debug = True

#________________________________________________________________________________________________
def printSummary(pot, expensemanager, expenseDict):

    dictPot      = pot.retrieveDict()
    dictExpenses = expensemanager.retrieveDict()[0]
    dictPaid     = expensemanager.retrieveDict()[1]

    peopleParticipating = list(set(dictPot.keys() + dictExpenses.keys()))
    peopleParticipating.sort()
    print str("PERSONA").ljust(15),
    print str("POT").ljust(15),
    print str("PAGAT").ljust(15),
    print str("CONSUMIT").ljust(15),
    print str("QUANTITAT NETA").ljust(15)
    for person in peopleParticipating:
        print str(person).ljust(15),
        print str("%.2f" % (dictPot[person])).ljust(15),
        print str("%.2f" % (dictPaid[person])).ljust(15),
        print str("%.2f" % (dictExpenses[person])).ljust(15),
        print str("%+.2f" % (dictPot[person] + dictPaid[person] - dictExpenses[person])).ljust(15)

    if (debug):
#        print "\n\n====================================================\n"
#        print pot
        print "\n\n====================================================\n"
        listOfExpenses = expenseDict.keys()
        listOfExpenses.sort()
        for e in listOfExpenses:
            print expenseDict[e]
#        print "\n\n====================================================\n"
#        print expensemanager
