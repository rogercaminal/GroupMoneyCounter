import os

class config(object):
    def __init__(self, fileName):
        self.fileName = fileName
        self.participants = {}
        self.pot = {}
        self.expenses = {}

    def __str__(self):
        string = str(self.participants)+'\n'
        string = str(self.pot)+'\n'
        string = str(self.expenses)+'\n'
        return string

    def process(self):
        f = open(self.fileName)
        lines = f.readlines()
        for line in lines:
            l = line.split()
            if "#" in line:
                continue

            if "PARTICIPANT" in line:
                if l[1] not in self.participants.keys():
                    self.participants[l[1]] = []
                if "All" not in self.participants.keys():
                    self.participants["All"] = []
                self.participants[l[1]].append(l[2])
                if l[2] not in self.participants["All"]:
                    self.participants["All"].append(l[2])

            if "POT" in line:
                if l[1] in self.participants.keys():
                    for p in self.participants[l[1]]:
                        self.pot[p] = float(l[2])
                else:
                    self.pot[l[1]] = float(l[2])

            if "EXPENSE" in line:
                if l[1] not in self.expenses.keys():
                    self.expenses[l[1]] = {}
                    self.expenses[l[1]]["PAYER"] = []
                    self.expenses[l[1]]["BENEFICIARY"] = []
                if "PAYER" in line:
                    self.expenses[l[1]]["PAYER"].append([l[3], float(l[4])])
                if "BENEFICIARY" in line:
                    self.expenses[l[1]]["BENEFICIARY"] = self.participants[l[3]]

        f.close()
