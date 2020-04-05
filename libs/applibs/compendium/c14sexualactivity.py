import os
import sys
import libs.applibs.compendium.abstractcompendium as abstractcompendium

class SexualActivity(abstractcompendium.Compendium):

    def __init__(self):
        super().__init__()

        self.metValue  = {14010 : 2.8
            ,14020 : 1.8
            ,14030 : 1.3 }

        # Unpacking with * works with any object that is iterable and, since dictionaries return their keys when iterated through, you can easily create a list by using it within a list literal.
        self.ckeys = [*self.metValue] # another option : list(self.metValue.keys())

        self.metDescription  = {14010 : "active, vigorous effort"
            ,14020 : "general, moderate effort"
            ,14030 : "passive, light effort, kissing, hugging"}

        self.metDescription_fr  = {14010 : "mode actif, effort vigoureux"
            ,14020 : "général, effort modéré"
            ,14030 : "mode passif, effort léger, baisers, embrassades"}

    def printValues(self):
        print("Beginning dump for 'SexualActivity' ")
        super().printValues()

    def getMetValue(self, code):
        return super().getMetValue(code)

if __name__ == "__main__":
    b = SexualActivity()
    b.printValues()
    print(b.getMetValue(14020))
    for l in b:
        print(l)