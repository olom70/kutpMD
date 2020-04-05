import os
import sys
import libs.applibs.compendium.abstractcompendium as abstractcompendium

class Running(abstractcompendium.Compendium):

    def __init__(self):
        super().__init__()

        self.metValue  = {12010 : 6.0 
            ,12020 : 7.0 
            ,12025 : 8.0 
            ,12027 : 4.5 
            ,12029 : 6.0
            ,12030 : 8.3 
            ,12040 : 9.0
            ,12050 : 9.8 
            ,12060 : 10.5
            ,12070 : 11.0 
            ,12080 : 11.8
            ,12090 : 11.8
            ,12100 : 12.3
            ,12110 : 12.8
            ,12120 : 14.5 
            ,12130 : 16.0
            ,12132 : 19.0
            ,12134 : 19.8
            ,12135 : 23.0
            ,12140 : 9.0
            ,12150 : 8.0 
            ,12170 : 15.0 
            ,12180 : 10.0 
            ,12190 : 8.0 
            ,12200 : 13.3}

        # Unpacking with * works with any object that is iterable and, since dictionaries return their keys when iterated through, you can easily create a list by using it within a list literal.
        self.ckeys = [*self.metValue] # another option : list(self.metValue.keys())

        self.metDescription  = {12010 : "jog/walk combination (jogging component of less than 10 minutes) (Taylor Code 180)"
            ,12020 : "jogging, general"
            ,12025 : "jogging, in place"
            ,12027 : "jogging, on a mini-tramp"
            ,12029 : "running, 4 mph (15 min/mile)"
            ,12030 : "running, 5 mph (12 min/mile)"
            ,12040 : "running, 5.2 mph (11.5 min/mile)"
            ,12050 : "running, 6 mph (10 min/mile)"
            ,12060 : "running, 6.7 mph (9 min/mile)"
            ,12070 : "running, 7 mph (8.5 min/mile)"
            ,12080 : "running, 7.5 mph (8 min/mile)"
            ,12090 : "running, 8 mph (7.5 min/mile)"
            ,12100 : "running, 8.6 mph (7 min/mile)"
            ,12110 : "running, 9 mph (6.5 min/mile)"
            ,12120 : "running, 10 mph (6 min/mile)"
            ,12130 : "running, 11 mph (5.5 min/mile)"
            ,12132 : "running, 12 mph (5 min/mile)"
            ,12134 : "running, 13 mph (4.6 min/mile)"
            ,12135 : "running, 14 mph (4.3 min/mile)"
            ,12140 : "running, cross country"
            ,12150 : "running, (Taylor code 200)"
            ,12170 : "running, stairs, up"
            ,12180 : "running, on a track, team practice"
            ,12190 : "running, training, pushing a wheelchair or baby carrier"
            ,12200 : "running, marathon"}

        self.metDescription_fr  = {12010 : "combinaison jogging/marche (composant jogging inférieur à 10 minutes) (code Taylor 180)"
            ,12020 : "jogging, général"
            ,12025 : "jogging, sur-place"
            ,12027 : "jogging, sur un mini-trampoline"
            ,12029 : "courir à 6,5 km/h (9 min/km)"
            ,12030 : "courir à 8 km/h (7,5 min/km)"
            ,12040 : "courir à 8,4 km/h (7,3 min/km)"
            ,12050 : "courir à 9,6 km/h (6,25 min/km)"
            ,12060 : "courir à 10.8 km/h (5,5 min/km)"
            ,12070 : "courir à 11,25 km/h (5,3 min/km)"
            ,12080 : "courir à 12 km/h (5 min/km)"
            ,12090 : "courir à 12,9 km/h (4,65 min/km)"
            ,12100 : "courir à 13,8 km/h (4,3 min/km)"
            ,12110 : "courir à 14,5 km/h (4,1 min/km)"
            ,12120 : "courir à 16 km/h (3,75 min/km)"
            ,12130 : "courir à 17,7 km/h (3,4 min/km)"
            ,12132 : "courir à 19,3 km/h (3,1 min/km)"
            ,12134 : "courir à 20,9 km/h (2,9 min/km)"
            ,12135 : "courir à 22,5 km/h (2,66 min/km)"
            ,12140 : "courir, cross"
            ,12150 : "courir (code Taylor 200)"
            ,12170 : "courir, escaliers, montée"
            ,12180 : "courir, sur une piste, entraînement d’équipe"
            ,12190 : "courir, entraînement, pousser un fauteuil roulant ou landau"
            ,12200 : "courir, marathon"}

    def printValues(self):
        print("Beginning dump for 'Running' ")
        super().printValues()

    def getMetValue(self, code):
        return super().getMetValue(code)

if __name__ == "__main__":
    b = Running()
    b.printValues()
    print(b.getMetValue(12132))
    for l in b:
        print(l)