**Author:**
  Roger Caminal Armadans (roger.caminal@gmail.com)
**created:**  31-12-2016
**Last modified:** 31-12-2016

# Why GroupMoneyCounter?

This package allows to adjust the money spent by different members of a group.

# How does it work?

First you need to import the classes pot.py and expense.py 

```bash
import pot, expense
```

Then, dedeclare a pot:

```bash
travelPot = pot.pot()
```

Add the people that is participating. If there's an initial pot, add it in the `amount` field.

```bash
travelPot.addContribution(person='John', amount=50.)
travelPot.addContribution(person='Steve', amount=10.)
travelPot.addContribution(person='Ann', amount=0.)
```

Then you need to create the dictionary with the expenses:

```bash
expenseDict = {}
```

And fill it with the different expenses, adding the information about who paid and among whom this needs to be shared. Don't forget to `computePricePerParticipant()` to enable the expense.

```bash
expenseDict["expenseA"] = expense.expense()
expenseDict["expenseA"].setExpenseName("expenseA")
expenseDict["expenseA"].addPayerAndAmount(payerName='John', amount=100.)
expenseDict["expenseA"].addBeneficiary(beneficiaryName='Steve')
expenseDict["expenseA"].addBeneficiary(beneficiaryName='Ann')
expenseDict["expenseA"].computePricePerParticipant()
```

Add the dictionary to the `expenseManager` and retrieve the information:

```bash
expensemanager = expense.expenseManager(expensesDict=expenseDict)
expensemanager.compute()

dictPot      = travelPot.retrieveDict()
dictExpenses = expensemanager.retrieveDict()[0]
dictPaid     = expensemanager.retrieveDict()[1]
```

Finally print the information to copy&paste to the members of the group:

```bash
printSummary(dictPot=dictPot, dictExpenses=dictExpenses, dictPaid=dictPaid)
```
