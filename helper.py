import os, sys, pot, expense, config

#________________________________________________________________________________________________
def printSummary(pot, expensemanager, expenseDict, debug):

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

#________________________________________________________________________________________________
def printCorrespondences(pot, expensemanager, debug):

    dictPot      = pot.retrieveDict()
    dictExpenses = expensemanager.retrieveDict()[0]
    dictPaid     = expensemanager.retrieveDict()[1]

    peopleParticipating = list(set(dictPot.keys() + dictExpenses.keys()))
    peopleParticipating.sort()

    positive = []
    negative = []
    for person in peopleParticipating:
        money = dictPot[person] + dictPaid[person] - dictExpenses[person]
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
