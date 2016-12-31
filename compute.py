import os, pot, expense

debug = True

#________________________________________________________________________________________________
def printSummary(pot, expensemanager):

    dictPot      = pot.retrieveDict()
    dictExpenses = expensemanager.retrieveDict()[0]
    dictPaid     = expensemanager.retrieveDict()[1]

    peopleParticipating = set(dictPot.keys() + dictExpenses.keys())
    print str("PERSONA").ljust(20),
    print str("POT").ljust(20),
    print str("PAGAT EXTRA").ljust(20),
    print str("CONSUMIT").ljust(20),
    print str("QUANTITAT NETA").ljust(20)
    for person in peopleParticipating:
        print str(person).ljust(20),
        print str("%.2f" % (dictPot[person])).ljust(20),
        print str("%.2f" % (dictPaid[person])).ljust(20),
        print str("%.2f" % (dictExpenses[person])).ljust(20),
        print str("%+.2f" % (dictPot[person] + dictPaid[person] - dictExpenses[person])).ljust(20)

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
if __name__=="__main__":

    listMenjar = []
    listMenjar.append('Adria')
    listMenjar.append('Albert')
    listMenjar.append('Carles')
    listMenjar.append('CeciRoger')
    listMenjar.append('LauraXavi')
    listMenjar.append('Meri')
    listMenjar.append('Montse')
    listMenjar.append('NataliaG')
    listMenjar.append('NataliaL')
    listMenjar.append('Raquel')
    listMenjar.append('RogerE')
    listMenjar.append('Melero')
    listMenjar.append('JEnric')
    listMenjar.append('Marta')

    listBeure = []
    listBeure.append('Adria')
    listBeure.append('Albert')
    listBeure.append('Carles')
    listBeure.append('CeciRoger')
    listBeure.append('LauraXavi')
    listBeure.append('Meri')
    listBeure.append('Montse')
    listBeure.append('NataliaG')
    listBeure.append('NataliaL')
    listBeure.append('RogerE')
    listBeure.append('Melero')
    listBeure.append('JEnric')
    listBeure.append('Marta')
    listBeure.append('MonicaMiquel')
    listBeure.append('AnnaAlex')

    listAll = list(set(listMenjar + listBeure))

    listMenjar.sort()
    listBeure.sort()
    listAll.sort()

    # Adding pot
    Pot = pot.pot()

    # Adding everyone (loop since initial amount is 0 for everyone)
    for person in listAll:
        Pot.addContribution(person=person,    amount=0.)

    # Adding expenses
    expenseDict = {}

    # Raim
    expenseDict["Raim"] = expense.expense()
    expenseDict["Raim"].setExpenseName("Raim")
    expenseDict["Raim"].addPayerAndAmount(payerName='LauraXavi', amount=4.88)
    for person in listMenjar:
        expenseDict["Raim"].addBeneficiary(beneficiaryName=person)
    expenseDict["Raim"].computePricePerParticipant()

    # Pollastre curry
    expenseDict["Pollastre"] = expense.expense()
    expenseDict["Pollastre"].setExpenseName("Pollastre")
    expenseDict["Pollastre"].addPayerAndAmount(payerName='Melero', amount=15.85)
    for person in listMenjar:
        expenseDict["Pollastre"].addBeneficiary(beneficiaryName=person)
    expenseDict["Pollastre"].computePricePerParticipant()

    # Ron cola
    expenseDict["RonCola"] = expense.expense()
    expenseDict["RonCola"].setExpenseName("RonCola")
    expenseDict["RonCola"].addPayerAndAmount(payerName='JEnric', amount=39.42)
    for person in listBeure:
        expenseDict["RonCola"].addBeneficiary(beneficiaryName=person)
    expenseDict["RonCola"].computePricePerParticipant()

    # Nachos Guacamole
    expenseDict["Guacamole"] = expense.expense()
    expenseDict["Guacamole"].setExpenseName("Guacamole")
    expenseDict["Guacamole"].addPayerAndAmount(payerName='NataliaG', amount=12.97)
    for person in listMenjar:
        expenseDict["Guacamole"].addBeneficiary(beneficiaryName=person)
    expenseDict["Guacamole"].computePricePerParticipant()

    # Cotillon
    expenseDict["Cotillon"] = expense.expense()
    expenseDict["Cotillon"].setExpenseName("Cotillon")
    expenseDict["Cotillon"].addPayerAndAmount(payerName='Meri', amount=24.10)
    for person in listAll:
        expenseDict["Cotillon"].addBeneficiary(beneficiaryName=person)
    expenseDict["Cotillon"].computePricePerParticipant()

    # Gintonic
    expenseDict["Gintonic"] = expense.expense()
    expenseDict["Gintonic"].setExpenseName("Gintonic")
    expenseDict["Gintonic"].addPayerAndAmount(payerName='MonicaMiquel', amount=52.95)
    for person in listBeure:
        expenseDict["Gintonic"].addBeneficiary(beneficiaryName=person)
    expenseDict["Gintonic"].computePricePerParticipant()

    # Pica-pica
    expenseDict["PicaPica"] = expense.expense()
    expenseDict["PicaPica"].setExpenseName("PicaPica")
    expenseDict["PicaPica"].addPayerAndAmount(payerName='CeciRoger', amount=26.29)
    for person in listMenjar:
        expenseDict["PicaPica"].addBeneficiary(beneficiaryName=person)
    expenseDict["PicaPica"].computePricePerParticipant()

    # Create expense manager
    expensemanager = expense.expenseManager(expensesDict=expenseDict)
    expensemanager.compute()

    # Compute and print Totals
    printSummary(pot=Pot, expensemanager=expensemanager)

