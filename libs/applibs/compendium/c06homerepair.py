import os
import sys
import libs.applibs.compendium.abstractcompendium as abstractcompendium

class HomeRepair(abstractcompendium.Compendium):

    def __init__(self):
        super().__init__()

        self.metValue  = {6010 : 3.0
            ,6020 : 4.0
            ,6030 : 3.3
            ,6040 : 3.0
            ,6050 : 6.0
            ,6052 : 3.8
            ,6060 : 3.3
            ,6070 : 6.0
            ,6072 : 4.0
            ,6074 : 2.3
            ,6080 : 5.0
            ,6090 : 4.5
            ,6100 : 5.0
            ,6110 : 5.0
            ,6120 : 5.0
            ,6122 : 5.0
            ,6124 : 3.0
            ,6126 : 2.5
            ,6127 : 4.5
            ,6128 : 6.0
            ,6130 : 4.5
            ,6140 : 3.8
            ,6144 : 3.0
            ,6150 : 5.0
            ,6160 : 3.3
            ,6165 : 4.5
            ,6167 : 3.0
            ,6170 : 3.0
            ,6180 : 6.0
            ,6190 : 4.5
            ,6200 : 4.5
            ,6205 : 2.0
            ,6210 : 5.0
            ,6220 : 4.5
            ,6225 : 2.0
            ,6230 : 4.5
            ,6240 : 3.3 }

        # Unpacking with * works with any object that is iterable and, since dictionaries return their keys when iterated through, you can easily create a list by using it within a list literal.
        self.ckeys = [*self.metValue] # another option : list(self.metValue.keys())

        self.metDescription  = {6010 : "airplane repair"
            ,6020 : "automobile body work"
            ,6030 : "automobile repair, light or moderate effort"
            ,6040 : "carpentry, general, workshop (Taylor Code 620)"
            ,6050 : "carpentry, outside house, installing rain gutters (Taylor Code 640),carpentry, outside house, building a fence"
            ,6052 : "carpentry, outside house, building a fence"
            ,6060 : "carpentry, finishing or refinishing cabinets or furniture"
            ,6070 : "carpentry, sawing hardwood"
            ,6072 : "carpentry, home remodeling tasks, moderate effort"
            ,6074 : "carpentry, home remodeling tasks, light effort "
            ,6080 : "caulking, chinking log cabin"
            ,6090 : "caulking, except log cabin"
            ,6100 : "cleaning gutters"
            ,6110 : "excavating garage"
            ,6120 : "hanging storm windows"
            ,6122 : "hanging sheet rock inside house"
            ,6124 : "hammering nails"
            ,6126 : "home repair, general, light effort"
            ,6127 : "home repair, general, moderate effort"
            ,6128 : "home repair, general, vigorous effort"
            ,6130 : "laying or removing carpet"
            ,6140 : "laying tile or linoleum,repairing appliances"
            ,6144 : "repairing appliances"
            ,6150 : "painting, outside home (Taylor Code 650)"
            ,6160 : "painting inside house,wallpapering, scraping paint"
            ,6165 : "painting, (Taylor Code 630)"
            ,6167 : "plumbing, general"
            ,6170 : "put on and removal of tarp - sailboat"
            ,6180 : "roofing"
            ,6190 : "sanding floors with a power sander"
            ,6200 : "scraping and painting sailboat or powerboat"
            ,6205 : "sharpening tools"
            ,6210 : "spreading dirt with a shovel"
            ,6220 : "washing and waxing hull of sailboat or airplane"
            ,6225 : "washing and waxing car"
            ,6230 : "washing fence, painting fence, moderate effort"
            ,6240 : "wiring, tapping-splicing"}

        self.metDescription_fr  = {6010 : "réparation d'un avion"
            ,6020 : "travailler sur la carrosserie d'une automobile"
            ,6030 : "réparation automobile, effort léger ou modéré"
            ,6040 : "menuiserie, général, atelier (code Taylor 620)"
            ,6050 : "menuiserie, extérieur de la maison, installer des gouttières, construire une clôture (code Taylor 640)"
            ,6052 : "menuiserie, extérieur de la maison, construire une clôture"
            ,6060 : "menuiserie, finition ou restauration de meubles"
            ,6070 : "menuiserie, scier du bois de feuillus"
            ,6072 : "menuiserie, travaux de rénovation résidentielle, effort modéré"
            ,6074 : "menuiserie, travaux de rénovation résidentielle, effort léger"
            ,6080 : "calfeutrer, isoler une cabane en bois"
            ,6090 : "calfeutrer, hors cabane"
            ,6100 : "nettoyer les gouttières"
            ,6110 : "creuser un garage"
            ,6120 : "poser des doubles fenêtres"
            ,6122 : "poser des plaques de plâtre à l’intérieur d’une maison"
            ,6124 : "planter des clous"
            ,6126 : "réparation domestique, général, effort léger"
            ,6127 : "réparation domestique, général, effort modéré"
            ,6128 : "réparation domestique, général, effort vigoureux"
            ,6130 : "poser ou retirer de la moquette"
            ,6140 : "poser du carrelage ou du linoléum, réparer des appareils"
            ,6144 : "réparer des appareils"
            ,6150 : "peindre, extérieur de la maison (code Taylor 650)"
            ,6160 : "peindre, intérieur de la maison, papier peint, décapage de peinture"
            ,6165 : "peindre, (code Taylor 630)"
            ,6167 : "plomberie, général"
            ,6170 : "poser et retirer une bâche – voilier"
            ,6180 : "poser la toiture"
            ,6190 : "poncer les sols avec une ponceuse"
            ,6200 : "décaper et peindre un voilier ou un hors-bord"
            ,6205 : "affûter des outils"
            ,6210 : "étaler de la terre à l'aide d'une pelle"
            ,6220 : "laver et cirer la coque d'un voilier ou un avion"
            ,6225 : "laver et cirer une voiture"
            ,6230 : "laver une clôture, peindre une clôture, effort modéré"
            ,6240 : "câblage, dériver-connecter"}        

    def printValues(self):
        print("Beginning dump for 'HomeRepair' ")
        super().printValues()

    def getMetValue(self, code):
        return super().getMetValue(code)

if __name__ == "__main__":
    b = HomeRepair()
    b.printValues()
    print(b.getMetValue(6020))
    for l in b:
        print(l)