**Author:**
  Roger Caminal Armadans (roger.caminal@gmail.com)
**created:**  31-12-2016
**Last modified:** 31-12-2016

# Why GroupMoneyCounter?

This package allows to adjust the money spent by different members of a group.

# How does it work?

First you need to import the classes pot.py and expense.py 

```python
import pot, expense
```

Then, dedeclare a pot:

```python
Pot = pot.pot()
```

Add the people that is participating. If there's an initial pot, add it in the `amount` field.

```python
Pot.addContribution(person='John', amount=50.)
Pot.addContribution(person='Steve', amount=10.)
Pot.addContribution(person='Ann', amount=0.)
```

Then you need to create the dictionary with the expenses:

```python
expenseDict = {}
```

And fill it with the different expenses, adding the information about who paid and among whom this needs to be shared. Don't forget to `computePricePerParticipant()` to enable the expense.

```python
expenseDict["expenseA"] = expense.expense()
expenseDict["expenseA"].setExpenseName("expenseA")
expenseDict["expenseA"].addPayerAndAmount(payerName='John', amount=100.)
expenseDict["expenseA"].addBeneficiary(beneficiaryName='Steve')
expenseDict["expenseA"].addBeneficiary(beneficiaryName='Ann')
expenseDict["expenseA"].computePricePerParticipant()
```

Add the dictionary to the `expenseManager` and retrieve the information:

```python
expensemanager = expense.expenseManager(expensesDict=expenseDict)
expensemanager.compute()
```

Finally print the information to copy&paste to the members of the group:

```python
import compute
compute.printSummary(pot=Pot, expensemanager=expensemanager)
```
