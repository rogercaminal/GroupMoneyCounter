import os, sys, pot, expense, config, summary

debug = False
#________________________________________________________________________________________________
if __name__=="__main__":

    fileName = sys.argv[1]
    c = config.config(fileName)
    c.process()

    # Adding pot
    Pot = pot.pot()

    # Adding everyone (loop since initial amount is 0 for everyone)
    for person in c.pot.keys():
        Pot.addContribution(person=person, amount=c.pot[person])

    # Adding expenses
    expenseDict = {}
    expenseList = c.expenses.keys()
    expenseList.sort()
    for e in expenseList:
        expenseDict[e] = expense.expense()
        expenseDict[e].setExpenseName(e)
        for p in c.expenses[e]["PAYER"]:
            expenseDict[e].addPayerAndAmount(payerName=p[0], amount=p[1])
        for p in c.expenses[e]["BENEFICIARY"]:
            expenseDict[e].addBeneficiary(beneficiaryName=p)
        expenseDict[e].computePricePerParticipant()

    # Create expense manager
    expensemanager = expense.expenseManager(expensesDict=expenseDict)
    expensemanager.compute()

    # Compute and print Totals
    summary = summary.summary(pot=Pot, expensemanager=expensemanager, expenseDict=expenseDict, debug=debug)
    summary.printTotals()
    summary.printCorrespondences()
