import os
import sys
import libs.applibs.compendium.abstractcompendium as abstractcompendium

class Walking(abstractcompendium.Compendium):

    def __init__(self):
        super().__init__()

        self.metValue  = {17010 : 7.0 
            ,17012 : 7.8
            ,17020 : 5.0
            ,17021 : 2.3
            ,17025 : 8.3
            ,17026 : 5.0
            ,17027 : 6.0 
            ,17028 : 8.0 
            ,17029 : 10.0 
            ,17030 : 12.0 
            ,17031 : 3.5
            ,17033 : 6.3
            ,17035 : 6.5
            ,17040 : 7.3
            ,17050 : 8.3 
            ,17060 : 9.0 
            ,17070 : 3.5 
            ,17080 : 6.0 
            ,17082 : 5.3
            ,17085 : 2.5 
            ,17088 : 4.5
            ,17090 : 8.0 
            ,17100 : 4.0
            ,17105 : 3.8 
            ,17110 : 6.5 
            ,17130 : 8.0 
            ,17133 : 4.0
            ,17134 : 8.8
            ,17140 : 5.0
            ,17150 : 2.0 
            ,17151 : 2.0
            ,17152 : 2.8 
            ,17160 : 3.5 
            ,17161 : 2.5 
            ,17162 : 2.5 
            ,17165 : 3.0 
            ,17170 : 3.0 
            ,17180 : 3.3 
            ,17190 : 3.5 
            ,17200 : 4.3
            ,17210 : 5.3
            ,17211 : 8.0
            ,17220 : 5.0 
            ,17230 : 7.0
            ,17231 : 8.3 
            ,17235 : 9.8
            ,17250 : 3.5 
            ,17260 : 4.8
            ,17262 : 4.5
            ,17270 : 4.0 
            ,17280 : 2.5 
            ,17302 : 4.8
            ,17305 : 9.5
            ,17310 : 6.8
            ,17320 : 6.0
            ,17325 : 8.0}

        # Unpacking with * works with any object that is iterable and, since dictionaries return their keys when iterated through, you can easily create a list by using it within a list literal.
        self.ckeys = [*self.metValue] # another option : list(self.metValue.keys())

        self.metDescription  = {17010 : "backpacking (Taylor Code 050)"
            ,17012 : "backpacking, hiking or organized walking with a daypack"
            ,17020 : "carrying 15 pound load (e.g. suitcase), level ground or downstairs"
            ,17021 : "carrying 15 lb child, slow walking"
            ,17025 : "carrying load upstairs, general"
            ,17026 : "carrying 1 to 15 lb load, upstairs"
            ,17027 : "carrying 16 to 24 lb load, upstairs"
            ,17028 : "carrying 25 to 49 lb load, upstairs"
            ,17029 : "carrying 50 to 74 lb load, upstairs"
            ,17030 : "carrying > 74 lb load, upstairs"
            ,17031 : "loading /unloading a car, implied walking"
            ,17033 : "climbing hills, no load"
            ,17035 : "climbing hills with 0 to 9 lb load"
            ,17040 : "climbing hills with 10 to 20 lb load"
            ,17050 : "climbing hills with 21 to 42 lb load"
            ,17060 : "climbing hills with 42+ lb load"
            ,17070 : "descending stairs"
            ,17080 : "hiking, cross country (Taylor Code 040)"
            ,17082 : "hiking or walking at a normal pace through fields and hillsides"
            ,17085 : "bird watching, slow walk"
            ,17088 : "marching, moderate speed, military, no pack"
            ,17090 : "marching rapidly, military, no pack"
            ,17100 : "pushing or pulling stroller with child or walking with children, 2.5 to 3.1 mph"
            ,17105 : "pushing a wheelchair, non-occupational "
            ,17110 : "race walking"
            ,17130 : "stair climbing, using or climbing up ladder (Taylor Code 030)"
            ,17133 : "stair climbing, slow pace"
            ,17134 : "stair climbing, fast pace"
            ,17140 : "using crutches"
            ,17150 : "walking, household"
            ,17151 : "walking, less than 2.0 mph, level, strolling, very slow"
            ,17152 : "walking, 2.0 mph, level, slow pace, firm surface"
            ,17160 : "walking for pleasure (Taylor Code 010)"
            ,17161 : "walking from house to car or bus, from car or bus to go places, from car or bus to and from the worksite"
            ,17162 : "walking to neighbor’s house or family’s house for social reasons"
            ,17165 : "walking the dog"
            ,17170 : "walking, 2.5 mph, level, firm surface"
            ,17180 : "walking, 2.5 mph, downhill"
            ,17190 : "walking, 2.8 to 3.2 mph, level, moderate pace, firm surface"
            ,17200 : "walking, 3.5 mph, level, brisk, firm surface, walking for exercise"
            ,17210 : "walking, 2.9 to 3.5 mph, uphill, 1 to 5% grade"
            ,17211 : "walking, 2.9 to 3.5 mph, uphill, 6% to 15% grade"
            ,17220 : "walking, 4.0 mph, level, firm surface, very brisk pace"
            ,17230 : "walking, 4.5 mph, level, firm surface, very, very brisk"
            ,17231 : "walking, 5.0 mph, level, firm surface"
            ,17235 : "walking, 5.0 mph, uphill, 3% grade"
            ,17250 : "walking, for pleasure, work break"
            ,17260 : "walking, grass track"
            ,17262 : "walking, normal pace, plowed field or sand"
            ,17270 : "walking, to work or class (Taylor Code 015)"
            ,17280 : "walking, to and from an outhouse"
            ,17302 : "walking, for exercise, 3.5 to 4 mph, with ski poles, Nordic walking, level, moderate pace"
            ,17305 : "walking, for exercise, 5.0 mph, with ski poles, Nordic walking, level, fast pace"
            ,17310 : "walking, for exercise, with ski poles, Nordic walking, uphill"
            ,17320 : "walking, backwards, 3.5 mph, level"
            ,17325 : "walking, backwards, 3.5 mph, uphill, 5% grade"}

        self.metDescription_fr  = {17010 : "randonnée (code Taylor 050)"
            ,17012 : "randonnée ou marche organisée avec un sac à dos"
            ,17020 : "porter une charge de 7 kg (par ex. valise), à plat ou en descendant des escaliers"
            ,17021 : "porter un enfant de 7 kg, marche lente"
            ,17025 : "porter une charge en montant des escaliers, général"
            ,17026 : "porter une charge de 0,5-7 kg en montant des escaliers"
            ,17027 : "porter une charge de 7-11 kg en montant des escaliers"
            ,17028 : "porter une charge de 11-22 kg en montant des escaliers"
            ,17029 : "porter une charge de 22-33 kg en montant des escaliers"
            ,17030 : "porter une charge > 34 kg en montant des escaliers"
            ,17031 : "charger/décharger une voiture impliquant de la marche"
            ,17033 : "randonner en collines, sans charge"
            ,17035 : "randonner en collines en portant une charge de 0 à 4 kg"
            ,17040 : "randonner en collines en portant une charge de 4,5 à 9 kg"
            ,17050 : "randonner en collines en portant une charge de 9,5 à 19 kg"
            ,17060 : "randonner en collines en portant une charge supérieure à 19 kg"
            ,17070 : "descendre des escaliers"
            ,17080 : "randonnée, à travers champs (code Taylor 040)"
            ,17082 : "randonner ou marcher à allure normale à travers champs et versants de colline"
            ,17085 : "admirer les oiseaux, marche lente"
            ,17088 : "marche militaire, vitesse modérée, sans sac"
            ,17090 : "marche militaire rapide, sans sac"
            ,17100 : "pousser ou tirer une poussette avec un enfant ou marcher avec des enfants, 4 à 5 km/h"
            ,17105 : "pousser un fauteuil roulant, cadre privé"
            ,17110 : "marche athlétique"
            ,17130 : "monter des escaliers, utiliser ou monter sur une échelle (code Taylor 030)"
            ,17133 : "monter des escaliers, rythme lent"
            ,17134 : "monter des escaliers, rythme rapide"
            ,17140 : "utiliser des béquilles"
            ,17150 : "marcher à la maison"
            ,17151 : "marcher à moins de 3 km/h, à plat, flâner, rythme très lent"
            ,17152 : "marcher à 3 km/h, à plat, rythme lent, sol ferme"
            ,17160 : "marcher pour le plaisir (code Taylor 010)"
            ,17161 : "marcher de la maison à la voiture ou au bus, de la voiture ou du bus vers d'autres endroits, de la voiture ou du bus vers et depuis le lieu de travail"
            ,17162 : "marcher vers la maison du voisin ou la maison familiale dans un but social"
            ,17165 : "promener le chien"
            ,17170 : "marcher à 4 km/h, à plat, sol ferme"
            ,17180 : "marcher à 4 km/h, en descente"
            ,17190 : "marcher à 4,5-5 km/h, à plat, rythme modéré, sol ferme"
            ,17200 : "marcher à 5,5 km/h, à plat, rythme rapide, sol ferme, marcher pour faire de l'exercice"
            ,17210 : "marcher à 4,5-5,5 km/h, en montée de 1 à 5 %"
            ,17211 : "marcher à 4,5-5,5 km/h, en montée de 6-15 %"
            ,17220 : "marcher à 6,5 km/h, à plat, sol ferme, rythme très rapide"
            ,17230 : "marcher à 7 km/h, à plat, sol ferme, rythme extrêmement rapide"
            ,17231 : "marcher à 8 km/h, à plat, sol ferme"
            ,17235 : "marcher à 8 km/h, en montée de 3 %"
            ,17250 : "marcher pour le plaisir, pause de travail"
            ,17260 : "marcher dans l'herbe"
            ,17262 : "marcher à un rythme normal, dans un champ labouré ou dans du sable"
            ,17270 : "marcher pour aller au travail ou à l'école (code Taylor 015)"
            ,17280 : "marcher vers et depuis une dépendance"
            ,17302 : "marcher pour l’exercice à 5,5-6,5 km/h avec des bâtons de ski, marche nordique, à plat, rythme modéré"
            ,17305 : "marcher pour l’exercice à 8 km/h avec des bâtons de ski, marche nordique, à plat, rythme rapide"
            ,17310 : "marcher pour l’exercice avec des bâtons de ski, marche nordique, en montée"
            ,17320 : "marcher, en arrière, 5,5 km/h, à plat"
            ,17325 : "marcher, en arrière à 5,5 km/h, en montée de 5%"}


    def printValues(self):
        print("Beginning dump for 'Walking' ")
        super().printValues()

    def getMetValue(self, code):
        return super().getMetValue(code)

if __name__ == "__main__":
    b = Walking()
    b.printValues()
    print(b.getMetValue(17140))
    for l in b:
        print(l)