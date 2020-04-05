import os
import sys
import libs.applibs.compendium.abstractcompendium as abstractcompendium

class ReligiousActivities(abstractcompendium.Compendium):

    def __init__(self):
        super().__init__()

        self.metValue  = {20000 : 1.3
            ,20001 : 2.0
            ,20005 : 1.8
            ,20010 : 1.3 
            ,20015 : 1.3 
            ,20020 : 2.0 
            ,20025 : 1.3 
            ,20030 : 1.8 
            ,20035 : 2.0 
            ,20036 : 2.0 
            ,20037 : 3.5
            ,20038 : 4.3
            ,20039 : 2.0 
            ,20040 : 5.0 
            ,20045 : 2.5 
            ,20046 : 2.0 
            ,20047 : 3.3 
            ,20050 : 1.5 
            ,20055 : 2.0 
            ,20060 : 3.3
            ,20061 : 4.0 
            ,20065 : 3.5 
            ,20095 : 4.5
            ,20100 : 1.3 }

        # Unpacking with * works with any object that is iterable and, since dictionaries return their keys when iterated through, you can easily create a list by using it within a list literal.
        self.ckeys = [*self.metValue] # another option : list(self.metValue.keys())

        self.metDescription  = {20000 : "sitting in church, in service, attending a ceremony, sitting quietly"
            ,20001 : "sitting, playing an instrument at church"
            ,20005 : "sitting in church, talking or singing, attending a ceremony, sitting, active participation"
            ,20010 : "sitting, reading religious materials at home"
            ,20015 : "standing quietly in church, attending a ceremony"
            ,20020 : "standing, singing in church, attending a ceremony, standing, active participation"
            ,20025 : "kneeling in church or at home, praying"
            ,20030 : "standing, talking in church"
            ,20035 : "walking in church"
            ,20036 : "walking, less than 2.0 mph, very slow"
            ,20037 : "walking, 3.0 mph, moderate speed, not carrying anything"
            ,20038 : "walking, 3.5 mph, brisk speed, not carrying anything"
            ,20039 : "walk/stand combination for religious purposes, usher"
            ,20040 : "praise with dance or run, spiritual dancing in church"
            ,20045 : "serving food at church"
            ,20046 : "preparing food at church"
            ,20047 : "washing dishes, cleaning kitchen at church"
            ,20050 : "eating at church"
            ,20055 : "eating/talking at church or standing eating, American Indian Feast days"
            ,20060 : "cleaning church"
            ,20061 : "general yard work at church"
            ,20065 : "standing, moderate effort (e.g., lifting heavy objects, assembling at fast rate)"
            ,20095 : "standing, moderate-to-heavy effort, manual labor, lifting ≥ 50 lbs, heavy maintenance"
            ,20100 : "typing, electric, manual, or computer"}


        self.metDescription_fr  = {20000 : "être assis à l'église, pendant la messe, assister à une cérémonie, être assis en silence"
            ,20001 : "être assis, jouer d'un instrument à l'église"
            ,20005 : "être assis à l'église, parler ou chanter, assister à une cérémonie, être assis, participation active"
            ,20010 : "être assis, lire des textes religieux à la maison"
            ,20015 : "être debout à l'église (en silence), assister à une cérémonie"
            ,20020 : "être debout, chanter à l'église, assister à une cérémonie, être debout, participation active"
            ,20025 : "être à genoux à l'église ou à la maison, prier"
            ,20030 : "être debout, parler à l'église"
            ,20035 : "marcher dans l'église"
            ,20036 : "marcher à moins de 3 km/h, rythme très lent"
            ,20037 : "marcher à 5 km/h, rythme modéré, sans rien porter"
            ,20038 : "marcher à 5,5 km/h, rythme rapide, sans rien porter"
            ,20039 : "combinaison marcher/se tenir debout à des fins religieuses, placer l'assistance"
            ,20040 : "faire une louange en dansant ou en courant, danse spirituelle dans l'église"
            ,20045 : "servir des aliments à l'église"
            ,20046 : "préparer des aliments à l'église"
            ,20047 : "faire la vaisselle, nettoyer la cuisine à l'église"
            ,20050 : "manger à l'église"
            ,20055 : "manger/parler à l'église ou manger debout, fêtes religieuses"
            ,20060 : "nettoyer l'église"
            ,20061 : "travail général dans la cour de l'église"
            ,20065 : "être debout, effort modéré (soulever des objets lourds, assembler à un rythme rapide)"
            ,20095 : "être debout, effort modéré à important, travail manuel, soulevez des charges ≥ 22,5 kg, maintenance lourde"
            ,20100 : "taper des documents avec une machine à écrire électrique, mécanique ou un ordinateur"}


    def printValues(self):
        print("Beginning dump for 'ReligiousActivities' ")
        super().printValues()

    def getMetValue(self, code):
        return super().getMetValue(code)

if __name__ == "__main__":
    b = ReligiousActivities()
    b.printValues()
    print(b.getMetValue(20095))
    for l in b:
        print(l)