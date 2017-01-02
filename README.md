**Author:**
  Roger Caminal Armadans (roger.caminal@gmail.com)
**created:**  31-12-2016
**Last modified:** 31-12-2016

# Why GroupMoneyCounter?

This package allows to adjust the money spent by different members of a group.

# How does it work?

Create a new job option file `myjoboption.txt` in the `events/` folder.

Specify the list(s) of participants (the same participant can be in different categories).
```bash
PARTICIPANT Category1 Albert
PARTICIPANT Category1 Bill

PARTICIPANT Category2 Bill
PARTICIPANT Category2 Charlie
```
The category "All" is automatically created with a set of all the participants from the different categories.

Then, specify whether there is any initial pot for any of the participants (or category).
```bash
POT All 0
```

Add the expenses.
```bash
EXPENSE expense1 PAYER Albert 10.00
EXPENSE expense1 BENEFICIARY Category1

EXPENSE expense2 PAYER Charlie 5.00
EXPENSE expense2 BENEFICIARY Category2
```

Process the job option with the follwing command:
```bash
python compute.py events/myjoboption.txt
```
