import os
import sys
import libs.applibs.compendium.abstractcompendium as abstractcompendium

class VolunteerActivities(abstractcompendium.Compendium):

    def __init__(self):
        super().__init__()

        self.metValue  = {21000 : 1.5 
            ,21005 : 1.5 
            ,21010 : 2.5 
            ,21015 : 2.3 
            ,21016 : 2.0 
            ,21017 : 3.0 
            ,21018 : 3.5
            ,21019 : 5.8 
            ,21020 : 3.0 
            ,21025 : 3.5 
            ,21030 : 4.5 
            ,21035 : 1.3 
            ,21040 : 2.0 
            ,21045 : 3.5 
            ,21050 : 4.3 
            ,21055 : 3.5 
            ,21060 : 4.5 
            ,21065 : 4.8 
            ,21070 : 3.0 }

        # Unpacking with * works with any object that is iterable and, since dictionaries return their keys when iterated through, you can easily create a list by using it within a list literal.
        self.ckeys = [*self.metValue] # another option : list(self.metValue.keys())

        self.metDescription  = {21000 : "sitting, meeting, general, and/or with talking involved"
            ,21005 : "sitting, light office work, in general"
            ,21010 : "sitting, moderate work"
            ,21015 : "standing, light work (filing, talking, assembling)"
            ,21016 : "sitting, child care, only active periods"
            ,21017 : "standing, child care, only active periods"
            ,21018 : "walk/run play with children, moderate, only active periods"
            ,21019 : "walk/run play with children, vigorous, only active periods"
            ,21020 : "standing, light/moderate work (e.g., pack boxes, assemble/repair, set up chairs/furniture)"
            ,21025 : "standing, moderate (lifting 50 lbs., assembling at fast rate)"
            ,21030 : "standing, moderate/heavy work"
            ,21035 : "typing, electric, manual, or computer"
            ,21040 : "walking, less than 2.0 mph, very slow"
            ,21045 : "walking, 3.0 mph, moderate speed, not carrying anything"
            ,21050 : "walking, 3.5 mph, brisk speed, not carrying anything"
            ,21055 : "walking, 2.5 mph slowly and carrying objects less than 25 pounds"
            ,21060 : "walking, 3.0 mph moderately and carrying objects less than 25 pounds, pushing something"
            ,21065 : "walking, 3.5 mph, briskly and carrying objects less than 25 pounds"
            ,21070 : "walk/stand combination, for volunteer purposes"}


        self.metDescription_fr  = {21000 : "être assis, réunion, général, et/ou impliquant une discussion"
            ,21005 : "être assis, travail de bureau léger, général"
            ,21010 : "être assis, travail modéré"
            ,21015 : "être debout, travail léger (remplissage, discussion, assemblage)"
            ,21016 : "être assis, s'occuper d'enfants, périodes actives uniquement"
            ,21017 : "être debout, s'occuper d'enfants, périodes actives uniquement"
            ,21018 : "marcher/courir, jouer avec les enfants, effort modéré, périodes actives uniquement"
            ,21019 : "marcher/courir, jouer avec des enfants, effort vigoureux, périodes actives uniquement"
            ,21020 : "être debout, travail léger/modéré (par ex. faire des cartons, assembler/réparer, installer des chaises/meubles)"
            ,21025 : "être debout, effort modéré (soulever 22,5kg, assembler à un rythme rapide)"
            ,21030 : "être debout, travail modéré/vigoureux"
            ,21035 : "taper des documents avec une machine à écrire électrique, mécanique ou un ordinateur"
            ,21040 : "marcher à moins de 3 km/h, rythme très lent"
            ,21045 : "marcher à 5 km/h, rythme modéré, sans rien porter"
            ,21050 : "marcher à 5,5 km/h, rythme rapide, sans rien porter"
            ,21055 : "marcher à 4 km/h, rythme lent, en portant des objets pesant moins de 11 kg"
            ,21060 : "marcher à 5 km/h, rythme modéré, en portant des objets pesant moins de 11 kg, en poussant quelque chose"
            ,21065 : "marcher à 6 km/h, rythme rapide, en portant des objets pesant moins de 11 kg"
            ,21070 : "combinaison marcher/arrêt debout, à des fins bénévoles"}


    def printValues(self):
        print("Beginning dump for 'VolunteerActivities' ")
        super().printValues()

    def getMetValue(self, code):
        return super().getMetValue(code)

if __name__ == "__main__":
    b = VolunteerActivities()
    b.printValues()
    print(b.getMetValue(21035))
    for l in b:
        print(l)