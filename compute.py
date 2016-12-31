import os, pot, expense

debug = True

#________________________________________________________________________________________________
def printSummary(dictPot, dictExpenses, dictPaid):

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
        print "\n\n====================================================\n"
        print travelPot
        print "\n\n====================================================\n"
        listOfExpenses = expenseDict.keys()
        listOfExpenses.sort()
        for e in listOfExpenses:
            print expenseDict[e]
        print "\n\n====================================================\n"
        print expensemanager


#________________________________________________________________________________________________
if __name__=="__main__":

    # Adding pot
    travelPot = pot.pot()
    travelPot.addContribution(person='Miquel',    amount=200.)
    travelPot.addContribution(person='Montse',    amount=200.)
    travelPot.addContribution(person='Laura',     amount=200.)
    travelPot.addContribution(person='Carles',    amount=200.)
    travelPot.addContribution(person='Meritxell', amount=200.)
    travelPot.addContribution(person='Xavier',    amount=200.)
    travelPot.addContribution(person='Raquel',    amount=200.)
    travelPot.addContribution(person='Marc',      amount=100.)
    travelPot.addContribution(person='Roger',     amount=0.)
    travelPot.addContribution(person='Cecilia',   amount=0.)
    travelPot.addContribution(person='Albert',    amount=130.)

    # Adding expenses
    expenseDict = {}

    # Allotjament dia 1
    expenseDict["Allotjament1"] = expense.expense()
    expenseDict["Allotjament1"].setExpenseName("Allotjament1")
    expenseDict["Allotjament1"].addPayerAndAmount(payerName='Roger', amount=443)
    expenseDict["Allotjament1"].addBeneficiary(beneficiaryName='Miquel')
    expenseDict["Allotjament1"].addBeneficiary(beneficiaryName='Montse')
    expenseDict["Allotjament1"].addBeneficiary(beneficiaryName='Laura')
    expenseDict["Allotjament1"].addBeneficiary(beneficiaryName='Carles')
    expenseDict["Allotjament1"].addBeneficiary(beneficiaryName='Meritxell')
    expenseDict["Allotjament1"].addBeneficiary(beneficiaryName='Xavier')
    expenseDict["Allotjament1"].addBeneficiary(beneficiaryName='Raquel')
    expenseDict["Allotjament1"].addBeneficiary(beneficiaryName='Cecilia')
    expenseDict["Allotjament1"].addBeneficiary(beneficiaryName='Albert')
    expenseDict["Allotjament1"].computePricePerParticipant()

    # Allotjament dia 2
    expenseDict["Allotjament2"] = expense.expense()
    expenseDict["Allotjament2"].setExpenseName("Allotjament2")
    expenseDict["Allotjament2"].addPayerAndAmount(payerName='Roger', amount=443)
    expenseDict["Allotjament2"].addBeneficiary(beneficiaryName='Miquel')
    expenseDict["Allotjament2"].addBeneficiary(beneficiaryName='Montse')
    expenseDict["Allotjament2"].addBeneficiary(beneficiaryName='Laura')
    expenseDict["Allotjament2"].addBeneficiary(beneficiaryName='Carles')
    expenseDict["Allotjament2"].addBeneficiary(beneficiaryName='Meritxell')
    expenseDict["Allotjament2"].addBeneficiary(beneficiaryName='Xavier')
    expenseDict["Allotjament2"].addBeneficiary(beneficiaryName='Raquel')
    expenseDict["Allotjament2"].addBeneficiary(beneficiaryName='Marc')
    expenseDict["Allotjament2"].addBeneficiary(beneficiaryName='Cecilia')
    expenseDict["Allotjament2"].addBeneficiary(beneficiaryName='Albert')
    expenseDict["Allotjament2"].computePricePerParticipant()

    # Vols Barcelona
    expenseDict["Vols Barcelona"] = expense.expense()
    expenseDict["Vols Barcelona"].setExpenseName("Vols Barcelona")
    expenseDict["Vols Barcelona"].addPayerAndAmount(payerName='Xavier', amount=229)
    expenseDict["Vols Barcelona"].addBeneficiary(beneficiaryName='Miquel')
    expenseDict["Vols Barcelona"].addBeneficiary(beneficiaryName='Montse')
    expenseDict["Vols Barcelona"].addBeneficiary(beneficiaryName='Laura')
    expenseDict["Vols Barcelona"].addBeneficiary(beneficiaryName='Carles')
    expenseDict["Vols Barcelona"].addBeneficiary(beneficiaryName='Meritxell')
    expenseDict["Vols Barcelona"].addBeneficiary(beneficiaryName='Raquel')
    expenseDict["Vols Barcelona"].computePricePerParticipant()

    # Alcohols Mercadona
    expenseDict["Alcohol Mercadona"] = expense.expense()
    expenseDict["Alcohol Mercadona"].setExpenseName("Alcohol Mercadona")
    expenseDict["Alcohol Mercadona"].addPayerAndAmount(payerName='Roger', amount=(12.99*2 + 12.89*2))
    expenseDict["Alcohol Mercadona"].addBeneficiary(beneficiaryName='Miquel')
    expenseDict["Alcohol Mercadona"].addBeneficiary(beneficiaryName='Montse')
    expenseDict["Alcohol Mercadona"].addBeneficiary(beneficiaryName='Laura')
    expenseDict["Alcohol Mercadona"].addBeneficiary(beneficiaryName='Carles')
    expenseDict["Alcohol Mercadona"].addBeneficiary(beneficiaryName='Meritxell')
    expenseDict["Alcohol Mercadona"].addBeneficiary(beneficiaryName='Xavier')
    expenseDict["Alcohol Mercadona"].addBeneficiary(beneficiaryName='Raquel')
    expenseDict["Alcohol Mercadona"].addBeneficiary(beneficiaryName='Marc')
    expenseDict["Alcohol Mercadona"].addBeneficiary(beneficiaryName='Cecilia')
    expenseDict["Alcohol Mercadona"].addBeneficiary(beneficiaryName='Albert')
    expenseDict["Alcohol Mercadona"].computePricePerParticipant()

    # Compra Carrefour
    expenseDict["Compra Carrefour"] = expense.expense()
    expenseDict["Compra Carrefour"].setExpenseName("Compra Carrefour")
    expenseDict["Compra Carrefour"].addPayerAndAmount(payerName='Cecilia', amount=(160.44+17.42))
    expenseDict["Compra Carrefour"].addBeneficiary(beneficiaryName='Miquel')
    expenseDict["Compra Carrefour"].addBeneficiary(beneficiaryName='Montse')
    expenseDict["Compra Carrefour"].addBeneficiary(beneficiaryName='Laura')
    expenseDict["Compra Carrefour"].addBeneficiary(beneficiaryName='Carles')
    expenseDict["Compra Carrefour"].addBeneficiary(beneficiaryName='Meritxell')
    expenseDict["Compra Carrefour"].addBeneficiary(beneficiaryName='Xavier')
    expenseDict["Compra Carrefour"].addBeneficiary(beneficiaryName='Raquel')
    expenseDict["Compra Carrefour"].addBeneficiary(beneficiaryName='Marc')
    expenseDict["Compra Carrefour"].addBeneficiary(beneficiaryName='Roger')
    expenseDict["Compra Carrefour"].addBeneficiary(beneficiaryName='Albert')
    expenseDict["Compra Carrefour"].computePricePerParticipant()

    # Dinar dissabte
    expenseDict["Dinar dissabte"] = expense.expense()
    expenseDict["Dinar dissabte"].setExpenseName("Dinar dissabte")
    expenseDict["Dinar dissabte"].addPayerAndAmount(payerName='Roger', amount=327)
    expenseDict["Dinar dissabte"].addBeneficiary(beneficiaryName='Miquel')
    expenseDict["Dinar dissabte"].addBeneficiary(beneficiaryName='Montse')
    expenseDict["Dinar dissabte"].addBeneficiary(beneficiaryName='Laura')
    expenseDict["Dinar dissabte"].addBeneficiary(beneficiaryName='Carles')
    expenseDict["Dinar dissabte"].addBeneficiary(beneficiaryName='Meritxell')
    expenseDict["Dinar dissabte"].addBeneficiary(beneficiaryName='Xavier')
    expenseDict["Dinar dissabte"].addBeneficiary(beneficiaryName='Raquel')
    expenseDict["Dinar dissabte"].addBeneficiary(beneficiaryName='Cecilia')
    expenseDict["Dinar dissabte"].addBeneficiary(beneficiaryName='Albert')
    expenseDict["Dinar dissabte"].computePricePerParticipant()

    # Tub 1 partit
    expenseDict["Partit tub 1"] = expense.expense()
    expenseDict["Partit tub 1"].setExpenseName("Partit tub 1")
    expenseDict["Partit tub 1"].addPayerAndAmount(payerName='Roger', amount=81)
    expenseDict["Partit tub 1"].addBeneficiary(beneficiaryName='Miquel')
    expenseDict["Partit tub 1"].addBeneficiary(beneficiaryName='Montse')
    expenseDict["Partit tub 1"].addBeneficiary(beneficiaryName='Laura')
    expenseDict["Partit tub 1"].addBeneficiary(beneficiaryName='Carles')
    expenseDict["Partit tub 1"].addBeneficiary(beneficiaryName='Meritxell')
    expenseDict["Partit tub 1"].addBeneficiary(beneficiaryName='Xavier')
    expenseDict["Partit tub 1"].addBeneficiary(beneficiaryName='Raquel')
    expenseDict["Partit tub 1"].addBeneficiary(beneficiaryName='Marc')
    expenseDict["Partit tub 1"].addBeneficiary(beneficiaryName='Cecilia')
    expenseDict["Partit tub 1"].addBeneficiary(beneficiaryName='Albert')
    expenseDict["Partit tub 1"].computePricePerParticipant()

    # Tub 2, 3, 4 partit
    expenseDict["Partit tubs 2, 3, 4"] = expense.expense()
    expenseDict["Partit tubs 2, 3, 4"].setExpenseName("Partit tubs 2, 3, 4")
    expenseDict["Partit tubs 2, 3, 4"].addPayerAndAmount(payerName='Marc', amount=243)
    expenseDict["Partit tubs 2, 3, 4"].addBeneficiary(beneficiaryName='Miquel')
    expenseDict["Partit tubs 2, 3, 4"].addBeneficiary(beneficiaryName='Montse')
    expenseDict["Partit tubs 2, 3, 4"].addBeneficiary(beneficiaryName='Laura')
    expenseDict["Partit tubs 2, 3, 4"].addBeneficiary(beneficiaryName='Carles')
    expenseDict["Partit tubs 2, 3, 4"].addBeneficiary(beneficiaryName='Meritxell')
    expenseDict["Partit tubs 2, 3, 4"].addBeneficiary(beneficiaryName='Xavier')
    expenseDict["Partit tubs 2, 3, 4"].addBeneficiary(beneficiaryName='Raquel')
    expenseDict["Partit tubs 2, 3, 4"].addBeneficiary(beneficiaryName='Roger')
    expenseDict["Partit tubs 2, 3, 4"].addBeneficiary(beneficiaryName='Cecilia')
    expenseDict["Partit tubs 2, 3, 4"].addBeneficiary(beneficiaryName='Albert')
    expenseDict["Partit tubs 2, 3, 4"].computePricePerParticipant()

    # T10
    expenseDict["T10"] = expense.expense()
    expenseDict["T10"].setExpenseName("T10")
    expenseDict["T10"].addPayerAndAmount(payerName='Xavier', amount=39.90)
    expenseDict["T10"].addBeneficiary(beneficiaryName='Miquel')
    expenseDict["T10"].addBeneficiary(beneficiaryName='Montse')
    expenseDict["T10"].addBeneficiary(beneficiaryName='Laura')
    expenseDict["T10"].addBeneficiary(beneficiaryName='Carles')
    expenseDict["T10"].addBeneficiary(beneficiaryName='Meritxell')
    expenseDict["T10"].addBeneficiary(beneficiaryName='Raquel')
    expenseDict["T10"].addBeneficiary(beneficiaryName='Albert')
    expenseDict["T10"].computePricePerParticipant()

    # Birres aeroport
    expenseDict["Birres aeroport"] = expense.expense()
    expenseDict["Birres aeroport"].setExpenseName("Birres aeroport")
    expenseDict["Birres aeroport"].addPayerAndAmount(payerName='Xavier', amount=17.25)
    expenseDict["Birres aeroport"].addBeneficiary(beneficiaryName='Miquel')
    expenseDict["Birres aeroport"].addBeneficiary(beneficiaryName='Montse')
    expenseDict["Birres aeroport"].addBeneficiary(beneficiaryName='Laura')
    expenseDict["Birres aeroport"].addBeneficiary(beneficiaryName='Carles')
    expenseDict["Birres aeroport"].addBeneficiary(beneficiaryName='Meritxell')
    expenseDict["Birres aeroport"].addBeneficiary(beneficiaryName='Raquel')
    expenseDict["Birres aeroport"].addBeneficiary(beneficiaryName='Albert')
    expenseDict["Birres aeroport"].computePricePerParticipant()

    # Tren GVA-Aeroport
    expenseDict["Tren GVA aeroport"] = expense.expense()
    expenseDict["Tren GVA aeroport"].setExpenseName("Tren GVA aeroport")
    expenseDict["Tren GVA aeroport"].addPayerAndAmount(payerName='Xavier', amount=11.41)
    expenseDict["Tren GVA aeroport"].addBeneficiary(beneficiaryName='Miquel')
    expenseDict["Tren GVA aeroport"].addBeneficiary(beneficiaryName='Montse')
    expenseDict["Tren GVA aeroport"].addBeneficiary(beneficiaryName='Laura')
    expenseDict["Tren GVA aeroport"].addBeneficiary(beneficiaryName='Carles')
    expenseDict["Tren GVA aeroport"].addBeneficiary(beneficiaryName='Meritxell')
    expenseDict["Tren GVA aeroport"].addBeneficiary(beneficiaryName='Raquel')
    expenseDict["Tren GVA aeroport"].addBeneficiary(beneficiaryName='Albert')
    expenseDict["Tren GVA aeroport"].computePricePerParticipant()

    # Embotit
    expenseDict["Embotit"] = expense.expense()
    expenseDict["Embotit"].setExpenseName("Embotit")
    expenseDict["Embotit"].addPayerAndAmount(payerName='Albert', amount=45)
    expenseDict["Embotit"].addBeneficiary(beneficiaryName='Miquel')
    expenseDict["Embotit"].addBeneficiary(beneficiaryName='Montse')
    expenseDict["Embotit"].addBeneficiary(beneficiaryName='Laura')
    expenseDict["Embotit"].addBeneficiary(beneficiaryName='Carles')
    expenseDict["Embotit"].addBeneficiary(beneficiaryName='Meritxell')
    expenseDict["Embotit"].addBeneficiary(beneficiaryName='Xavier')
    expenseDict["Embotit"].addBeneficiary(beneficiaryName='Raquel')
    expenseDict["Embotit"].addBeneficiary(beneficiaryName='Marc')
    expenseDict["Embotit"].addBeneficiary(beneficiaryName='Cecilia')
    expenseDict["Embotit"].addBeneficiary(beneficiaryName='Roger')
    expenseDict["Embotit"].computePricePerParticipant()


    expensemanager = expense.expenseManager(expensesDict=expenseDict)
    expensemanager.compute()

    dictPot      = travelPot.retrieveDict()
    dictExpenses = expensemanager.retrieveDict()[0]
    dictPaid     = expensemanager.retrieveDict()[1]

    # Compute and print Totals
    printSummary(dictPot=dictPot, dictExpenses=dictExpenses, dictPaid=dictPaid)

