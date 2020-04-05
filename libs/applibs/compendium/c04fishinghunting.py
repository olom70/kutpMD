import os
import sys
import libs.applibs.compendium.abstractcompendium as abstractcompendium

class FishingHunting(abstractcompendium.Compendium):

    def __init__(self):
        super().__init__()

        self.metValue  = {4001 : 3.5
            ,4005 : 4.5
            ,4007 : 4.0
            ,4010 : 4.3
            ,4020 : 4.0
            ,4030 : 2.0
            ,4040 : 3.5
            ,4050 : 6.0
            ,4060 : 2.0
            ,4061 : 1.8
            ,4062 : 3.5
            ,4063 : 3.8
            ,4064 : 3.0
            ,4065 : 2.3
            ,4070 : 2.5
            ,4080 : 6.0
            ,4081 : 11.3
            ,4083 : 4.0
            ,4085 : 2.5
            ,4086 : 2.0
            ,4090 : 2.5
            ,4095 : 3.0
            ,4100 : 5.0
            ,4110 : 6.0
            ,4115 : 3.3
            ,4120 : 5.0
            ,4123 : 3.3
            ,4124 : 2.0
            ,4125 : 9.5
            ,4130 : 2.5
            ,4140 : 2.3
            ,4145 : 2.5}

        # Unpacking with * works with any object that is iterable and, since dictionaries return their keys when iterated through, you can easily create a list by using it within a list literal.
        self.ckeys = [*self.metValue] # another option : list(self.metValue.keys())

        self.metDescription  = {4001 : "fishing, general"
            ,4005 : "fishing, crab fishing"
            ,4007 : "fishing, catching fish with hands"
            ,4010 : "fishing related, digging worms, with shovel"
            ,4020 : "fishing from river bank and walking"
            ,4030 : "fishing from boat or canoe, sitting"
            ,4040 : "fishing from river bank, standing (Taylor Code 660)"
            ,4050 : "fishing in stream, in waders (Taylor Code 670)"
            ,4060 : "fishing, ice, sitting"
            ,4061 : "fishing, jog or line, standing, general"
            ,4062 : "fishing, dip net, setting net and retrieving fish, general"
            ,4063 : "fishing, set net, setting net and retrieving fish, general"
            ,4064 : "fishing, fishing wheel, setting net and retrieving fish, general"
            ,4065 : "fishing with a spear, standing"
            ,4070 : "hunting, bow and arrow, or crossbow"
            ,4080 : "hunting, deer, elk, large game (Taylor Code 170)"
            ,4081 : "hunting large game, dragging carcass"
            ,4083 : "hunting large marine animals"
            ,4085 : "hunting large game, from a hunting stand, limited walking"
            ,4086 : "hunting large game from a car, plane, or boat"
            ,4090 : "hunting, duck, wading"
            ,4095 : "hunting, flying fox, squirrel"
            ,4100 : "hunting, general"
            ,4110 : "hunting, pheasants or grouse (Taylor Code 680)"
            ,4115 : "hunting, birds"
            ,4120 : "hunting, rabbit, squirrel, prairie chick, raccoon, small game (Taylor Code 690)"
            ,4123 : "hunting, pigs, wild"
            ,4124 : "trapping game, general"
            ,4125 : "hunting, hiking with hunting gear"
            ,4130 : "pistol shooting or trap shooting, standing"
            ,4140 : "rifle exercises, shooting, lying down"
            ,4145 : "rifle exercises, shooting, kneeling or standing"}

        self.metDescription_fr  = {4001 : "pêche, général"
            ,4005 : "pêche, pêche au crabe"
            ,4007 : "pêche, capture du poisson à la main"
            ,4010 : "activités liées à la pêche, recherche de vers, avec une pelle"
            ,4020 : "pêcher depuis la rive et marcher"
            ,4030 : "pêcher depuis un bateau ou canoë, position assise"
            ,4040 : "pêche depuis la rive, position debout (code Taylor 660)"
            ,4050 : "pêcher dans le courant, avec des cuissardes (code Taylor 670)"
            ,4060 : "pêche, glace, position assise"
            ,4061 : "pêcher, à la turlutte ou à la ligne, en position debout, général"
            ,4062 : "pêcher, épuisette, placer le filet et récupérer le poisson, général"
            ,4063 : "pêcher, filet fixe, poser le filet et récupérer le poisson, général"
            ,4064 : "pêcher, moulinet, placer le filet et récupérer le poisson, général"
            ,4065 : "pêcher au harpon, debout"
            ,4070 : "chasse, arc et flèches ou arbalète"
            ,4080 : "chasse, cerf, élan, gros gibier (code Taylor 170)"
            ,4081 : "chasse au gros gibier, en traînant la carcasse"
            ,4083 : "chasse aux gros animaux marins"
            ,4085 : "chasse au gros gibier, depuis une cache, peu de marche"
            ,4086 : "chasse au gros gibier à partir d'une voiture, un avion ou un bateau"
            ,4090 : "chasse, canard, échassier"
            ,4095 : "chasse, roussette, écureuil"
            ,4100 : "chasse, général"
            ,4110 : "chasse, faisans ou tétras (code Taylor 680)"
            ,4115 : "chasse, oiseaux"
            ,4120 : "chasse, lapin, écureuil, tétra des prairies, raton laveur, petit gibier (code Taylor 690)"
            ,4123 : "chasse, cochons sauvages"
            ,4124 : "piégeage, général"
            ,4125 : "chasse, randonnée avec équipement de chasse"
            ,4130 : "tir au pistolet ou ball-trap, position debout"
            ,4140 : "exercices de tir, position couchée"
            ,4145 : "exercices de tir, agenouillé ou en position debout"}        

    def printValues(self):
        print("Beginning dump for 'FishingHunting' ")
        super().printValues()

    def getMetValue(self, code):
        return super().getMetValue(code)

if __name__ == "__main__":
    b = FishingHunting()
    b.printValues()
    print(b.getMetValue(4145))
    for l in b:
        print(l)