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
    print str("PAGAT").ljust(20),
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
    listMenjar.append('Ceci')
    listMenjar.append('RogerC')
    listMenjar.append('Laura')
    listMenjar.append('Manrique')
    listMenjar.append('Meri')
    listMenjar.append('Montse')
    listMenjar.append('NataliaG')
    listMenjar.append('NataliaL')
    listMenjar.append('Oscar')
    listMenjar.append('XaviB')
    listMenjar.append('Raquel')
    listMenjar.append('RogerE')
    listMenjar.append('Melero')
    listMenjar.append('JEnric')
#    listMenjar.append('Marta')

    listBeure = []
    listBeure.append('Adria')
    listBeure.append('Albert')
    listBeure.append('Carles')
    listBeure.append('Ceci')
    listBeure.append('RogerC')
    listBeure.append('Laura')
    listBeure.append('Manrique')
    listBeure.append('Meri')
    listBeure.append('Montse')
    listBeure.append('NataliaG')
    listBeure.append('NataliaL')
    listBeure.append('Oscar')
    listBeure.append('XaviB')
    listBeure.append('RogerE')
    listBeure.append('Melero')
    listBeure.append('JEnric')
#    listBeure.append('Marta')
    listBeure.append('Miquel')
    listBeure.append('Monica')
    listBeure.append('Anna')
    listBeure.append('Alex')

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
    expenseDict["Raim"].addPayerAndAmount(payerName='Laura', amount=4.88)
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
    expenseDict["Gintonic"].addPayerAndAmount(payerName='Miquel', amount=52.95)
    for person in listBeure:
        expenseDict["Gintonic"].addBeneficiary(beneficiaryName=person)
    expenseDict["Gintonic"].computePricePerParticipant()

    # Pica-pica
    expenseDict["PicaPica"] = expense.expense()
    expenseDict["PicaPica"].setExpenseName("PicaPica")
    expenseDict["PicaPica"].addPayerAndAmount(payerName='RogerC', amount=26.29)
    for person in listMenjar:
        expenseDict["PicaPica"].addBeneficiary(beneficiaryName=person)
    expenseDict["PicaPica"].computePricePerParticipant()

    # Amanida
    expenseDict["Amanida"] = expense.expense()
    expenseDict["Amanida"].setExpenseName("Amanida")
    expenseDict["Amanida"].addPayerAndAmount(payerName='Montse', amount=22.00)
    for person in listMenjar:
        expenseDict["Amanida"].addBeneficiary(beneficiaryName=person)
    expenseDict["Amanida"].computePricePerParticipant()

    # Hummus
    expenseDict["Hummus"] = expense.expense()
    expenseDict["Hummus"].setExpenseName("Hummus")
    expenseDict["Hummus"].addPayerAndAmount(payerName='Raquel', amount=7.5)
    for person in listMenjar:
        expenseDict["Hummus"].addBeneficiary(beneficiaryName=person)
    expenseDict["Hummus"].computePricePerParticipant()

    # Vi negre
    expenseDict["ViNegre"] = expense.expense()
    expenseDict["ViNegre"].setExpenseName("ViNegre")
    expenseDict["ViNegre"].addPayerAndAmount(payerName='RogerE', amount=19.00)
    for person in listMenjar:
        expenseDict["ViNegre"].addBeneficiary(beneficiaryName=person)
    expenseDict["ViNegre"].computePricePerParticipant()

    # Torrons
    expenseDict["Torrons"] = expense.expense()
    expenseDict["Torrons"].setExpenseName("Torrons")
    expenseDict["Torrons"].addPayerAndAmount(payerName='Carles', amount=7.52)
    for person in listMenjar:
        expenseDict["Torrons"].addBeneficiary(beneficiaryName=person)
    expenseDict["Torrons"].computePricePerParticipant()

    # Cervesa
    expenseDict["Cervesa"] = expense.expense()
    expenseDict["Cervesa"].setExpenseName("Cervesa")
    expenseDict["Cervesa"].addPayerAndAmount(payerName='NataliaL', amount=24.00)
    for person in listAll:
        expenseDict["Cervesa"].addBeneficiary(beneficiaryName=person)
    expenseDict["Cervesa"].computePricePerParticipant()

    # Vi blanc
    expenseDict["ViBlanc"] = expense.expense()
    expenseDict["ViBlanc"].setExpenseName("ViBlanc")
    expenseDict["ViBlanc"].addPayerAndAmount(payerName='Albert', amount=20.00)
    for person in listMenjar:
        expenseDict["ViBlanc"].addBeneficiary(beneficiaryName=person)
    expenseDict["ViBlanc"].computePricePerParticipant()

    # Create expense manager
    expensemanager = expense.expenseManager(expensesDict=expenseDict)
    expensemanager.compute()

    # Compute and print Totals
    printSummary(pot=Pot, expensemanager=expensemanager)

