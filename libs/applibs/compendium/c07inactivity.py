import os
import sys
import libs.applibs.compendium.abstractcompendium as abstractcompendium

class Inactivity(abstractcompendium.Compendium):

    def __init__(self):
        super().__init__()

        self.metValue  = {7010 : 1.0 
            ,7011 : 1.3 
            ,7020 : 1.3 
            ,7021 : 1.3
            ,7022 : 1.5
            ,7023 : 1.8
            ,7024 : 1.3
            ,7025 : 1.5
            ,7026 : 1.3
            ,7030 : 0.95 
            ,7040 : 1.3 
            ,7041 : 1.8
            ,7050 : 1.3 
            ,7060 : 1.3 
            ,7070 : 1.3 
            ,7075 : 1.0}

        # Unpacking with * works with any object that is iterable and, since dictionaries return their keys when iterated through, you can easily create a list by using it within a list literal.
        self.ckeys = [*self.metValue] # another option : list(self.metValue.keys())

        self.metDescription  = {7010 : "lying quietly and watching television"
            ,7011 : "lying quietly, doing nothing, lying in bed awake, listening to music (not talking or reading)"
            ,7020 : "sitting quietly and watching television"
            ,7021 : "sitting quietly, general"
            ,7022 : "sitting quietly, fidgeting, general, fidgeting hands"
            ,7023 : "sitting, fidgeting feet"
            ,7024 : "sitting, smoking"
            ,7025 : "sitting, listening to music (not talking or reading) or watching a movie in a theater"
            ,7026 : "sitting at a desk, resting head in hands"
            ,7030 : "sleeping"
            ,7040 : "standing quietly, standing in a line"
            ,7041 : "standing, fidgeting"
            ,7050 : "reclining, writing"
            ,7060 : "reclining, talking or talking on phone"
            ,7070 : "reclining, reading"
            ,7075 : "meditating"}

        self.metDescription_fr  = {7010 : "être allongé en silence et regarder la télévision"
            ,7011 : "être allongé en silence sans rien faire, être allongé dans un lit sans dormir, écouter de la musique (sans parler ni lire)"
            ,7020 : "être assis en silence et regarder la télévision"
            ,7021 : "être assis en silence, général"
            ,7022 : "être assis en silence, s’agiter, général, agiter les mains"
            ,7023 : "être assis, agiter les pieds"
            ,7024 : "être assis, fumer"
            ,7025 : "être assis, écouter de la musique (sans parler ni lire), regarder un film au cinéma"
            ,7026 : "être assis à un bureau, la tête dans les mains"
            ,7030 : "dormir"
            ,7040 : "être debout en silence, être dans une file d'attente"
            ,7041 : "être debout, s’agiter"
            ,7050 : "être allongé, écrire"
            ,7060 : "être allongé, parler ou parler au téléphone"
            ,7070 : "être allongé, lire"
            ,7075 : "méditer"} 

    def printValues(self):
        print("Beginning dump for 'Inactivity' ")
        super().printValues()

    def getMetValue(self, code):
        return super().getMetValue(code)

if __name__ == "__main__":
    b = Inactivity()
    b.printValues()
    print(b.getMetValue(7075))
    for l in b:
        print(l)