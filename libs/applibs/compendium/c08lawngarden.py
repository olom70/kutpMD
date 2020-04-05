import os
import sys
import libs.applibs.compendium.abstractcompendium as abstractcompendium

class LawnGarden(abstractcompendium.Compendium):

    def __init__(self):
        super().__init__()

        self.metValue  = {8009 : 3.3
            ,8010 : 5.5 
            ,8019 : 4.5
            ,8020 : 6.3 
            ,8025 : 3.5
            ,8030 : 6.3
            ,8040 : 5.0 
            ,8045 : 3.5
            ,8050 : 5.0 
            ,8052 : 7.8
            ,8055 : 2.8
            ,8057 : 8.3
            ,8058 : 5.3
            ,8060 : 5.8
            ,8065 : 2.3
            ,8070 : 4.0
            ,8080 : 6.3 
            ,8090 : 5.0 
            ,8095 : 5.5
            ,8100 : 2.5 
            ,8110 : 6.0 
            ,8120 : 5.0
            ,8125 : 4.5 
            ,8130 : 2.5
            ,8135 : 2.0
            ,8140 : 4.3 
            ,8145 : 4.3
            ,8150 : 4.5 
            ,8160 : 3.8
            ,8165 : 4.0 
            ,8170 : 4.0 
            ,8180 : 3.0 
            ,8190 : 4.0 
            ,8192 : 5.5
            ,8195 : 5.3
            ,8200 : 6.0 
            ,8202 : 7.5
            ,8210 : 4.0 
            ,8215 : 3.5 
            ,8220 : 3.0
            ,8230 : 1.5 
            ,8239 : 3.5
            ,8240 : 4.5 
            ,8241 : 5.0
            ,8245 : 3.8 
            ,8246 : 3.5 
            ,8248 : 4.5
            ,8250 : 3.3
            ,8251 : 3.0 
            ,8255 : 5.5
            ,8260 : 3.0
            ,8261 : 4.0
            ,8262 : 6.0}

        # Unpacking with * works with any object that is iterable and, since dictionaries return their keys when iterated through, you can easily create a list by using it within a list literal.
        self.ckeys = [*self.metValue] # another option : list(self.metValue.keys())

        self.metDescription  = {8009 : "carrying, loading or stacking wood, loading/unloading or carrying lumber, light-to-moderate effort"
            ,8010 : "carrying, loading or stacking wood, loading/unloading or carrying lumber"
            ,8019 : "chopping wood, splitting logs, moderate effort"
            ,8020 : "chopping wood, splitting logs, vigorous effort"
            ,8025 : "clearing light brush, thinning garden, moderate effort"
            ,8030 : "clearing brush/land, undergrowth, or ground, hauling branches, wheelbarrow chores, vigorous effort"
            ,8040 : "digging sandbox, shoveling sand"
            ,8045 : "digging, spading, filling garden, composting, light-to-moderate effort"
            ,8050 : "digging, spading, filling garden, compositing, (Taylor Code 590)"
            ,8052 : "digging, spading, filling garden, composting, vigorous effort"
            ,8055 : "driving tractor"
            ,8057 : "felling trees, large size"
            ,8058 : "felling trees, small-medium size"
            ,8060 : "gardening with heavy power tools, tilling a garden, chain saw"
            ,8065 : "gardening, using containers, older adults > 60 years"
            ,8070 : "irrigation channels, opening and closing ports"
            ,8080 : "laying crushed rock"
            ,8090 : "laying sod"
            ,8095 : "mowing lawn, general"
            ,8100 : "mowing lawn, riding mower (Taylor Code 550)"
            ,8110 : "mowing lawn, walk, hand mower (Taylor Code 570)"
            ,8120 : "mowing lawn, walk, power mower, moderate or vigorous effort"
            ,8125 : "mowing lawn, power mower, light or moderate effort (Taylor Code 590)"
            ,8130 : "operating snow blower, walking"
            ,8135 : "planting, potting, transplanting seedlings or plants, light effort"
            ,8140 : "planting seedlings, shrub, stooping, moderate effort"
            ,8145 : "planting crops or garden, stooping, moderate effort"
            ,8150 : "planting trees"
            ,8160 : "raking lawn or leaves, moderate effort"
            ,8165 : "raking lawn (Taylor Code 600)"
            ,8170 : "raking roof with snow rake"
            ,8180 : "riding snow blower"
            ,8190 : "sacking grass, leaves"
            ,8192 : "shoveling dirt or mud"
            ,8195 : "shoveling snow, by hand, moderate effort"
            ,8200 : "shovelling snow, by hand (Taylor Code 610)"
            ,8202 : "shoveling snow, by hand, vigorous effort"
            ,8210 : "trimming shrubs or trees, manual cutter"
            ,8215 : "trimming shrubs or trees, power cutter, using leaf blower, edge, moderate effort"
            ,8220 : "walking, applying fertilizer or seeding a lawn, push applicator"
            ,8230 : "watering lawn or garden, standing or walking"
            ,8239 : "weeding, cultivating garden, light-to-moderate effort"
            ,8240 : "weeding, cultivating garden (Taylor Code 580)"
            ,8241 : "weeding, cultivating garden, using a hoe, moderate-to-vigorous effort"
            ,8245 : "gardening, general, moderate effort"
            ,8246 : "picking fruit off trees, picking fruits/vegetables, moderate effort"
            ,8248 : "picking fruit off trees, gleaning fruits, picking fruits/vegetables, climbing ladder to pick fruit, vigorous effort"
            ,8250 : "implied walking/standing - picking up yard, light, picking flowers or vegetables"
            ,8251 : "walking, gathering gardening tools"
            ,8255 : "wheelbarrow, pushing garden cart or wheelbarrow"
            ,8260 : "yard work, general, light effort"
            ,8261 : "yard work, general, moderate effort"
            ,8262 : "yard work, general, vigorous effort"}

        self.metDescription_fr  = {8009 : "porter, charger ou empiler du bois, charger/décharger ou transporter du bois de charpente, effort léger à modéré"
        ,8010 : "porter, charger ou empiler du bois, charger/décharger ou transporter du bois de charpente"
        ,8019 : "couper du bois, fendre des bûches, effort modéré"
        ,8020 : "couper du bois, fendre des bûches, effort vigoureux"
        ,8025 : "débroussailler, éclaircir un jardin, effort modéré"
        ,8030 : "débroussailler, sous-bois ou terrain, porter des branches, tirer une brouette, effort vigoureux"
        ,8040 : "creuser un bac à sable, pelleter du sable"
        ,8045 : "creuser, bêcher, garnir le jardin, composter, effort léger à modéré"
        ,8050 : "creuser, bêcher, garnir le jardin, composter (code Taylor 590)"
        ,8052 : "creuser, bêcher, garnir le jardin, composter, effort vigoureux"
        ,8055 : "conduire un tracteur"
        ,8057 : "abattre des arbres de grande taille"
        ,8058 : "abattre des arbres de taille moyenne à petite"
        ,8060 : "jardiner avec des outils motorisés lourds, labourer un jardin, utiliser une tronçonneuse"
        ,8065 : "jardiner, avec des conteneurs, personnes de plus de 60 ans"
        ,8070 : "canaux d'irrigation, ouvrir et fermer des barrages"
        ,8080 : "poser des pierres concassées"
        ,8090 : "poser du gazon"
        ,8095 : "tondre la pelouse, général"
        ,8100 : "tondre la pelouse, conduire une tondeuse (code Taylor 550)"
        ,8110 : "tondre la pelouse, marcher, tondeuse manuelle (code Taylor 570)"
        ,8120 : "tondre la pelouse, marcher, tondeuse à moteur, effort modéré ou vigoureux"
        ,8125 : "tondre la pelouse, tondeuse à moteur, effort léger ou modéré (code Taylor 590)"
        ,8130 : "utiliser une souffleuse à neige, marcher"
        ,8135 : "planter, rempoter, transplanter des germes ou plantes, effort léger"
        ,8140 : "planter des germes, buissons, penché, effort modéré"
        ,8145 : "planter des cultures ou jardiner, penché, effort modéré"
        ,8150 : "planter des arbres"
        ,8160 : "ratisser la pelouse ou des feuilles, effort modéré"
        ,8165 : "ratisser la pelouse (code Taylor 600)"
        ,8170 : "ratisser le toit avec un grattoir à neige"
        ,8180 : "conduire une souffleuse à neige"
        ,8190 : "mettre en sac de l'herbe, des feuilles"
        ,8192 : "pelleter de la terre ou de la boue"
        ,8195 : "pelleter de la neige, à la main, effort modéré"
        ,8200 : "pelleter de la neige, à la main (code Taylor 610)"
        ,8202 : "pelleter de la neige, à la main, effort vigoureux"
        ,8210 : "tailler des arbustes ou des arbres, outil de coupe manuel"
        ,8215 : "tailler des arbustes ou des arbres, outil de coupe à moteur, utilisation d'un souffleur de feuilles, d'une débroussailleuse, effort modéré"
        ,8220 : "marcher, appliquer de l'engrais ou ensemencer une pelouse, distributeur roulant"
        ,8230 : "arroser la pelouse ou le jardin, debout ou en marchant"
        ,8239 : "désherber, cultiver le jardin, effort léger à modéré"
        ,8240 : "désherber, cultiver le jardin (code Taylor 580)"
        ,8241 : "désherber, cultiver le jardin, avec une houe, effort modéré à vigoureux"
        ,8245 : "jardiner, général, effort modéré"
        ,8246 : "cueillir des fruits sur les arbres, ramasser des fruits/légumes, effort modéré"
        ,8248 : "cueillir des fruits, glaner des fruits, ramasser des fruits/légumes, monter une échelle pour cueillir des fruits, effort vigoureux"
        ,8250 : "impliquant de marcher/d'être debout – récolter le jardin, effort léger, cueillir des fleurs ou ramasser des légumes"
        ,8251 : "marcher, ranger des outils de jardinage"
        ,8255 : "brouetter, pousser un chariot ou une brouette de jardinage"
        ,8260 : "travaux de cour, général, effort léger"
        ,8261 : "travaux de cour, général, effort modéré"
        ,8262 : "travaux de cour, général, effort vigoureux"}        

    def printValues(self):
        print("Beginning dump for 'LawnGarden' ")
        super().printValues()

    def getMetValue(self, code):
        return super().getMetValue(code)

if __name__ == "__main__":
    b = LawnGarden()
    b.printValues()
    print(b.getMetValue(8262))
    for l in b:
        print(l)